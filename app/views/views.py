from flask import Flask, jsonify, request, json
# from app.controllers.user_controllers import User_controller
# from app.controllers.incident_controllers import Incidence
# from app.validators import Validators
# import jwt
# import datetime
# from flasgger import Swagger, swag_from
from app.helpers.db import Database
from app.models.user import User
# from app.control lers.token import *


app = Flask(__name__)
# validators = Validators()
# user_controller = User_controller()
# incidence = Incidence()
db = Database()
user = User()


@app.route('/')
# @user_controller.user_ttoken
# @swag_from('../apidocs/index.yml')
def index():
    """index url"""
    
    return jsonify({"status": 200, "message": "hi welcome to the ireporter testing"})


@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    """A user can signup by entering all the required data"""
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')

    db.add_user(firstname, lastname)
    return jsonify({"status": 200, "message": "you have successfully signed up"})
    

    # invalid_user_input = validators.validate_strings(
    #     firstname, lastname, othernames, username, data)
    # if invalid_user_input:
    #     return jsonify({"status": 400, 'error': invalid_user_input}), 400
    # invalid_email = validators.validate_email(email)
    # if invalid_email:
    #     return jsonify({"status": 400, 'error': invalid_email}), 400
    # invalid_type = validators.validat_numbers(phoneNumber)
    # if invalid_type:
    #     return jsonify({"status": 400, 'error': invalid_type}), 400
    # validate_boolean = validators.validate_boolean(isAdmin)
    # if validate_boolean:
    #     return jsonify({"status": 400, 'error': validate_boolean}), 400
    # validate_password = validators.validate_password(password)
    # if validate_password:
    #     return jsonify({"status": 400, 'error': validate_password}), 400

    # invalid_detail = user_controller.check_repitition(
    #     username, email, password)
    # if invalid_detail:
    #     return jsonify({"status": 400, 'error': invalid_detail}), 400
    # else:
    #     new = user_controller.create_user(
    #         firstname,
    #         lastname,
    #         othernames,
    #         email,
    #         phoneNumber,
    #         username,
    #         isAdmin,
    #         password)

    #     loggedin_admin = user_controller.admins_login(data['isAdmin'])
    #     if loggedin_admin:
    #         # admin_token = encode_token("username":username, "user":data['isAdmin'])
    #         # print(admin_token)

    #         return jsonify({"status": 201, "data": [{"user": new,"message": "you have successfully logged in as a adminstrator"}]})
    #     if not loggedin_admin:
    #         user_token = jwt.encode({'username': data['username'],
    #                             'exp': datetime.datetime.utcnow(
    #         ) + datetime.timedelta(minutes=30)}, 'amauser') 
    #         return jsonify({"status": 201, "data": [{"user": new,"message": "you have successfully signedup in as a user"}]})