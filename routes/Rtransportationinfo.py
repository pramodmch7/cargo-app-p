from flask import Blueprint, jsonify, request, current_app as app, make_response
import json
import datetime
import uuid0 as ID
import jwt

from models.transportationinfo import *
from codes.transportationinfodicGen import *
from codes.AuthToken import token_required

TransportationinfoRoute = Blueprint('TransportationinfoRoute', __name__)


@TransportationinfoRoute.route('/api/gatravdata', methods=['GET'])
@token_required
def GetAllTravel(current_user):
    DBData = TransportationinfoDetails.getAll()
    data = []
    for index, _data in enumerate(DBData):
        Data = Convert(index, _data)
        data.append(Data)
    return{'message': data, 'status': 200}


@TransportationinfoRoute.route('/api/atravdata', methods=['POST'])
@token_required
def AddTravelData(current_user):
    data = request.get_json()
    Id = str(ID.generate())
    NewData = TransportationinfoDetails(id=Id,
                                        HTrpTransportationName=data['htrptransportationname'],
                                        HTrpCreatedD=datetime.datetime.today().date(),
                                        HTrpCreatedDT=datetime.datetime.today(),
                                        HTrpCreatedBy=current_user.HUsrEmail
                                        )
    TransportationinfoDetails.saveDB(NewData)
    return{'status': 200, 'message': 'New Travel Added', 'code': f'Created'}


@TransportationinfoRoute.route('/api/utravdata/<id>', methods=['PUT'])
@token_required
def UpdateTravels(current_user, id):
    data = request.get_json()
    DBData = TransportationinfoDetails.getById(id)
    if DBData:
        DBData.HTrpTransportationName = data['htrptransportationname']
        DBData.UpdatedD = datetime.datetime.today().date()
        DBData.UpdatedDT = datetime.datetime.today()
        DBData.UpdatedBy = current_user.HUsrEmail
        TransportationinfoDetails.updateDB(TransportationinfoDetails)
    return{'status': 200, 'message': 'Travel Updated', 'code': f'Update'}
