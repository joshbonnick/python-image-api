import unittest

from django.test import RequestFactory

from pythonimageapi.views import images


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_svg_returns_ok_response(self):
        request = self.factory.get("/images")

        response = images.svg(request)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
