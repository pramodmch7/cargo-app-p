from datetime import datetime


def Convert(a, b):
    Status = b.HPkgAllStatus.split('|')[-2]
    Data = {}
    Data["slno"] = a+1
    Data['id'] = b.id
    Data['hpkglrno'] = b.HPkgLRNo
    Data['hpkgfragile'] = b.HPkgFragile
    Data['hpkgcustomerfromname'] = b.HPkgCustomerFromName
    Data['hpkglocationfrom'] = b.HPkgLocationFrom
    Data['hpkgphonefrom'] = b.HPkgPhoneFrom
    Data['hpkgcustomertoname'] = b.HPkgCustomerToName
    Data['hpkglocationto'] = b.HPkgLocationTo
    Data['hpkgphoneto'] = b.HPkgPhoneTo
    Data['hpkgarticlescount'] = b.HPkgArticlesCount
    Data['hpkgweight'] = f'{int(b.HPkgWeight)/1000} kg'
    Data['hpkgtransportingcharges'] = b.HPkgTransportingCharges
    Data['hpkgloadingcharges'] = b.HPkgLoadingCharges
    Data['hpkgapproximatedeliverydate'] = str(b.HPkgApproximateDeliveryDate)
    Data['hpkgadvanceamount'] = b.HPkgAdvanceAmount
    Data['hpkgbalanceamount'] = b.HPkgBalanceAmount
    Data['hpkgstatusfrom'] = b.HPkgStatusFrom
    Data['hpkgstatuscodefrom'] = b.HPkgStatusCodeFrom
    Data['hpkgallstatus'] = b.HPkgAllStatus
    Data['hpkgqrcode'] = b.HPkgQrCode
    Data['hpkgcreatedd'] = str(b.HPkgCreatedD)
    Data['hpkgcreateddt'] = str(b.HPkgCreatedDT)
    Data['hpkgcreatedby'] = b.HPkgCreatedBy
    Data['currentstatus'] = Status.split('~')[1]
    # print(b.HPkgAllStatus.split('|')[-2])
    # print(b.HPkgCreatedD)
    return Data


def Convert_Format(c, d):
    Data = {}
    Data["slno"] = c+1
    Data['id'] = d.id
    Data['lrno'] = d.HPkgLRNo
    Data['PN'] = d.HPkgName

    Data['PDIST'] = d.HPkgDistance
    Data['PW'] = d.HPkgWeight

    #Data['PDD'] = d.HPkgActualDeliveryDate

    Data['PC'] = d.HPkgQrCode

    Data['PSF'] = d.HPkgStatusFrom
    Data['PSFC'] = d.HPkgStatusCodeFrom
    Data['PDISD'] = d.HPkgDispatchD

    Data['PST'] = d.HPkgStatusTo
    Data['PSTC'] = d.HPkgStatusCodeTo
    Data['PAD'] = d.HPkgArrivingD

    Data["PkgDates"] = {'Dheading': 'Date:', 'Dvalue': str(datetime.fromisoformat(str(d.HPkgCreatedD)).date()),
                        'ADheading': 'Delivery Date:', 'ADvalue': str(datetime.fromisoformat(str(d.HPkgApproximateDeliveryDate)).date())
                        }
    Data['PkgcustomerF'] = {'Location': d.HPkgLocationFrom,
                            'Name': d.HPkgCustomerFromName,
                            'Phone': d.HPkgPhoneFrom
                            }
    Data['PkgcustomerT'] = {'Location': d.HPkgLocationTo,
                            'Name': d.HPkgCustomerToName,
                            'Phone': d.HPkgPhoneTo
                            }

    Data['Pkgfragil'] = d.HPkgFragile
    Data['hpkgarticlescount'] = d.HPkgArticlesCount
    Data['hpkgtransportingcharges'] = d.HPkgTransportingCharges
    Data['hpkgloadingcharges'] = d.HPkgLoadingCharges
    Data['hpkgadvanceamount'] = d.HPkgAdvanceAmount

    Data['pkgfilamt'] = {'TAheading': 'Total:',
                         'TAvalue': float(d.HPkgTransportingCharges) + float(d.HPkgLoadingCharges),
                         'APheading': 'Advance:',
                         'APvalue': d.HPkgAdvanceAmount,
                         'BAheading': 'Balance:',
                         'BAvalue': d.HPkgBalanceAmount,
                         'FAheading': 'Final Amount:',
                         'FAvalue': float(d.HPkgTransportingCharges) + float(d.HPkgLoadingCharges),
                         }

    return Data
