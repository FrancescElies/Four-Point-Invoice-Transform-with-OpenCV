# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

package = "image-to-scan"
description = "Helps you transform a photo to a scanned document"
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=package,
    version="0.0.6",
    install_requires=[
        "opencv-python-headless",
        "numpy",
        "typer[all]",
        "schema",
        "setuptools",
        # "imutils",
        # "scikit-image",
    ],
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    url="https://github.com/FrancescElies/image-to-scan",
    python_requires=">=3.0",
    test_suite="tests.test_project",
    entry_points={
        "console_scripts": [
            "image-to-scan = image_to_scan.app:app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ],
)
