from flask import render_template, request, session
from . import app
from twilio import twiml
from .models import Employee
NOT_FOUND_MESSAGE = "We did not find the employee you're looking for"


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/directory/search', methods=['POST'])
def search():
    name = request.form['Body']
    employees = list(Employee.query.filter(Employee.full_name.contains(name)))
    if len(employees) == 1:
        return _send_single_result(employees)
    elif len(employees) > 1:
        names = [employee.full_name for employee in employees]
        session['choices'] = names
        return _send_multiple_results(names)
    return _send_not_found()


def _send_not_found():
    response = twiml.Response()
    response.message(NOT_FOUND_MESSAGE)
    return str(response)


def _send_single_result(employees):
    response = twiml.Response()
    employee = employees[0]
    employee_data = '\n'.join([employee.full_name,
                               employee.phone_number,
                               employee.email])
    with response.message(employee_data) as message:
        message.media(employee.image_url)
    return str(response)


def _send_multiple_results(names):
    response = twiml.Response()
    message = ["We found multiple people, reply with:"]
    for i, name in enumerate(names, 1):
        message.append("%s for %s" % (i, name))
    message.append("Or start over")
    response.message('\n'.join(message))
    return str(response)
