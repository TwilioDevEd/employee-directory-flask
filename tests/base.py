from xmlunittest import XmlTestCase


class BaseTest(XmlTestCase):

    def setUp(self):
        from employee_directory_flask import app, db
        self.app = app
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.db = db
        self.client = self.app.test_client()
