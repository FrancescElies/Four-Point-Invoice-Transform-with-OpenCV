# -*- coding: utf-8 -*-

from setuptools import setup

import photo_to_scan

package = "photo-to-scan"
version = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=package,
    version=version,
    install_requires=[
        "opencv-python",
        "imutils",
        "numpy",
        "scikit-image",
        "docopt",
        "schema",
    ],
    description="Convert photos of documents made "
    "with a camera to a 'scanned' documents. "
    "It will the documents' contour and apply a "
    "four point transformation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV",
    entry_points={
        "console_scripts": [
            "photo-to-scan = photo_to_scan.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ],
)
