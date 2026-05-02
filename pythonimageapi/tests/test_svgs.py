import unittest

from pythonimageapi.images.svg_generator import SvgGenerator


class SvgsTestCase(unittest.TestCase):
    def test_hex_is_detected(self):
        generator = SvgGenerator()

        self.assertEqual(generator.detect_color_format("#000000"), "hex")
        self.assertEqual(generator.detect_color_format("rgb(255,255,232)"), "rgb")
        self.assertEqual(generator.detect_color_format("rgb(255,255,232,123)"), "rgb")
        self.assertEqual(generator.detect_color_format("rgba(255,255,232,256)"), "rgb")


if __name__ == '__main__':
    unittest.main()
