def Convert(a, b):
    Data = {}
    Data['slno'] = a+1
    Data['id'] = b.id
    Data['hbruniqueno'] = b.HBrUniqueNo
    Data['hbrname'] = b.HBrName
    Data['hbrlocation'] = b.HBrLocation
    Data['hbrbranchcode'] = b.HBrBranchCode
    Data['hbraddress'] = b.HBrAddress
    Data['hbrphone'] = b.HBrPhone
    Data['hbrlatitude'] = b.HBrLatitude
    Data['hbrlongitude'] = b.HBrLongitude
    Data['hbrauthorizeduser'] = b.HBrAuthorizedUser
    Data['hbrauthorizedusername'] = b.HBrAuthorizedUserName
    Data['hbrcreatedd'] = b.HBrCreatedD
    Data['hbrcreateddt'] = b.HBrCreatedDT
    return Data
