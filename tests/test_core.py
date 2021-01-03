# -*- coding: utf-8 -*-
import os
from pathlib import Path

import image_to_scan


class TestMiscellanea:
    def test_import(self):
        assert image_to_scan is not None


class TestSamples:
    def teardown_method(self, method):
        os.remove(self.output_file)

    def test_sample_02(self):
        input_file = Path("tests/samples/02/original.jpg")
        suffix = "warped"
        extension = "jpg"
        self.output_file = input_file.parent / f"{input_file.stem}-{suffix}.{extension}"
        image_to_scan.convert_object(input_file, new_file_suffix=f"{suffix}")
        assert self.output_file.exists()
