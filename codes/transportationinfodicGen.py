def Convert(a, b):
    Data = {}
    Data['id'] = b.id
    Data['slno'] = a+1
    Data['htrptransportationname'] = b.HTrpTransportationName
    Data['htrpbusnumber'] = b.HTrpBusNumber
    Data['htrpcreatedd'] = b.HTrpCreatedD
    Data['htrpcreateddt'] = b.HTrpCreatedDT
    Data['htrpcreatedby'] = b.HTrpCreatedBy
    return Data
