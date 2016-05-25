from .base import BaseTest
from employee_directory_flask import parser
import json


class ParserTest(BaseTest):

    def test_model_from_json_string(self):
        data = [{"fullName": "Spider-Man",
                 "imageUrl": "http://example.com/526548a343e4b.jpg",
                 "email": "Spider-Man@heroes.example.com",
                 "phoneNumber": "+14155559610"}]
        employees = parser.parse(json.dumps(data))

        self.assertEquals(len(data), len(employees))
        self.assertEquals(employees[0].full_name, data[0]["fullName"])
        self.assertEquals(employees[0].image_url, data[0]["imageUrl"])
        self.assertEquals(employees[0].email, data[0]["email"])
        self.assertEquals(employees[0].phone_number, data[0]["phoneNumber"])
