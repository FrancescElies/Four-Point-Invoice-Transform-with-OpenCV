import logging
from enum import Enum
from pathlib import Path
from typing import List, Optional

import typer

from image_to_scan.core import convert_object, log

app = typer.Typer()


class Loglevel(str, Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"


class ImageExtension(str, Enum):
    # Windows bitmaps
    bmp = "bmp"
    dib = "dib"
    # JPEG
    jpeg = "jpeg"
    jpg = "jpg"
    jpe = "jpe"
    jp2 = "jp2"
    # Portable Network Graphics
    png = "png"
    # WebP
    webp = "webp"
    # Portable image format
    pbm = "pbm"
    pgm = "pgm"
    ppm = "ppm"
    pxm = "pxm"
    pnm = "pnm"
    # PFM
    pfm = "pfm"
    # Sun rasters
    sr = "sr"
    ras = "ras"
    # TIFF
    tiff = "tiff"
    tif = "tif"
    # OpenEXR Image
    exr = "exr"
    # Radiance HDR
    hdr = "hdr"
    pic = "pic"


@app.command()
def main(files: Optional[List[Path]],
         loglevel: Loglevel = Loglevel.INFO,
         output_extension: ImageExtension = ImageExtension.jpg):
    """
    Four Point Invoice Transform with OpenCV

    https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/

    """

    log.setLevel(logging.getLevelName(loglevel.upper()))

    for file_path in files:
        convert_object(file_path)


if __name__ == "__main__":
    app()
