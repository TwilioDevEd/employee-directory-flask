from flask import request, session
from . import app
from .models import Employee
from twilio.twiml.messaging_response import MessagingResponse, Message, Body, Media

NOT_FOUND_MESSAGE = "We did not find the employee you're looking for"


@app.route('/directory/search', methods=['POST'])
def search():
    query = request.form['Body']

    if _is_choice_answer(query):
        return _send_selected_employee(query)

    employees = list(Employee.query.filter(Employee.full_name.contains(query)))
    if len(employees) == 1:
        return _send_single_result(employees)
    elif len(employees) > 1:
        return _send_multiple_results(employees)
    else:
        return _send_not_found()


def _send_not_found():
    response = MessagingResponse()
    response.message(NOT_FOUND_MESSAGE)
    return str(response)


def _send_single_result(employees):
    response = MessagingResponse()
    employee = employees[0]
    message = Message()
    message.append(
        Body(f'{employee.full_name}\n{employee.phone_number}\n{employee.email}')
    )
    message.append(Media(employee.image_url))
    return str(response.append(message))


def _is_choice_answer(query):
    choices = session.get('choices', [])
    if query.isdigit():
        query = int(query)
        return (query - 1) in range(len(choices))
    return False


def _send_selected_employee(query):
    name = session['choices'][int(query) - 1]
    employees = Employee.query.filter_by(full_name=name)
    return _send_single_result(employees)


def _send_multiple_results(employees):
    names = [employee.full_name for employee in employees]
    session['choices'] = names
    response = MessagingResponse()
    message = ["We found multiple people, reply with:"]
    for i, name in enumerate(names, 1):
        message.append("%s for %s" % (i, name))
    message.append("Or start over")
    response.message('\n'.join(message))
    return str(response)
