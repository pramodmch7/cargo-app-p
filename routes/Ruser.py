from flask import Blueprint, jsonify, request, current_app as app, make_response
import json
import datetime
import uuid0 as ID
import jwt
from werkzeug.security import check_password_hash as Hcph


from models.userdetailsn import *
from codes.AuthToken import token_required

UserRoute = Blueprint('UserRoute', __name__)


@UserRoute.route('/api/login', methods=['POST'])
def Login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Please enter valid email and password', 'status': 401})

    user = UserdetailsnDetails.getByEmail(auth.username.lower())

    if not user:
        return jsonify({'message': 'Please enter valid email', 'status': 501})

    if user.HUsrActive == False:
        return jsonify({'message': 'Please enter valid email', 'status': 501})

    elif Hcph(user.HUsrPassword, auth.password):
        token = jwt.encode({'public_id': user.id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=610)}, app.config['SECRET_KEY'])
        # token = jwt.encode({'public_id': user.id, 'exp': datetime.datetime.utcnow(
        # ) + datetime.timedelta(seconds=5)}, app.config['SECRET_KEY'])

        if user.HUsrAdmin == True:
            return jsonify({'token': token, 'roles': [1001, 1002], 'user': user.HUsrEmail})
        else:
            return jsonify({'token': token, 'roles': [1002], 'user': user.HUsrEmail})

    return jsonify({'message': 'Could not verify. Please try again', 'status': 601})
