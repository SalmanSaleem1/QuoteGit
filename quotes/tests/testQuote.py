from quotes.tests.testbase import BaseTestCase
import unittest
from flask import request
from quotes.quote.forms import NewQuoteForm
from quotes.models import Categories, Quotes


class TestQuotes(BaseTestCase):
    def test_quote(self):
        with self.client:
            response = self.client.get('http://127.0.0.1:5000/1', follow_redirects=True)
            self.assertIn(b'', response.data)
            self.assertEqual(response.status_code, 200)

    def test_quote_delete(self):
        with self.client:
            response = self.client.get('/delete/1', follow_redirects=True)
            self.assertIn(b'', response.data)
            assert response.status_code == 200

    def test_quote_update(self):
        if request.method == "POST":
            cat = request.form.get('select_value')
        else:
            cat = None
        form = NewQuoteForm()
        categories = Categories.query.all()
        #
        # cat_id = []
        for one_cat in categories:
            if cat == one_cat.category_name:
                cat_id = one_cat.category_name
                break
        with self.client:
            response = self.client.get('/1', follow_redirects=True)
            self.assertIn(b'', response.data)
            assert response.status_code == 200

            response = self.client.post('/add_quote', data=dict(
                category_id=cat_id, quote='salman saleem is a good developer'
            ))

            self.assertIn(b'', response.data)
            self.assertEqual(response.status_code, 200)


class TestNewQuote(BaseTestCase):
    def test_new_post_case(self):
        self.client.post('/add_new_category', data=dict(
            category_name='sad'
        ), follow_redirects=True)
        response = self.client.post('/http://127.0.0.1:5000/add_quote', data=dict(
            category_id='love', quote='salman saleem is a good developer', language='English', color_code='#FFFF',
            font_family='Arial'
        ))

        response = self.client.get('/', data=dict(
            category_id='love', quote='salman saleem is a good developer'
        ))
        self.assertIn(b'', response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
