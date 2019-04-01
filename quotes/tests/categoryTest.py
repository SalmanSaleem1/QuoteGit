import unittest
from quotes.tests.testbase import BaseTestCase
from quotes.categories.utils import savePicture
from quotes.categories.forms import AddNewCategoryForm
from PIL import Image
import glob


class TestCategory(BaseTestCase):
    def test_category(self):
        # path = "/home/salman/PythonWork/quote-app-svs/quotes/static/cat_images/default.jpg"
        # for file in glob.glob(path):
        #     print(file)
        response = self.client.post('/add_new_category', data=dict(
            category_name='salman'
        ), follow_redirects=True)
        self.assertIn(b'', response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
