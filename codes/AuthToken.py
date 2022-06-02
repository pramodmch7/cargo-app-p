from flask import jsonify, request, current_app as app
from functools import wraps
import jwt

from models.userdetailsn import UserdetailsnDetails


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            # print(token)
            # print('I am Before Decode data')
            # print(app.config['SECRET_KEY'])
            # try:
            #     data = jwt.decode(
            #         token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # except:
            #     return jsonify({'message': 'Token got expired!'}), 402

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # print('I am From Try')
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = UserdetailsnDetails.query.filter_by(
                id=data['public_id']).first()
            # print(current_user.HUerem)

        except:

            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
