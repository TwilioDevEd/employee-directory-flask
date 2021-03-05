<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# SMS/MMS Employee Directory on Python/Flask

![](https://github.com/TwilioDevEd/employee-directory-flask/workflows/Flask/badge.svg)

Use Twilio to accept SMS messages and turn them into queries against a SQL database. These are example functions where you get information from an Employee Directory through the request of an SMS. A mobile phone user can send a text message with a partial string of the person's name and it will return their picture and contact information (Email address and Phone number).

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/employee-directory/python/flask)!

## Local Development

This project is built using [Flask](http://flask.pocoo.org/) web framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/employee-directory-flask.git
   $ cd employee-directory-flask
   ```

1. Create and activate a new python3 virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. Install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

1. Copy the `.env.example` file to `.env`, and edit it to match your database.

1. Activate Flask development environment
   
   ```bash
   export FLASK_ENV=development
   ```

1. Run the migrations.

   Our app uses SQLite, so you probably will not need to install additional software.

   ```bash
   python manage.py db upgrade
   ```

1. Seed the database.

   ```bash
   python manage.py dbseed
   ```

   Seeding will load `employees.json` into SQLite.

1. Make sure the tests succeed.

    ```bash
    python manage.py test
    ```

1. Start the server.

    ```bash
    python manage.py runserver
    ```

1. Start ngrok.

   To actually forward incoming SMSs, your development server will need to be publicly accessible.
   [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).


   ```bash
   ngrok http 5000
   ```
   Once ngrok is running, it will look something like this: `http://9a159ccf.ngrok.io`

1. Configure Twilio to call your webhooks.

   You will also need to configure Twilio to call your application when calls are received
   on your _Twilio Number_. The **SMS & MMS Request URL** should look something like this:

   ```
   http://<sub-domain>.ngrok.io/directory/search
   ```

### How To Demo

1. Text your Twilio number the name "Iron"

1. Should get the following response:

   ```
   We found multiple people, reply with:
   1 for Iron Man
   2 for Iron Clad
   Or start over
   ```
1. Reply with 1

1. Should get the following response:

   ```
   Iron Man
   +14155559368
   +1-202-555-0143
   IronMan@heroes.example.com
   [the image goes here]
   ```


## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Lovingly crafted by Twilio Developer Education.
