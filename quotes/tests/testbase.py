from flask_testing import TestCase
from quotes.config import TestConfig
from quotes import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    # def tearDown(self):
    #     db.drop_all()
    #     db.session.commit()
