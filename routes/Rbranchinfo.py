from flask import Blueprint, jsonify, request, current_app as app, make_response
import json
import datetime
import uuid0 as ID
import jwt

from models.branchinfo import *
from models1.bckbranchinfo import BckBranchinfoDetails
from codes.branchinfodicGen import *
from models.userdetailsn import UserdetailsnDetails
from codes.AuthToken import token_required

BranchinfoRoute = Blueprint('BranchinfoRoute', __name__)


@BranchinfoRoute.route('/api/gabr', methods=['GET'])
@token_required
def getBranchs(current_user):
    DBData = BranchinfoDetails.getAll()
    data = []
    for index, _data in enumerate(DBData):
        Data = Convert(index, _data)
        data.append(Data)
    return{'message': data, 'status': 200}


@BranchinfoRoute.route('/api/anbr', methods=['POST'])
@token_required
def addBranch(current_user):
    data = request.get_json()
    Id = str(ID.generate())

    if current_user.HUsrAdmin == True:
        Branchs = len(BranchinfoDetails.getAll())
        CheckBranch = BranchinfoDetails.getByBranchName(data['hbrname'])
        if not CheckBranch:
            Id = str(ID.generate())
            BrachCodeGen = f'BRAN{Branchs + 1}'
            Latitude = 0
            Longitude = 0
            Authorised_User_Name = ''

            if data['hbrlatitude'] != "":
                Latitude = data['hbrlatitude']

            if data['hbrlongitude'] != "":
                Latitude = data['hbrlongitude']

            if data['hbrauthorizeduser'] != '':
                BranchSelectedUser = UserdetailsnDetails.getByEmail(
                    data['hbrauthorizeduser'])
                Authorised_User_Name = f'{BranchSelectedUser.HUsrFirstName} {BranchSelectedUser.HUsrLastName}'

            NewData = BranchinfoDetails(id=Id,
                                        HBrUniqueNo=BrachCodeGen,
                                        HBrName=data['hbrname'],
                                        HBrLocation=data['hbrlocation'],
                                        HBrBranchCode=data['hbrbranchcode'],
                                        HBrAddress=data['hbraddress'],
                                        HBrPhone=data['hbrphone'],
                                        HBrLatitude=Latitude,
                                        HBrLongitude=Longitude,
                                        HBrAuthorizedUser=data['hbrauthorizeduser'],
                                        HBrAuthorizedUserName=Authorised_User_Name,
                                        HBrCreatedD=datetime.datetime.today().date(),
                                        HBrCreatedDT=datetime.datetime.today(),
                                        HBrCreatedBy=current_user.HUsrEmail
                                        )
            BranchinfoDetails.saveDB(NewData)
            # BckBranchinfoDetails.saveDB(NewData)
            NewData1 = BckBranchinfoDetails(id=Id,
                                            HBrUniqueNo=BrachCodeGen,
                                            HBrName=data['hbrname'],
                                            HBrLocation=data['hbrlocation'],
                                            HBrBranchCode=data['hbrbranchcode'],
                                            HBrAddress=data['hbraddress'],
                                            HBrPhone=data['hbrphone'],
                                            HBrLatitude=Latitude,
                                            HBrLongitude=Longitude,
                                            HBrAuthorizedUser=data['hbrauthorizeduser'],
                                            HBrAuthorizedUserName=Authorised_User_Name,
                                            HBrCreatedD=datetime.datetime.today().date(),
                                            HBrCreatedDT=datetime.datetime.today(),
                                            HBrCreatedBy=current_user.HUsrEmail
                                            )

            BckBranchinfoDetails.saveDB(NewData1)

            AUser = UserdetailsnDetails.getByEmail(data['hbrauthorizeduser'])

            if AUser:
                # print('Successfuly Got Search User Name Email form DB')
                AUser.HUsrLocation = data['hbrlocation']
                UserdetailsnDetails.updateDB(AUser)
            return{'status': 200, 'message': 'New Branch Created', 'code': f'Created'}
        else:
            return{'status': 202, 'message': 'Branch is Already Exists', 'code': f'Exists'}
    return{'status': 401, 'message': 'You Are Not Admin', 'code': f'Unauthorize'}


@BranchinfoRoute.route('/api/edbr/<id>', methods=['PUT'])
@token_required
def updateBranch(current_user, id):
    data = request.get_json()
    DBData = BranchinfoDetails.getById(id)
    DBData1 = BranchinfoDetails.getById(id)
    if DBData:
        Latitude = 0
        Longitude = 0

        if data['hbrlatitude'] != 0 or data['hbrlatitude'] != "":
            Latitude = data['hbrlatitude']

        if data['hbrlongitude'] != 0 or data['hbrlongitude'] != "":
            Longitude = data['hbrlongitude']

        if data['hbrauthorizeduser'] != '':
            BranchSelectedUser = UserdetailsnDetails.getByEmail(
                data['hbrauthorizeduser'])
            Authorised_User_Name = f'{BranchSelectedUser.HUsrFirstName} {BranchSelectedUser.HUsrLastName}'

        DBData.HBrName = data['hbrname']
        DBData.HBrLocation = data['hbrlocation']
        DBData.HBrBranchCode = data['hbrbranchcode']
        DBData.HBrAddress = data['hbraddress']
        DBData.HBrPhone = data['hbrphone']
        DBData.HBrLatitude = Latitude
        DBData.HBrLongitude = Longitude
        DBData.HBrAuthorizedUser = data['hbrauthorizeduser']
        DBData.HBrAuthorizedUserName = Authorised_User_Name
        DBData.UpdatedD = datetime.datetime.today().date()
        DBData.UpdatedDT = datetime.datetime.today()
        DBData.UpdatedBy = current_user.HUsrEmail

        BranchinfoDetails.updateDB(BranchinfoDetails)

        DBData1.HBrName = data['hbrname']
        DBData1.HBrLocation = data['hbrlocation']
        DBData1.HBrBranchCode = data['hbrbranchcode']
        DBData1.HBrAddress = data['hbraddress']
        DBData1.HBrPhone = data['hbrphone']
        DBData1.HBrLatitude = Latitude
        DBData1.HBrLongitude = Longitude
        DBData1.HBrAuthorizedUser = data['hbrauthorizeduser']
        DBData1.HBrAuthorizedUserName = Authorised_User_Name
        DBData1.UpdatedD = datetime.datetime.today().date()
        DBData1.UpdatedDT = datetime.datetime.today()
        DBData1.UpdatedBy = current_user.HUsrEmail

        BckBranchinfoDetails.updateDB(BckBranchinfoDetails)

        AUser = UserdetailsnDetails.getByEmail(data['hbrauthorizeduser'])

        if AUser:
            # print('Successfuly Got Search User Name Email form DB')
            AUser.HUsrLocation = data['hbrlocation']
            UserdetailsnDetails.updateDB(AUser)
        return{'status': 200, 'message': 'Branch Updated', 'code': f'Updated'}
    return{'status': 200, 'message': 'Something Went Wrong', 'code': f'Error'}


@BranchinfoRoute.route('/api/dbr/<id>', methods=['PUT'])
@token_required
def dissableBranch(current_user, id):
    data = request.get_json()
    DBData = BranchinfoDetails.getById(id)
    DBData1 = BranchinfoDetails.getById(id)
    if DBData:
        DBData.Deleted = True
        DBData.UpdatedD = datetime.datetime.today().date()
        DBData.UpdatedDT = datetime.datetime.today()
        DBData.UpdatedBy = current_user.HUsrEmail

        BranchinfoDetails.updateDB(BranchinfoDetails)

        DBData1.Deleted = True
        DBData1.UpdatedD = datetime.datetime.today().date()
        DBData1.UpdatedDT = datetime.datetime.today()
        DBData1.UpdatedBy = current_user.HUsrEmail

        BckBranchinfoDetails.updateDB(BckBranchinfoDetails)

        return{'status': 200, 'message': 'Branch Dissabled', 'code': f'Dissable'}
    return{'status': 200, 'message': 'Something Went Wrong', 'code': f'Error'}
