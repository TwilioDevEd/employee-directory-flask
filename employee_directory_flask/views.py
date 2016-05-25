from flask import render_template, request
from . import app
from twilio import twiml
from .models import Employee


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/directory/search', methods=['POST'])
def search():
    response = twiml.Response()
    NOT_FOUND_MESSAGE = "We did not find the employee you're looking for"
    name = request.form['Body']
    employees = list(Employee.query.filter(Employee.full_name.contains(name)))
    if len(employees) == 1:
        employee = employees[0]
        employee_data = '\n'.join([employee.full_name,
                                   employee.phone_number,
                                   employee.email])
        with response.message(employee_data) as message:
            message.media(employee.image_url)
    elif len(employees) > 1:
        message = ["We found multiple people, reply with:"]
        names = [employee.full_name for employee in employees]
        for i, name in enumerate(names, 1):
            message.append("%s for %s" % (i, name))
        message.append("Or start over")
        response.message('\n'.join(message))
    else:
        response.message(NOT_FOUND_MESSAGE)
    return str(response)
