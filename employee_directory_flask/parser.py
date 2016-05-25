import json
from .models import Employee


def parse(json_string):
    employees_data = json.loads(json_string)
    employees = []
    for employee_data in employees_data:
        employee = Employee(email=employee_data["email"])
        employee.full_name = employee_data["fullName"]
        employee.image_url = employee_data["imageUrl"]
        employee.phone_number = employee_data["phoneNumber"]
        employees.append(employee)
    return employees
