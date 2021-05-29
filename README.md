# Backend
### TODO
* Admin interface: 
    * show readonly fields

## Website
https://good-enough.herokuapp.com


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was prepared for HackOn 2.0 between the 28th May 2021 and 30th May 2021 in the subject of mental health.
Focusing on building self-confidence in the epidemics aftermath era, it uses the easy to use method to boost one's inner strength frequently used by therapist and coaches.
By adding their everyday achievements, user realizes how much they can appreciate themselves for on a daily basis.
This is an MVP exposing the API for user registration and login functionalities, as well as adding the achievements with the date and reading the latest achievements from the database. This is to be integrated with the Frontend also prepared for the same hackathon, which is based on angular js and bootstrap, but can also be easily integrable with other solutions and expended with further fanctionalities in the future.

## Functionalities in place:
* Registering a new user
* Login and logout
* Creating a new achievement
* Displaying list of user's achievements
* Delete user account

## Endpoints
* Register new user
    * auth/users/ 
    * method: POST
    * data: {'email': '[string]', 'password': '[string]'}
* Log In 
    * auth/token/login/
    * method: POST
    * data: {'email': '[string]', 'password': '[string]'}
    * response: {'auth_token': '[string]'}
* Log Out
    * auth/token/logout/
    * method: POST
    * headers: {Authorization: 'Token [string]'}
* Getting user details
    * auth/users/me/
    * method: GET
    * headers: {Authorization: 'Token [string]'}
    * response: {'uuid": '[stirng]', 'email': '[string]'
* Delete account
    * /auth/users/me
    * method: DELETE
    * headers: {Authorization: 'Token [string]'}
    * data: {'email': '[string]', 'password': '[string]'}
* Adding achievement
    * api/achievements/
    * method: POST
    * headers: {Authorization: 'Token [string]'}
    * data: {'content': '[string]'}
    


	
## Technologies
Project is created with:
* Python 3.6
* Django 3.2.3
* PostgreSQL

For further details see requirements.txt
	
## Setup
To run this project:
* clone the repository locally
* creaete virtual environement using Python 3.6.9
* install `requirements.txt`
* replace placeholders in `backend/example_settings.py` using your own creditentials.
* rename `backend/example_settings.py` to `backend/local_settings.py` 
* run `python manage.py migrate`
* run `python manage.py runserver`


