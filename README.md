<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# SMS/MMS Employee Directory on Python/Flask

[![Build Status](https://travis-ci.org/TwilioDevEd/employee-directory-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/employee-directory-flask)

Use Twilio to accept SMS messages and turn them into queries against a SQL database. This example functions as an Employee Directory where a mobile phone user can send a text message with a partial string of the person's name and it will return their picture and contact information (Email address and Phone number).

[Tutorial soon]()

## Local Development

This project is built using [Flask](http://flask.pocoo.org/) web framework.

1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/employee-directory-flask.git
   $ cd employee-directory-flask
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

1. Run the migrations.

   Our app uses SQLite, so you probably will not need to install additional software.

   ```bash
   python manage.py db upgrade
   ```

1. Seed the database:

   ```bash
   python manage.py dbseed
   ```

   Seeding will load `employees.json` into SQLite.

1. Make sure the tests succeed.

    ```bash
    $ coverage run manage.py test
    ```

1. Start the server.

    ```bash
    python manage.py runserver
    ```

1. Start ngrok
   
   To actually forward incoming SMSs, your development server will need to be publicly accessible.
   [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).


   ```bash
   $ ngrok http 5000
   ```
   Once ngrok is running, it will look something like this: `http://9a159ccf.ngrok.io`

1. Configure Twilio to call your webhooks

   You will also need to configure Twilio to call your application when calls are received
   on your _Twilio Number_. The **SMS & MMS Request URL** should look something like this:

   ```
   http://<sub-domain>.ngrok.io/directory/search
   ```

   ![Configure SMS](http://howtodocs.s3.amazonaws.com/twilio-number-config-all-med.gif)


### Expose the Application to the Wider Internet

Your application will need to be accessible from the internet, you can either
forward the necessary ports in your router, or use a tool like
[ngrok](https://ngrok.com/) that will expose your local host to the internet.

You can read [this blog post](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
for more details on how to use ngrok. If you are using version 2.x, exposing
a specific port should be easily done with the following command:

```bash
$ ngrok http 5000
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
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
