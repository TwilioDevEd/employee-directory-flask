from flask import render_template
from . import app
from twilio import twiml


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/directory/search', methods=['POST'])
def search():
    NOT_FOUND_MESSAGE = "We did not find the employee you're looking for"
    response = twiml.Response()
    response.message(NOT_FOUND_MESSAGE)
    return str(response)
