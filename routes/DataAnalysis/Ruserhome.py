import os
from flask import Blueprint, jsonify, request, current_app as app, make_response, send_from_directory
from werkzeug.utils import secure_filename
import json
import datetime
import uuid0 as ID
import jwt


from models.packageinfo import *
from codes.AuthToken import token_required

UserHome = Blueprint('UserHome', __name__)


@UserHome.route('/api/gauhdata', methods=['GET'])
@token_required
def GetAll(current_user):
    DBData = PackageinfoDetails.getAll()
    data = {
        'UHtoday': [{'SData':                   {
            'HHUDay': 'Today',
            'HHUDate': datetime.datetime.today().date(),
        }}, {'DData': []}],
        'UHyesterday': [{'SData':                   {
                        'HHUDay': 'Yesterday',
                        'HHUDate': (datetime.datetime.today() - datetime.timedelta(days=1)).date(),
                        }}, {'DData': []}],
        'UHall': [{'SData':                   {
            'HHUDay': 'All',
            'HHUDate': '',
        }}, {'DData': []}]
    }
    for index, _data in enumerate(DBData):
        if _data.HPkgCreatedBy == current_user.HUsrEmail or _data.HPkgUpdatedBy == current_user.HUsrEmail:
            _count = 0
            if _data.HPkgCreatedD == datetime.datetime.today().date():
                _count += 1
                data['UHtoday'][0]['SData']['HHUDay'] = 'Today'
                # data['UHtoday'][0]['SData']['HHUDate'] = datetime.datetime.today().date()

                data['UHtoday'][1]['DData'].append(
                    {
                        'slno': index+1,
                        'HHUCount': _count,
                        'lrno': _data.HPkgLRNo,
                        'PN': _data.HPkgName,
                        'HHUCustomerName': _data.HPkgCustomerFromName,
                        'HHUCustomerPhone': _data.HPkgPhoneFrom,
                        'HHUCustomerToName': _data.HPkgCustomerToName,
                        'HHUCustomerToPhone': _data.HPkgPhoneTo,
                        'HHUCustomerToLocation': _data.HPkgLocationTo,
                        'HHUStatus': _data.HPkgAllStatus,
                        'HHUBalanceAmt': (_data.HPkgTransportingCharges + _data.HPkgLoadingCharges) - (_data.HPkgAdvanceAmount + _data.HPkgBalAmtReceived),
                        'Pkgfragil': _data.HPkgFragile,
                    }
                )
            elif _data.HPkgCreatedD == (datetime.datetime.today() - datetime.timedelta(days=1)).date():
                _count += 1
                data['UHyesterday'][0]['SData']['HHUDay'] = 'Yesterday'
                # data['UHyesterday'][0]['SData']['HHUDate'] = ''

                data['UHyesterday'][1]['DData'].append(
                    {
                        'slno': index+1,
                        'HHUCount': _count,
                        'lrno': _data.HPkgLRNo,
                        'PN': _data.HPkgName,
                        'HHUCustomerName': _data.HPkgCustomerFromName,
                        'HHUCustomerPhone': _data.HPkgPhoneFrom,
                        'HHUCustomerToName': _data.HPkgCustomerToName,
                        'HHUCustomerToPhone': _data.HPkgPhoneTo,
                        'HHUCustomerToLocation': _data.HPkgLocationTo,
                        'HHUStatus': _data.HPkgAllStatus,
                        'HHUBalanceAmt': (_data.HPkgTransportingCharges + _data.HPkgLoadingCharges) - (_data.HPkgAdvanceAmount + _data.HPkgBalAmtReceived),
                        'Pkgfragil': _data.HPkgFragile,
                    }
                )
            else:
                _count += 1
                data['UHall'][0]['SData']['HHUDay'] = 'All'
                # data['UHall'][0]['SData']['HHUDate'] = _data.HProinCreatedD

                data['UHall'][1]['DData'].append(
                    {
                        'slno': index+1,
                        'HHUCount': _count,
                        'lrno': _data.HPkgLRNo,
                        'PN': _data.HPkgName,
                        'HHUCustomerName': _data.HPkgCustomerFromName,
                        'HHUCustomerPhone': _data.HPkgPhoneFrom,
                        'HHUCustomerToName': _data.HPkgCustomerToName,
                        'HHUCustomerToPhone': _data.HPkgPhoneTo,
                        'HHUCustomerToLocation': _data.HPkgLocationTo,
                        'HHUStatus': _data.HPkgAllStatus,
                        'HHUBalanceAmt': (_data.HPkgTransportingCharges + _data.HPkgLoadingCharges) - (_data.HPkgAdvanceAmount + _data.HPkgBalAmtReceived),
                        'Pkgfragil': _data.HPkgFragile,
                    }
                )
                # print(_data.HProinCustomerID)
            # data.append(_data)
    return{'message': data, 'status': 200}
    # return "make_response(jsonify({'BikData': data}), 200)"


"""
@UserHome.route('/api/gabdata/<id>', methods=['GET'])
@token_required
def GetBikeByName(current_user, id):
    DBData = BikeinfoDetails.getById(id)
    data = []
    for index, _data in enumerate([DBData]):
        Data = Convert(index, _data)
        data.append(Data)
    return{'message': data, 'status': 200}


@UserHome.route('/api/gbb/<id>', methods=['GET'])
@token_required
def GetBrochure(current_user, id):
    print(id)

    pdfFileName = id

    filePath = app.config['upload_path']

    # dirname = os.path.join(os.path.dirname(
    #     os.path.abspath(__name__)), filePath)

    filename = os.path.join(
        filePath, f'{filePath}\\{pdfFileName}')

    print(filename)

    Response = send_from_directory(
        directory=filePath, path=pdfFileName, as_attachment=True)
    Response.headers['FileName'] = pdfFileName
    return Response


@UserHome.route('/api/abdata', methods=['POST'])
@token_required
def AddNewData(current_user):
    data = request.get_json()
    Id = str(ID.generate())
    UNumber = f'Bike{len(BikeinfoDetails.getAll())+1}'

    Model = data['hbikmodelname'].split('|')[0]
    Variant = data['hbikmodelname'].split('|')[1]

    NewData = BikeinfoDetails(
        id=Id,
        HBikUniqueNo=UNumber,
        HBikModelName=data['hbikmodelname'],
        HBikModel=Model,
        HBikVariant=Variant,
        HBikPrice=data['hbikprice'],
        HBikInsurance=data['hbikinsurance'],
        HBikPDICharges=data['hbikpdicharges'],
        HBikRoadTax=data['hbikroadtax'],
        HBikGoodLife=data['hbikgoodlife'],
        HBikOnRoadPrice=data['hbikonroadprice'],
        HBikStdAccessories=data['hbikstdaccessories'],
        HBikOptAccessories=data['hbikoptaccessories'],
        HBikNetPrice=data['hbiknetprice'],
        HBikColor=data['hbikcolor'],
        HBikCreatedD=datetime.today().date(),
        HBikCreatedDT=datetime.today(),
        HBikCreatedBy=current_user.HUsrEmail,
    )
    BikeinfoDetails.saveDB(NewData)
    return{'status': 200, 'message': ['New Bike Added', Id], 'code': f'Created'}


@UserHome.route('/api/abb/<id>', methods=['POST'])
@token_required
def AddBrochure(current_user, id):
    print(id)
    try:
        if request.method == 'POST':
            Bfile = request.files['brochureFile']
            if not Bfile.filename.rsplit('.', 1)[1].upper() in AllowedExtentation:
                return{'status': 300, 'message': 'Please Upload Only "PDF" file.', 'code': f'Invalid Extention'}
            Bfile.save(os.path.join(
                app.config['upload_path'], secure_filename(id)))
            DBData = BikeinfoDetails.getById(id)
            if DBData:
                DBData.HBikBrochureLink = secure_filename(id)
                BikeinfoDetails.updateDB(BikeinfoDetails)
    except:
        return{'status': 404, 'message': 'Brochure File Not Uploaded', 'code': f'Brochure Fail'}
    return{'status': 200, 'message': 'Brochure Added', 'code': f'Brochure'}


@UserHome.route('/api/ubdata/<id>', methods=['PUT'])
@token_required
def UpdateData(current_user, id):
    data = request.get_json()
    DBData = BikeinfoDetails.getById(id)
    if DBData:
        Model = data['hbikmodelname'].split('|')[0]
        Variant = data['hbikmodelname'].split('|')[1]

        DBData.HBikModelName = data['hbikmodelname']
        DBData.HBikModel = Model
        DBData.HBikVariant = Variant
        DBData.HBikPrice = data['hbikprice']
        DBData.HBikInsurance = data['hbikinsurance']
        DBData.HBikPDICharges = data['hbikpdicharges']
        DBData.HBikRoadTax = data['hbikroadtax']
        DBData.HBikGoodLife = data['hbikgoodlife']
        DBData.HBikOnRoadPrice = data['hbikonroadprice']
        DBData.HBikStdAccessories = data['hbikstdaccessories']
        DBData.HBikOptAccessories = data['hbikoptaccessories']
        DBData.HBikNetPrice = data['hbiknetprice']
        DBData.HBikColor = data['hbikcolor']
        DBData.UpdatedD = datetime.datetime.today().date()
        DBData.UpdatedDT = datetime.datetime.today()
        DBData.UpdatedBy = current_user.HUsrEmail
        BikeinfoDetails.updateDB(BikeinfoDetails)
    return{'status': 200, 'message': ['Bike Details Updated', id], 'code': f'Update'}


@UserHome.route('/api/ubaccdata/<id>', methods=['PUT'])
@token_required
def UpdateAcc(current_user, id):
    data = request.get_json()
    DBData = BikeinfoDetails.getById(id)
    if DBData:
        DBData.HBikAccessoriesList = json.dumps(data['hbikaccessories'])
        BikeinfoDetails.updateDB(BikeinfoDetails)
    return{'status': 200, 'message': 'AccessoriesList Added', 'code': f'Acc Added'}


@UserHome.route('/api/dbaccdata/<id>', methods=['PUT'])
@token_required
def DissableBike(current_user, id):
    data = request.get_json()
    DBData = BikeinfoDetails.getById(id)
    if DBData:
        DBData.Deleted = True
        BikeinfoDetails.updateDB(BikeinfoDetails)
    return{'status': 200, 'message': 'AccessoriesList Added', 'code': f'Acc Added'}
"""
