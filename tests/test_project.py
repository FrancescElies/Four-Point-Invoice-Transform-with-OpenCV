# -*- coding: utf-8 -*-
import filecmp
import os

import image_to_scan


class TestMiscellanea:
    def test_import(self):
        assert image_to_scan is not None


class TestSamples:
    def test_sample_02(self):
        input_file = "tests/samples/02/original.png"
        reference_file = "tests/samples/02/original-scanned.png"
        output_file = "tests/samples/02/original-test.png"
        image_to_scan.convert_object(input_file, new_file_suffix="-test")
        assert filecmp.cmp(reference_file, output_file)
        os.remove(output_file)
