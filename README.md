# Leaderboard Project


## Setup and run

1. Create a virtual environment with Python3.7: `virtualenv env -p python3.7`. If you dont have `python3.7` yet then you can install it with:
    1. linux(ubuntu/debian) - `sudo apt install python3.7`
    1. windows - Download installer from https://www.python.org/downloads/release/python-370/.
1. Activate the virutal environment: `source env/bin/activate`
1. Install all the dependencies in `requirements.txt` file: `pip install -r requirements.txt`
1. Migrate the migrations: `python manage.py migrate`
1. [See below for webhooks setup](#webhooks-setup).
1. Run the app: `python manage.py runserver`
1. To test the APIs in your local, we can use ngrok [See below for ngrok setup](#ngrok-setup).
1. Navigate to http://localhost:8000/docs/ for the swagger UI documentation in your browser.
1. When you are done using the app, deactivate the virtual environment: `deactivate`


## Ngrok Setup

1. Install [ngrok](https://ngrok.com/download) 
1. When you're done installing, you can expose your localhost by running `./ngrok http 8000` .
1. Copy that funky `*.ngrok.io` URL. That's your server public URL for now.

![Screenshot from 2020-06-23 22-28-50](https://user-images.githubusercontent.com/49693160/85433398-04517c80-b5a2-11ea-81ae-a7db3cef22e7.png)


## Webhooks Setup

We recommend you go through [Webhooks Docs](https://developer.github.com/webhooks/) to be able to use this project effeciently.

![Screenshot from 2020-06-23 22-09-56](https://user-images.githubusercontent.com/49693160/85433388-0287b900-b5a2-11ea-86f3-04d92b8c4d20.png)


1. Select any repo and head over to https://github.com/:owner/:repo/settings/hooks/new
1. Create a webhook with payload URL (ngrok or real server) with `/pull_request/` appended to it.
1. Set the content type as `application/json`. No secrets for now.
1. Select the individual event called "Pull Requests". Let the webhook be `Active`.
1. Make another similar webhook with payload URL `/issue/` appended to it, and select the event "issues".
1. Also create a new Leaderboard object in the admin panel or Python shell with the, username same as the github username you are making your PRs with. 
