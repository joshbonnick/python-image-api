import unittest

from django.test import RequestFactory

from pythonimageapi.views import test


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_images_returns_ok_response(self):
        request = self.factory.get("/images")

        response = test.index(request)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
