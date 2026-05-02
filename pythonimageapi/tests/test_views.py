import unittest

from django.test import RequestFactory, TestCase

from pythonimageapi.views import images


class ViewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_svg_returns_svg_response(self):
        request = self.factory.get("/svg/200/ff0000", data={"text": "::foo::"})
        response = images.svg(request, 200, "ff0000")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'image/svg+xml')

        svg = response.content.decode('utf-8')

        self.assertIn('<svg', svg)
        self.assertIn('width="200"', svg)
        self.assertIn('height="200"', svg)
        self.assertIn('fill="#ff0000"', svg)
        self.assertIn('::foo::', svg)

if __name__ == '__main__':
    unittest.main()
