from xmlunittest import XmlTestCase

from employee_directory_flask import app, db, parser


class BaseTest(XmlTestCase):
    def setUp(self):
        self.client = app.test_client()
        db.create_all()
        self._seed_db()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @staticmethod
    def _seed_db():
        json_data = open('employees.json').read()
        employees = parser.parse(json_data)
        for employee in employees:
            db.session.add(employee)
        db.session.commit()
