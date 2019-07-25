# -*- coding: utf-8 -*-

"""Converts a photo taken from a document and transforms in such a way
it looks like as if you scanned it. Uses 4 Point OpenCV perspective
transform.

"""

import pkg_resources

from .core import convert_object  # noqa: F401

try:
    __version__ = pkg_resources.get_distribution('setuptools').version
except Exception:
    __version__ = 'unknown'
