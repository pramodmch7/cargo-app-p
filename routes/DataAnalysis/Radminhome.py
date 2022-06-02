from dataclasses import dataclass
import os
from flask import Blueprint, jsonify, request, current_app as app, make_response, send_from_directory
from werkzeug.utils import secure_filename
import json
import datetime
import uuid0 as ID
import jwt


from models.bikeinfo import *
from models.proformainvoiceinfo import *
from models.customerinfo import *
from models.financeinfo import *
from codes.AuthToken import token_required

AdminHome = Blueprint('AdminHome', __name__)


@AdminHome.route('/api/gaaddata', methods=['GET'])
@token_required
def GetAll(current_user):
    DBData = ProformainvoiceinfoDetails.getAll()
    for index, _data in enumerate(DBData):
        if current_user.HUsrAdmin == True:
            data = []
            for index, _data in enumerate(DBData):
                CustomerData = CustomerinfoDetails.getById(
                    _data.HProinCustomerID)
                BikeData = BikeinfoDetails.getById(_data.HProinBikeID)
                Data = {}
                Data['slno'] = index+1
                Data['id'] = _data.id
                Data['finalPrice'] = _data.Spare1
                Data['hproinserialno'] = format(
                    int(_data.HProinSerialNo), '03d')
                Data['hproindate'] = _data.HProinDate
                Data['customerName'] = CustomerData.HCustName
                Data['customerPhone'] = CustomerData.HCustPhone
                Data['customerContactTime'] = CustomerData.HCustContactTime
                Data['bikeModel'] = BikeData.HBikModelName
                Data['pInvoiceDow'] = _data.HProinFileNameInvoice
                data.append(Data)
            return{'message': data, 'status': 200}
    return make_response(jsonify({'message': []}), 200)


@AdminHome.route('/api/gachartdata', methods=['GET'])
@token_required
def GetAllChart(current_user):
    # DBData = ProformainvoiceinfoDetails.getAllPIAsc('HProinCreatedD')
    # print(len(DBData))
    # for index, _data in enumerate(DBData):
    #     print('Yes Chart Data')
    #     print(_data.HProinCreatedD)
    DBCount = ProformainvoiceinfoDetails.getEnquiryCount()
    # print(DBCount)
    data = []
    for index, _data in enumerate(DBCount):
        data.append([_data[0], _data[1]])
    # print(data)
    # if current_user.HUsrAdmin == True:
    #     data = []
    #     for index, _data in enumerate(DBData):
    #         CustomerData = CustomerinfoDetails.getById(
    #             _data.HProinCustomerID)
    #         BikeData = BikeinfoDetails.getById(_data.HProinBikeID)
    #         Data = {}
    #         Data['slno'] = index+1
    #         Data['id'] = _data.id
    #         Data['finalPrice'] = _data.Spare1
    #         Data['hproinserialno'] = format(
    #             int(_data.HProinSerialNo), '03d')
    #         Data['hproindate'] = _data.HProinDate
    #         Data['customerName'] = CustomerData.HCustName
    #         Data['customerPhone'] = CustomerData.HCustPhone
    #         Data['customerContactTime'] = CustomerData.HCustContactTime
    #         Data['bikeModel'] = BikeData.HBikModelName
    #         Data['pInvoiceDow'] = _data.HProinFileNameInvoice
    #         data.append(Data)
    # return{'message': ['data', 'dataa'], 'status': 200}
    return make_response(jsonify({'message': data}), 200)


@AdminHome.route('/api/gachartbkdata', methods=['GET'])
@token_required
def GetBikeChart(current_user):
    # DBData = ProformainvoiceinfoDetails.getAllPIAsc('HProinCreatedD')
    # print(len(DBData))
    # for index, _data in enumerate(DBData):
    #     print('Yes Chart Data')
    #     print(_data.HProinCreatedD)
    DBCount = ProformainvoiceinfoDetails.getBikeCount()
    # print(DBCount)
    data = []
    for index, _data in enumerate(DBCount):
        BikeName = BikeinfoDetails.getById(_data[0])
        data.append([BikeName.HBikModelName, _data[1]])
    # print(data)
    # if current_user.HUsrAdmin == True:
    #     data = []
    #     for index, _data in enumerate(DBData):
    #         CustomerData = CustomerinfoDetails.getById(
    #             _data.HProinCustomerID)
    #         BikeData = BikeinfoDetails.getById(_data.HProinBikeID)
    #         Data = {}
    #         Data['slno'] = index+1
    #         Data['id'] = _data.id
    #         Data['finalPrice'] = _data.Spare1
    #         Data['hproinserialno'] = format(
    #             int(_data.HProinSerialNo), '03d')
    #         Data['hproindate'] = _data.HProinDate
    #         Data['customerName'] = CustomerData.HCustName
    #         Data['customerPhone'] = CustomerData.HCustPhone
    #         Data['customerContactTime'] = CustomerData.HCustContactTime
    #         Data['bikeModel'] = BikeData.HBikModelName
    #         Data['pInvoiceDow'] = _data.HProinFileNameInvoice
    #         data.append(Data)
    # return{'message': ['data', 'dataa'], 'status': 200}
    return make_response(jsonify({'message': data}), 200)
