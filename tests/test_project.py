# -*- coding: utf-8 -*-

import image_to_scan


class Tests:
    def test_import(self):
        assert image_to_scan is not None

    def test_sample_02(self):
        image_to_scan.convert_object("tests/samples/02/original.png")
