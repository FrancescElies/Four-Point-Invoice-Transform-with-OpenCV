import logging
from collections import namedtuple
from operator import attrgetter

import cv2
import numpy as np

logging.basicConfig()

log = logging.getLogger(__name__)


Screen = namedtuple('Screen', ['fourpoints', 'width'])


def previewImage(window_name: str,
                 image: np.ndarray,
                 wait_miliseconds_before_destroy: int = 2000):
    log.debug(f"Showing {window_name}")
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    # Hack: setting WINDOW_FULLSCREEN and backt to WINDOW_NORMAL makes sure
    # image is presented at the front over other windows.
    cv2.setWindowProperty(window_name,
                          prop_id=cv2.WND_PROP_FULLSCREEN,
                          prop_value=cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    cv2.setWindowProperty(window_name,
                          prop_id=cv2.WND_PROP_FULLSCREEN,
                          prop_value=cv2.WINDOW_NORMAL)

    cv2.imshow(window_name, image)
    cv2.waitKey(wait_miliseconds_before_destroy)
    cv2.destroyAllWindows()


def previewContours(image, contours, thickness=5):
    green = (0, 255, 0)
    _image = image.copy()

    _image = cv2.drawContours(_image, contours,
                              contourIdx=-1, color=green, thickness=thickness)
    previewImage("contours", _image)


def order_points(pts):
    """ Orders points to a proper rectangle """
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    _sum = pts.sum(axis=1)
    rect[0] = pts[np.argmin(_sum)]
    rect[2] = pts[np.argmax(_sum)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect


def transform_to_four_points(image, pts):
    """Apply the four point tranform to obtain a "birds eye view" of the image """

    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)

    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array(
        [
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1],
        ],
        dtype="float32",
    )

    # compute the perspective transform matrix and then apply it
    transform_matrix = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, transform_matrix, (maxWidth, maxHeight))

    # return the warped image
    return warped


def convert_object(file_path, screen_size=None, new_file_suffix="scanned"):
    """ Identifies 4 corners and does four point transformation """
    debug = True if log.level == logging.DEBUG else False
    image = cv2.imread(str(file_path))

    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(
        gray, 11, 17, 17
    )  # 11  //TODO 11 FRO OFFLINE MAY NEED TO TUNE TO 5 FOR ONLINE

    gray = cv2.medianBlur(gray, 5)
    edged = cv2.Canny(gray, 30, 400)

    if debug:
        previewImage("Edged Image", edged)

    # find contours in the edged image, keep only the largest
    # ones, and initialize our screen contour

    contours, hierarcy = cv2.findContours(
        edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE
    )

    log.debug("Contours found: %s", len(contours))


    # approximate the contour
    ContourArea = namedtuple('ContourArea', ['curve', 'area'])
    contourAreas = [ContourArea(curve=x, area=cv2.contourArea(x))
                    for x in contours]
    contourAreas = sorted(contourAreas, key=attrgetter('area'))

    if debug:
        previewContours(image, [x.curve for x in contourAreas])

    screens = []  # 4 point polygons, repressenting possible screens (rectangles)
    for contour in contourAreas:
        peri = cv2.arcLength(contour.curve, True)
        polygon_less_vertices = cv2.approxPolyDP(contour.curve,
                                                 epsilon=0.02 * peri,  # approximation accuracy
                                                 closed=True)

        num_vertices = len(polygon_less_vertices)
        if num_vertices == 4:
            (x, y, width, height) = cv2.boundingRect(contour.curve)
            log.debug(f'x={x} y={y} width={width} height={height}')
            screens.append(Screen(fourpoints=polygon_less_vertices, width=width))

    log.debug(f"Screens found {len(screens)}: {screens}")
    previewContours(image, [x.fourpoints for x in screens])

    # find largest screen
    largest_screen = max(screens, key=attrgetter('width'))

    if debug:
        previewContours(image, [largest_screen.fourpoints])

    # now that we have our screen contour, we need to determine
    # the top-left, top-right, bottom-right, and bottom-left
    # points so that we can later warp the image -- we'll start
    # by reshaping our contour to be our finals and initializing
    # our output rectangle in top-left, top-right, bottom-right,
    # and bottom-left order
    pts = largest_screen.fourpoints.reshape(4, 2)
    log.debug("Found bill rectagle at %s", pts)
    rect = order_points(pts)
    log.debug(rect)

    warped = transform_to_four_points(image, pts)

    # convert the warped image to grayscale and then adjust
    # the intensity of the pixels to have minimum and maximum
    # values of 0 and 255, respectively
    warp = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    # Replacement for `skimage.exposure.rescale_intensity`
    # Contrast Limited Adaptive Histogram Equalization
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
    warp = clahe.apply(warp)

    # show the original and warped images
    if debug:
        previewImage("Original", image)
        previewImage("warp", warp)

    warp_file = str(file_path.parent / f"{file_path.stem}-{new_file_suffix}.jpg")
    cv2.imwrite(warp_file, warp)
    log.debug(f"Result: {warp_file}")

    if screen_size:
        return cv2.cvtColor(
            cv2.resize(warp, screen_size), cv2.COLOR_GRAY2RGB
        )
    else:
        return cv2.cvtColor(warp, cv2.COLOR_GRAY2RGB)
