from unittest import TestCase

from pythonimageapi.images.svg_generator import SvgGenerator


class TestSvgGenerator(TestCase):
    def setUp(self):
        self.generator = SvgGenerator()

    def test_generate_svg(self):
        svg = self.generator.generate_svg(100, 100, "ff0000")
        self.assertIn('<svg', svg)
        self.assertIn('width="100"', svg)
        self.assertIn('height="100"', svg)
        self.assertIn('fill="#ff0000"', svg)

    def test_detect_color_format(self):
        self.assertEqual(self.generator.detect_color_format("#000000"), "hex")
        self.assertEqual(self.generator.detect_color_format("ff0000"), "hex")
        self.assertEqual(self.generator.detect_color_format("ffFF00"), "hex")
        self.assertEqual(self.generator.detect_color_format("rgb(255,255,232)"), "rgb")
        self.assertEqual(self.generator.detect_color_format("rgb(255,255,232,123)"), "rgba")
        self.assertEqual(self.generator.detect_color_format("rgba(255,255,232,256)"), "rgba")

    def test_rgb_to_hex(self):
        self.assertEqual(self.generator.rgb_to_hex(255, 255, 255), "#ffffff")
        self.assertEqual(self.generator.rgb_to_hex(0, 0, 0), "#000000")
        self.assertEqual(self.generator.rgb_to_hex(128, 128, 128), "#808080")
        self.assertEqual(self.generator.rgb_to_hex(255, 0, 0), "#ff0000")
        self.assertEqual(self.generator.rgb_to_hex(0, 255, 0), "#00ff00")
        self.assertEqual(self.generator.rgb_to_hex(0, 0, 255), "#0000ff")
