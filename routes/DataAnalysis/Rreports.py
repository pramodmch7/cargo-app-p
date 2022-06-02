
import os
from flask import Blueprint, jsonify, request, current_app as app, make_response, send_from_directory
from werkzeug.utils import secure_filename
import json
import datetime
import uuid0 as ID
import jwt
from sqlalchemy import func, extract
from sqlalchemy.sql import text, select


from models.packageinfo import PackageinfoDetails
from models.branchinfo import BranchinfoDetails
from models.combine_br_pk_info import COMBINE_BR_PK_INFO
from codes.packageinfodicGen import Convert, Convert_Format
from codes.AuthToken import token_required

FReports = Blueprint('FReports', __name__)


@FReports.route('/api/getreport/<dates>', methods=['GET'])
@token_required
def getPIReports(current_user, dates):
    DBData = PackageinfoDetails.getAll()

    FDate = dates.split('~')[0]
    LDate = dates.split('~')[1]

    DBDateData = PackageinfoDetails.query.filter(
        PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)).all()

    DatesData = PackageinfoDetails.query.with_entities(

        func.count(PackageinfoDetails.HPkgLocationFrom),
        func.sum(PackageinfoDetails.HPkgTransportingCharges +
                 PackageinfoDetails.HPkgLoadingCharges),
        func.sum(PackageinfoDetails.HPkgAdvanceAmount),
        func.sum(PackageinfoDetails.HPkgBalanceAmount)
    ).filter(PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)).all()

    BranchBrekupData = PackageinfoDetails.query.with_entities(
        PackageinfoDetails.HPkgLocationFrom,
        func.count(PackageinfoDetails.HPkgLocationFrom),
        func.sum(PackageinfoDetails.HPkgTransportingCharges +
                 PackageinfoDetails.HPkgLoadingCharges),
        func.sum(PackageinfoDetails.HPkgAdvanceAmount),
        func.sum(PackageinfoDetails.HPkgBalanceAmount),
        # PackageinfoDetails.HPkgLocationTo,
    ).filter(PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)
             ).group_by(PackageinfoDetails.HPkgLocationFrom).all()

    BranchBrekupDataTo = PackageinfoDetails.query.with_entities(
        PackageinfoDetails.HPkgLocationFrom,
        func.count(PackageinfoDetails.HPkgLocationFrom),
        func.sum(PackageinfoDetails.HPkgTransportingCharges +
                 PackageinfoDetails.HPkgLoadingCharges),
        func.sum(PackageinfoDetails.HPkgAdvanceAmount),
        func.sum(PackageinfoDetails.HPkgBalanceAmount),
        PackageinfoDetails.HPkgLocationTo,
        # PackageinfoDetails.HPkgAllStatus,
    ).filter(PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)
             ).group_by(PackageinfoDetails.HPkgLocationFrom
                        ).group_by(PackageinfoDetails.HPkgLocationTo
                                   ).all()

    Data = {
        'HHUDates': f"{FDate} to {LDate}",
        'HHUData': [
            {
                'HHUCount': '',
                'HHUTA': '',
                'HHUAA': '',
                'HHUBA': '',
            },
            [],
            []
        ],
        'HHUDataB': {'DataBF': [], 'DataBT': [], 'DataBE': []},

    }
    for index, _data in enumerate(DatesData):
        Data['HHUData'][0]['HHUCount'] = _data[0]
        Data['HHUData'][0]['HHUTA'] = _data[1]
        Data['HHUData'][0]['HHUAA'] = _data[2]
        Data['HHUData'][0]['HHUBA'] = _data[3]

    for index, _Bdata in enumerate(BranchBrekupData):
        # print(_Bdata)
        DataJ = {}
        DataJ['slno'] = index+1
        DataJ['LF'] = _Bdata[0]
        DataJ['CO'] = _Bdata[1]
        DataJ['TA'] = _Bdata[2]
        DataJ['AA'] = _Bdata[3]
        DataJ['BA'] = _Bdata[4]
        DataJ['LTD'] = []
        Data['HHUDataB']['DataBF'].append(DataJ)

    for i, j in enumerate(Data['HHUDataB']['DataBF']):
        for k, l in enumerate(BranchBrekupDataTo):
            if j['LF'] == l[0]:
                # print(l[5])
                DataK = {}
                DataK['slno'] = k+1
                DataK['LF'] = l[0]
                DataK['CO'] = l[1]
                DataK['TA'] = l[2]
                DataK['AA'] = l[3]
                DataK['BA'] = l[4]
                DataK['LT'] = l[5]
                Data['HHUDataB']['DataBF'][i]['LTD'].append(DataK)

    data = []
    if len(DBDateData) > 0:
        for index, _data in enumerate(DBDateData):
            if current_user.HUsrAdmin == True:
                DatA = Convert(index, _data)

                data.append(DatA)
        Data['HHUData'][2] = data
        # print(Data['HHUDataB']['DataBF'][0]['LTD'])
    return{'message': Data, 'status': 200}

    return make_response(jsonify({'message': []}), 200)


@FReports.route('/api/getreportnew/<dates>', methods=['GET'])
@token_required
def getNewReports(current_user, dates):
    DBData = BranchinfoDetails.getAll()

    FDate = dates.split('~')[0]
    LDate = dates.split('~')[1]

    BranchData = BranchinfoDetails.query.with_entities(
        BranchinfoDetails.HBrBranchCode,
        BranchinfoDetails.HBrLocation,
        BranchinfoDetails.HBrName,
    ).group_by(BranchinfoDetails.HBrLocation)\
        .group_by(BranchinfoDetails.HBrName)\
        .group_by(BranchinfoDetails.HBrBranchCode)\
        .all()

    BranchDataDetailsSend = COMBINE_BR_PK_INFO.query.with_entities(
        COMBINE_BR_PK_INFO.idBranchF,
        func.count(COMBINE_BR_PK_INFO.idBranchF),
        func.sum(COMBINE_BR_PK_INFO.PackageAA),
    ).filter(COMBINE_BR_PK_INFO.PackageCD.between(FDate, LDate))\
        .group_by(COMBINE_BR_PK_INFO.idBranchF)\
        .all()

    BranchDataDetailsReceived = COMBINE_BR_PK_INFO.query.with_entities(
        COMBINE_BR_PK_INFO.idBranchT,
        func.count(COMBINE_BR_PK_INFO.idBranchT),
        func.sum(COMBINE_BR_PK_INFO.PackageBA),
        func.sum(COMBINE_BR_PK_INFO.PackageBAR),
    ).filter(COMBINE_BR_PK_INFO.PackageCD.between(FDate, LDate))\
        .group_by(COMBINE_BR_PK_INFO.idBranchT)\
        .all()

    # print(BranchData)
    # print(BranchDataDetailsSend)

    Data = {
        'HHUDates': f"{FDate} to {LDate}",
        'HHUDataBr': [],
        'HHUDataB': {'DataBF': [], 'DataBT': [], 'DataBE': []},
    }

    for index, BrData in enumerate(BranchData):
        _Br = {}
        _Br['brCode'] = BrData[0]
        _Br['brLocation'] = BrData[1]
        _Br['brName'] = BrData[2]
        _Br['brCountS'] = ''
        _Br['brCountR'] = ''
        _Br['brAmtG'] = ''
        _Br['brAmtYR'] = ''
        _Br['brAmtR'] = ''
        _Br['brPkgs'] = []
        Data['HHUDataBr'].append(_Br)
    # print(Data['HHUDataBr'])
    for i, j in enumerate(Data['HHUDataBr']):
        # print(j['brLocation'])
        for index, BranDataS in enumerate(BranchDataDetailsSend):
            if j['brLocation'] == BranchinfoDetails.getById(BranDataS[0]).HBrLocation:
                # print(i)
                Data['HHUDataBr'][i]['brCountS'] = BranDataS[1]
                Data['HHUDataBr'][i]['brAmtG'] = BranDataS[2]
            # print(
            #     f"{BranchinfoDetails.getById( BranDataS[0]).HBrLocation}-{BranDataS[1]}-{BranDataS[2]}")

        for index, BranDataF in enumerate(BranchDataDetailsReceived):
            if j['brLocation'] == BranchinfoDetails.getById(BranDataF[0]).HBrLocation:
                Data['HHUDataBr'][i]['brCountR'] = BranDataF[1]
                Data['HHUDataBr'][i]['brAmtYR'] = BranDataF[2]
                Data['HHUDataBr'][i]['brAmtR'] = BranDataF[3]
            # print(
            #     f"{BranchinfoDetails.getById( BranDataF[0]).HBrLocation}-{BranDataF[1]}-{BranDataF[2]}-{BranDataF[3]}")
    print(json.dumps(Data))
    return make_response(jsonify({'message': []}), 200)


'''
    DBDateData = PackageinfoDetails.query.filter(
        PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)).all()

    DatesData = PackageinfoDetails.query.with_entities(

        func.count(PackageinfoDetails.HPkgLocationFrom),
        func.sum(PackageinfoDetails.HPkgTransportingCharges +
                 PackageinfoDetails.HPkgLoadingCharges),
        func.sum(PackageinfoDetails.HPkgAdvanceAmount),
        func.sum(PackageinfoDetails.HPkgBalanceAmount)
    ).filter(PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)).all()

    BranchBrekupData = PackageinfoDetails.query.with_entities(
        PackageinfoDetails.HPkgLocationFrom,
        func.count(PackageinfoDetails.HPkgLocationFrom),
        func.sum(PackageinfoDetails.HPkgTransportingCharges +
                 PackageinfoDetails.HPkgLoadingCharges),
        func.sum(PackageinfoDetails.HPkgAdvanceAmount),
        func.sum(PackageinfoDetails.HPkgBalanceAmount),
        # PackageinfoDetails.HPkgLocationTo,
    ).filter(PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)
             ).group_by(PackageinfoDetails.HPkgLocationFrom).all()

    BranchBrekupDataTo = PackageinfoDetails.query.with_entities(
        PackageinfoDetails.HPkgLocationFrom,
        func.count(PackageinfoDetails.HPkgLocationFrom),
        func.sum(PackageinfoDetails.HPkgTransportingCharges +
                 PackageinfoDetails.HPkgLoadingCharges),
        func.sum(PackageinfoDetails.HPkgAdvanceAmount),
        func.sum(PackageinfoDetails.HPkgBalanceAmount),
        PackageinfoDetails.HPkgLocationTo,
        # PackageinfoDetails.HPkgAllStatus,
    ).filter(PackageinfoDetails.HPkgCreatedD.between(FDate, LDate)
             ).group_by(PackageinfoDetails.HPkgLocationFrom
                        ).group_by(PackageinfoDetails.HPkgLocationTo
                                   ).all()

    Data = {
        'HHUDates': f"{FDate} to {LDate}",
        'HHUData': [
            {
                'HHUCount': '',
                'HHUTA': '',
                'HHUAA': '',
                'HHUBA': '',
            },
            [],
            []
        ],
        'HHUDataB': {'DataBF': [], 'DataBT': [], 'DataBE': []},

    }
    for index, _data in enumerate(DatesData):
        Data['HHUData'][0]['HHUCount'] = _data[0]
        Data['HHUData'][0]['HHUTA'] = _data[1]
        Data['HHUData'][0]['HHUAA'] = _data[2]
        Data['HHUData'][0]['HHUBA'] = _data[3]

    for index, _Bdata in enumerate(BranchBrekupData):
        # print(_Bdata)
        DataJ = {}
        DataJ['slno'] = index+1
        DataJ['LF'] = _Bdata[0]
        DataJ['CO'] = _Bdata[1]
        DataJ['TA'] = _Bdata[2]
        DataJ['AA'] = _Bdata[3]
        DataJ['BA'] = _Bdata[4]
        DataJ['LTD'] = []
        Data['HHUDataB']['DataBF'].append(DataJ)

    for i, j in enumerate(Data['HHUDataB']['DataBF']):
        for k, l in enumerate(BranchBrekupDataTo):
            if j['LF'] == l[0]:
                # print(l[5])
                DataK = {}
                DataK['slno'] = k+1
                DataK['LF'] = l[0]
                DataK['CO'] = l[1]
                DataK['TA'] = l[2]
                DataK['AA'] = l[3]
                DataK['BA'] = l[4]
                DataK['LT'] = l[5]
                Data['HHUDataB']['DataBF'][i]['LTD'].append(DataK)

    data = []
    if len(DBDateData) > 0:
        for index, _data in enumerate(DBDateData):
            if current_user.HUsrAdmin == True:
                DatA = Convert(index, _data)

                data.append(DatA)
        Data['HHUData'][2] = data
        # print(Data['HHUDataB']['DataBF'][0]['LTD'])
    return{'message': Data, 'status': 200}
'''
