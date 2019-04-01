from quotes.tests.testbase import BaseTestCase
import unittest


class TestMain(BaseTestCase):
    def test_home(self):
        with self.client:
            response = self.client.get('/', follow_redirects=True)
            self.assertIn(b'', response.data)
            assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
