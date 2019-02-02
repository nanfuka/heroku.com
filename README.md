[![Build Status](https://travis-ci.com/nanfuka/heroku.com.svg?branch=login)](https://travis-ci.com/nanfuka/heroku.com)[![Maintainability](https://api.codeclimate.com/v1/badges/8134adf8a1711f0bc673/maintainability)](https://codeclimate.com/github/nanfuka/heroku.com/maintainability)[![Coverage Status](https://coveralls.io/repos/github/nanfuka/heroku.com/badge.svg?branch=login)](https://coveralls.io/github/nanfuka/heroku.com?branch=login)

ireporter_api
Description
iReporter is an application that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention. It was developed because corruption is a huge bane to Africa's development.

Getting Started
Follow these instructions to get a copy of the API to run on your machine.

Prerequisites
Install the following programs before using the API:

1. Python version 3.7.1
2. Postman
Instructions for set up
Clone into this repo using:
git clone https://github.com/reifred/i_reporter_3.git
Set up a virtual environment for python in the project directory
Inorder to set up the virtual environment, you need to install the python package called virtualenv using pip. Run the command below to install it.

pip install virtualenv to install virtualenv
virtualenv virtual to create a virtual environment named virtual
virtual/Scripts/activate to activate your virtual environment.
virtual/Scripts/deactivate to deactivate your virtual environment.
Install the required packages using:
After setting up and activating your virtual environment, you need to install all the packages required by the project.

pip install -r requirements.txt
Setting Up environment variables
For windows using command prompt

Database
set URI='postgres://db_user_name:db_password@db_host/database_name'
Secret Key
set SECRET_KEY="your_secret_key"
For Linux using bash

Database
export URI='postgres://db_user_name:db_password@db_host/database_name'
Secret Key
export SECRET_KEY="your_secret_key"
