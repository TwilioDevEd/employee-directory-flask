<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# SMS/MMS Employee Directory on ASP.NET MVC

[![Build Status](https://travis-ci.org/TwilioDevEd/employee-directory-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/employee-directory-flask)

Use Twilio to accept SMS messages and turn them into queries against a SQL database. This example functions as an Employee Directory where a mobile phone user can send a text message with a partial string of the person's name and it will return their picture and contact information (Email address and Phone number).

[Tutorial soon]()

## Local Development

This project is built using [Flask](http://flask.pocoo.org/) web framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/sms2fa-flask.git
   $ cd sms2fa-flask
   ```

1. Create a new virtual environment.
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```bash
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```bash
        mkvirtualenv automated-survey
        ```

1. Install the dependencies.

    ```bash
    pip install -r requirements.txt
    ```


1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your
   [Twilio Account Settings](https://www.twilio.com/user/account/settings).
   You will also need a `TWILIO_NUMBER`, which you may find [here](https://www.twilio.com/user/account/phone-numbers/incoming).

   Run `source .env` to export the environment variables.

1. Run the migrations.

    Our app uses SQLite, so you probably will not need to install additional software.

    ```bash
    python manage.py db upgrade
    ```

1. Make sure the tests succeed.

    ```bash
    $ coverage run manage.py test
    ```

1. Start the server.

    ```bash
    python manage.py runserver
    ```
    
1. Check it out at: [http://localhost:5000/](http://localhost:5000/).

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
