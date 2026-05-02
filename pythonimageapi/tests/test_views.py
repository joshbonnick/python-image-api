import unittest

from django.test import RequestFactory

from pythonimageapi.views import images


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_svg_returns_svg_response(self):
        request = self.factory.get("/svg/200/ff0000")
        response = images.svg(request, 200, "ff0000")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'image/svg+xml')

if __name__ == '__main__':
    unittest.main()
