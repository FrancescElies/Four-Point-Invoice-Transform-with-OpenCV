# -*- coding: utf-8 -*-
import os

import image_to_scan


class TestMiscellanea:
    def test_import(self):
        assert image_to_scan is not None


class TestSamples:
    def teardown_method(self, method):
        os.remove(self.output_file)

    def test_sample_02(self):
        input_file = "tests/samples/02/original.jpg"
        input_file_no_ext = input_file.split(".")[0]
        suffix = "warped"
        extension = "jpg"
        self.output_file = f"{input_file_no_ext}-{suffix}.{extension}"
        image_to_scan.convert_object(input_file, new_file_suffix=f"-{suffix}")
        assert os.path.exists(self.output_file)
