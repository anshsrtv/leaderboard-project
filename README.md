# Leaderboard Project

## Setup and run

1. Create a virtual environment with Python3.7: `virtualenv env -p python3.7`. If you dont have `python3.7` yet then you can install it with:
    1. linux(ubuntu/debian) - `sudo apt install python3.7`
    1. windows - Download installer from https://www.python.org/downloads/release/python-370/.
1. Activate the virtual environment: `source env/bin/activate`
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

## Other Instructions
This repository has been created while keeping some good coding practices and situational advantages, and so the following needs to be kept in mind while working with it.

We keep track of merged PRs and total PRs made by each user. For scoring purposes we have divided the issues into three categories. These categories are identifies by adding labels to the issues.
1. Good first issue - These are simpler issues to get you started.
2. Medium issues - These are mildly challenging and worthwhile.
3. Hard issues - These are definitely meant to challenge you.

We understand that the contributing is itself of great importance. So we have decide to keep reward of all participants that solve atleast 2 medium issues and 1 good first issue. Those are tracked by `milestone_achieved`.

For every issue closed, we increment points. The following needs to be kept in mind in practice.
1. Every issue is assigned to one user only (This is important for proper points distribution and less confusion in the repository.)
2. Every issue is solved only by the user assigned to it. The person making the PR must ensure the s/he has been assigned the issue to make sure your contribution is counted.
3. Each issue shall contain only one of the labels described above.
4. Make sure the user is registered before the PR is made for proper updation, as updation is instant.
