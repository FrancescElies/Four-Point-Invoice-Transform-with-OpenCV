# -*- coding: utf-8 -*-

from setuptools import setup

import photo_to_scan

package = "photo-to-scan"
version = "0.0.1"


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
    description=photo_to_scan.__doc__.strip(),
    entry_points={
        "console_scripts": [
            "photo-to-scan = photo_to_scan.__main__:main"
        ]
    },
)
