# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

package = "image-to-scan"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=package,
    version="0.0.5",
    install_requires=[
        "opencv-python-headless",
        "numpy",
        "docopt",
        "schema",
        # "imutils",
        # "scikit-image",
    ],
    description="Convert photos of documents made "
    "with a camera to a 'scanned' documents. "
    "It will take documents' contour and apply a "
    "four point transformation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    zip_safe=False,
    url="https://github.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV",
    python_requires=">=3.0",
    test_suite="tests.test_project",
    entry_points={
        "console_scripts": [
            "image-to-scan = image_to_scan.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ],
)
