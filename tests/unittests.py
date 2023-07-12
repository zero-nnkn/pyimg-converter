from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

import PIL

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))

from src.pyimg_converter import convert_from_path

SAMPLE_PATH = FILE.parent / 'samples'


class FileToImageTestCase(unittest.TestCase):
    def test_convert_png_to_image(self):
        file_path = SAMPLE_PATH / 'sample.png'
        result = convert_from_path(file_path)
        for image in result:
            self.assertIsInstance(image, PIL.Image.Image)

    def test_convert_heic_to_image(self):
        file_path = SAMPLE_PATH / 'sample.heic'
        result = convert_from_path(file_path)
        for image in result:
            self.assertIsInstance(image, PIL.Image.Image)

    def test_convert_tiff_to_image(self):
        file_path = SAMPLE_PATH / 'sample.tiff'
        result = convert_from_path(file_path)
        for image in result:
            self.assertIsInstance(image, PIL.Image.Image)

    def test_convert_pdf_to_image(self):
        file_path = SAMPLE_PATH / 'sample.pdf'
        result = convert_from_path(file_path)
        for image in result:
            self.assertIsInstance(image, PIL.Image.Image)

    def test_convert_invalid_format(self):
        file_path = SAMPLE_PATH / 'sample.txt'
        with self.assertRaises(ValueError):
            convert_from_path(file_path)


if __name__ == '__main__':
    unittest.main()
