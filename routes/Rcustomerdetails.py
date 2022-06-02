from flask import Blueprint, jsonify, request, current_app as app, make_response
import uuid0 as ID
import jwt
import datetime
from functools import wraps
from datetime import datetime

from models.customerdetails import *
from codes.AuthToken import token_required
from codes.customerinfodicGen import Convert


CustomerRoute = Blueprint('CustomerRoute', __name__)


@CustomerRoute.route('/api/gacu', methods=['GET'])
@token_required
def getCustomers(current_user):
    Customers = CustomerDetails.getAllCustomer()

    data = []
    for index, customer in enumerate(Customers):
        if current_user.HUsrAdmin == True or current_user.HUsrAdmin == False:
            Data = Convert(index, customer)
            data.append(Data)
        # else:
        #     return{'message': 'You Are Not Admin', 'status': 200}

    return{'message': data, 'status': 200}
