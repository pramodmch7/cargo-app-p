def Convert(a, b):
    Data = {}
    Data['slno'] = a+1
    Data['id'] = b.id
    Data['hcustuniqueno'] = b.HcustUniqueNo
    Data['hcustname'] = b.HcustName
    Data['hcustphone'] = b.HcustPhone
    Data['hcustemail'] = b.HcustEmail
    Data['hcustlocation'] = b.HcustLocation
    return Data
