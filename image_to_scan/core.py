import logging
import re
from collections import namedtuple
from itertools import islice
from operator import attrgetter

import cv2
import numpy as np

logging.basicConfig()

log = logging.getLogger(__name__)


def previewImage(window_name: str,
                 image: np.ndarray,
                 wait_miliseconds_before_destroy: int = 2000):
    log.debug(f"Showing {window_name}")
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name,
                          prop_id=cv2.WND_PROP_FULLSCREEN,
                          prop_value=cv2.WINDOW_NORMAL)

    cv2.imshow(window_name, image)
    cv2.waitKey(wait_miliseconds_before_destroy)
    cv2.destroyAllWindows()


def previewContours(image, contours):
    green = (0, 255, 0)
    image = cv2.drawContours(image, contours,
                             contourIdx=-1, color=green, thickness=10)
    previewImage("contours", image)


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

    # # multiply the rectangle by the original ratio
    # rect *= ratio

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


def findLargestContours(cntList, cntWidths):
    """Finds two largest contours, they may be, our full image and our rectangle
    edged object.

    """
    newCntList = []
    newCntWidths = []

    # finding 1st largest rectangle
    first_largest_cnt_pos = cntWidths.index(max(cntWidths))

    # adding it in new
    newCntList.append(cntList[first_largest_cnt_pos])
    newCntWidths.append(cntWidths[first_largest_cnt_pos])

    # removing it from old
    cntList.pop(first_largest_cnt_pos)
    cntWidths.pop(first_largest_cnt_pos)

    # finding second largest rectangle
    seccond_largest_cnt_pos = cntWidths.index(max(cntWidths))

    # adding it in new
    newCntList.append(cntList[seccond_largest_cnt_pos])
    newCntWidths.append(cntWidths[seccond_largest_cnt_pos])

    # removing it from old
    cntList.pop(seccond_largest_cnt_pos)
    cntWidths.pop(seccond_largest_cnt_pos)

    log.debug("findLargestContours: Old Screen Dimentions filtered %s", cntWidths)
    log.debug("findLargestContours: Screen Dimentions filtered %s", newCntWidths)
    return newCntList, newCntWidths


def save_image(src_file_path, image, suffix="-scanned", extension="jpg"):
    """Given the original image name, saves a new modified image with
    desired suffix next to it myimage.jpg myimage-warped.jpg.

    :param src_file_path: Original file path
    :param image: modified imagee
    :param suffix: string to be added to the new image name
    """

    new_file_path = re.sub(
        r"\.(?P<extension>.*)$",
        fr"{suffix}.{extension}",
        src_file_path,
    )
    cv2.imwrite(new_file_path, image)


def convert_object(file_path, screen_size=None, new_file_suffix="-scanned"):
    """ Identifies 4 corners and does four point transformation """
    debug = True if log.level == logging.DEBUG else False
    image = cv2.imread(str(file_path))

    # image = imutils.resize(image, height=300)
    # ratio = image.shape[0] / 300.0

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

    imageCopy = image.copy()

    # approximate the contour
    ContourArea = namedtuple('ContourArea', ['curve', 'area'])
    contourAreas = [ContourArea(curve=x, area=cv2.contourArea(x))
                    for x in contours]
    contourAreas = sorted(contourAreas, key=attrgetter('area'))

    if debug:
        previewContours(imageCopy, [x.curve for x in contourAreas])

    four_edge_polygons = []
    polygonWidths = []
    for contour in contourAreas:
        peri = cv2.arcLength(contour.curve, True)
        polygon_less_vertices = cv2.approxPolyDP(contour.curve,
                                                 epsilon=0.02 * peri,  # approximation accuracy
                                                 closed=True)

        num_vertices = len(polygon_less_vertices)
        if num_vertices == 4:
            (X, Y, W, H) = cv2.boundingRect(contour.curve)
            log.debug(f'X={X} Y={Y} W={W} H={H}')
            four_edge_polygons.append(polygon_less_vertices)
            polygonWidths.append(W)

    log.debug("Screens found : %s", len(four_edge_polygons))
    previewContours(imageCopy, four_edge_polygons)
    log.debug("Screen Dimentions %s", polygonWidths)

    four_edge_polygons, polygonWidths = findLargestContours(
        four_edge_polygons, polygonWidths
    )

    if not len(four_edge_polygons) >= 2:
        raise RuntimeError("No rectangle found")

    if polygonWidths[0] != polygonWidths[1]:
        raise RuntimeError(f"Rectangle mismatch: {polygonWidths}")

    if debug:
        previewContours(image, [four_edge_polygons[0]])

    # now that we have our screen contour, we need to determine
    # the top-left, top-right, bottom-right, and bottom-left
    # points so that we can later warp the image -- we'll start
    # by reshaping our contour to be our finals and initializing
    # our output rectangle in top-left, top-right, bottom-right,
    # and bottom-left order
    pts = four_edge_polygons[0].reshape(4, 2)
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

    save_image(file_path, warp, suffix=new_file_suffix)

    if screen_size:
        return cv2.cvtColor(
            cv2.resize(warp, screen_size), cv2.COLOR_GRAY2RGB
        )
    else:
        return cv2.cvtColor(warp, cv2.COLOR_GRAY2RGB)
