import json


def pdfData(Udata, LrNo, AdvanceAmt, data):

    PDFdata = {
        'LRNoDate': [LrNo],
        'CName': ['Received From ', data['hpkgcustomerfromname']],
        'CPhone': ['Received From ', data['hpkgphonefrom']],
        'CLocation': ['Received From ', data['hpkglocationfrom']],

        'DName': ['Delivery To ', data['hpkgcustomertoname']],
        'DPhone': ['Delivery To ', data['hpkgphoneto']],
        'DLocation': ['Delivery To ', data['hpkglocationto']],

        'PName': ['Package Name ', ''],
        'PWeight': ['Weight ', float(data['hpkgweight'])/1000],
        'PArricle': ['No of Article ', data['hpkgarticlescount']],

        'TC': ['Transporting Charges ', float(data['hpkgtransportingcharges'])],
        'LC': ['Loading Charges ', float(data['hpkgloadingcharges'])],
        'TO': ['Total ', float(data['hpkgtransportingcharges']) + float(data['hpkgloadingcharges'])],
        'AP': ['Paid ', float(AdvanceAmt)],
        'TP': ['To Pay ', float(data['hpkgtransportingcharges']) + float(data['hpkgloadingcharges']) - float(AdvanceAmt)],
        'UD': ['Attended By: ', Udata.HUsrFirstName, 'Phone ', Udata.HUsrPhone]
    }

    return PDFdata
