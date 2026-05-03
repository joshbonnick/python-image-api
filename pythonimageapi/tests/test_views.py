import unittest

from django.test import RequestFactory, TestCase

from images.views import SvgImages


class ViewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_svg_returns_svg_response(self):
        request = self.factory.get("/svg/200/ff0000")
        response = SvgImages().get(request, "200", "ff0000")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'image/svg+xml')

        svg_bytes = b"".join(response.streaming_content)
        svg = svg_bytes.decode("utf-8")

        self.assertIn('<svg', svg)
        self.assertIn('width="200"', svg)
        self.assertIn('height="200"', svg)
        self.assertIn('fill="#ff0000"', svg)

        request = self.factory.get("/svg/300x400/00ff00")
        response = SvgImages().get(request, "300x400", "00ff00")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'image/svg+xml')

        svg_bytes = b"".join(response.streaming_content)
        svg = svg_bytes.decode("utf-8")

        self.assertIn('<svg', svg)
        self.assertIn('width="300"', svg)
        self.assertIn('height="400"', svg)
        self.assertIn('fill="#00ff00"', svg)
        self.assertNotIn('<text', svg)

    def test_accepts_various_url_styles(self):
        request = self.factory.get("/svg/200")
        response = SvgImages().get(request, "200")

        svg_bytes = b"".join(response.streaming_content)
        svg = svg_bytes.decode("utf-8")
        self.assertIn('<svg', svg)
        self.assertIn('width="200"', svg)

    def test_svg_accepts_text(self):
        request = self.factory.get("/svg/200/ff0000", data={"text": "::foo::"})
        response = SvgImages().get(request, "200", "ff0000")

        svg_bytes = b"".join(response.streaming_content)
        svg = svg_bytes.decode("utf-8")

        self.assertIn('<svg', svg)
        self.assertIn('::foo::', svg)

if __name__ == '__main__':
    unittest.main()
