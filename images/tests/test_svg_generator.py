from unittest import TestCase

from images.services.svg_generator import SvgGenerator


class TestSvgGenerator(TestCase):
    def setUp(self):
        self.generator = SvgGenerator()

    def test_generate_svg(self):
        svg = self.generator.generate_svg(100, 100, "ff0000", "::foo::")
        self.assertIn('<svg', svg)
        self.assertIn('width="100"', svg)
        self.assertIn('height="100"', svg)
        self.assertIn('fill="#ff0000"', svg)
        self.assertIn('::foo::', svg)
