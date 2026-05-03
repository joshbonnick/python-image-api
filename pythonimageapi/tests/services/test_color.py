from django.test import SimpleTestCase

from pythonimageapi.images.services import color


class TestSvgGenerator(SimpleTestCase):
    def test_detect_color_format(self):
        self.assertEqual(color.detect_color_format("#000000"), "hex")
        self.assertEqual(color.detect_color_format("ff0000"), "hex")
        self.assertEqual(color.detect_color_format("ffFF00"), "hex")
        self.assertEqual(color.detect_color_format("rgb(255,255,232)"), "rgb")
        self.assertEqual(color.detect_color_format("rgb(255,255,232,123)"), "rgba")
        self.assertEqual(color.detect_color_format("rgba(255,255,232,256)"), "rgba")

    def test_rgb_to_hex(self):
        self.assertEqual(color.rgb_to_hex(255, 255, 255), "#ffffff")
        self.assertEqual(color.rgb_to_hex(0, 0, 0), "#000000")
        self.assertEqual(color.rgb_to_hex(128, 128, 128), "#808080")
        self.assertEqual(color.rgb_to_hex(255, 0, 0), "#ff0000")
        self.assertEqual(color.rgb_to_hex(0, 255, 0), "#00ff00")
        self.assertEqual(color.rgb_to_hex(0, 0, 255), "#0000ff")
