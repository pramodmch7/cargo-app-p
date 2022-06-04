from email.policy import default
from db import db
import datetime


class BckPackageinfoDetails(db.Model):
    __bind_key__ = 'bckkomitladb'
    __tablename__ = 'packageinfo_table_bck'

    id1 = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String, unique=True)
    Spare1 = db.Column(db.Text())
    Spare2 = db.Column(db.Text())
    UpdatedD = db.Column(db.Date())
    UpdatedDT = db.Column(db.DateTime())
    UpdatedBy = db.Column(db.String(512))
    Deleted = db.Column(db.Boolean(), default=False)
    FDeleted = db.Column(db.Boolean(), default=False)
    HPkgLRNo = db.Column(db.String(32), unique=True)
    HPkgName = db.Column(db.String(256), unique=False)
    HPkgFragile = db.Column(db.Boolean(), default=False)
    HPkgVehicleDetails = db.Column(db.String(128), unique=False)
    HPkgTravelsDetails = db.Column(db.String(128), unique=False)
    HPkgCustomerFromName = db.Column(db.String(256), unique=False)
    HPkgLocationFrom = db.Column(db.String(128), unique=False)
    HPkgPhoneFrom = db.Column(db.String(32), unique=False)
    HPkgCustomerToName = db.Column(db.String(256), unique=False)
    HPkgLocationTo = db.Column(db.String(128), unique=False)
    HPkgPhoneTo = db.Column(db.String(32), unique=False)
    HPkgArticlesCount = db.Column(db.String(128), unique=False)
    HPkgWeight = db.Column(db.String(64), unique=False)
    HPkgTransportingCharges = db.Column(db.Float(), default=0, unique=False)
    HPkgLoadingCharges = db.Column(db.Float(), default=0, unique=False)
    HPkgApproximateDeliveryDate = db.Column(db.Date(), unique=False)
    HPkgAdvanceAmount = db.Column(db.Float(), default=0, unique=False)
    HPkgBalanceAmount = db.Column(db.Float(), default=0, unique=False)
    HPkgBalanceAmountReceived = db.Column(db.Float(), default=0, unique=False)
    HPkgBalAmtReceived = db.Column(db.Float(), default=0, unique=False)
    HPkgStatusFrom = db.Column(db.String(512), unique=False)
    HPkgStatusCodeFrom = db.Column(db.String(128), unique=False)
    HPkgStatusTo = db.Column(db.String(512), unique=False)
    HPkgStatusCodeTo = db.Column(db.String(128), unique=False)
    HPkgAllStatus = db.Column(db.Text(), unique=False)
    HPkgDistance = db.Column(db.String(64), unique=False)
    HPkgQrCode = db.Column(db.Text(), unique=False)
    HPkgLogPath = db.Column(db.Text(), unique=False)
    HPkgCreatedD = db.Column(db.Date(), unique=False)
    HPkgCreatedDT = db.Column(db.DateTime(), unique=False)
    HPkgCreatedBy = db.Column(db.String(256), unique=False)
    HPkgDispatchD = db.Column(db.Date(), unique=False)
    HPkgDispatchDT = db.Column(db.DateTime(), unique=False)
    HPkgDispatchBy = db.Column(db.String(256), unique=False)
    HPkgArrivingD = db.Column(db.Date(), unique=False)
    HPkgArrivingDT = db.Column(db.DateTime(), unique=False)
    HPkgArrivingBy = db.Column(db.String(256), unique=False)
    HPkgDeliveryD = db.Column(db.Date(), unique=False)
    HPkgDeliveryDT = db.Column(db.DateTime(), unique=False)
    HPkgDeliveredBy = db.Column(db.String(256), unique=False)
    HPkgUpdatedD = db.Column(db.Date(), unique=False)
    HPkgUpdatedDT = db.Column(db.DateTime(), unique=False)
    HPkgUpdatedBy = db.Column(db.String(256), unique=False)
    HPkgDeleted = db.Column(db.Boolean(), unique=False)
    HPkgForceDeleted = db.Column(db.Boolean(), unique=False)
    HPkgSlipName = db.Column(db.String(128), unique=False)

    def __init__(
        self,
        id,
        HPkgLRNo,
        HPkgFragile,
        HPkgWeight,
        HPkgCustomerFromName,
        HPkgLocationFrom,
        HPkgPhoneFrom,
        HPkgCustomerToName,
        HPkgLocationTo,
        HPkgPhoneTo,
        HPkgArticlesCount,
        HPkgTransportingCharges,
        HPkgLoadingCharges,
        HPkgApproximateDeliveryDate,
        HPkgAdvanceAmount,
        HPkgBalanceAmount,
        HPkgStatusFrom,
        HPkgStatusCodeFrom,
        HPkgAllStatus,
        HPkgQrCode,
        HPkgCreatedD,
        HPkgCreatedDT,
        HPkgCreatedBy,
        HPkgSlipName
    ):
        self.id = id
        self.HPkgLRNo = HPkgLRNo
        self.HPkgFragile = HPkgFragile
        self.HPkgWeight = HPkgWeight
        self.HPkgCustomerFromName = HPkgCustomerFromName
        self.HPkgLocationFrom = HPkgLocationFrom
        self.HPkgPhoneFrom = HPkgPhoneFrom
        self.HPkgCustomerToName = HPkgCustomerToName
        self.HPkgLocationTo = HPkgLocationTo
        self.HPkgPhoneTo = HPkgPhoneTo
        self.HPkgArticlesCount = HPkgArticlesCount
        self.HPkgTransportingCharges = HPkgTransportingCharges
        self.HPkgLoadingCharges = HPkgLoadingCharges
        self.HPkgApproximateDeliveryDate = HPkgApproximateDeliveryDate
        self.HPkgAdvanceAmount = HPkgAdvanceAmount
        self.HPkgBalanceAmount = HPkgBalanceAmount
        self.HPkgStatusFrom = HPkgStatusFrom
        self.HPkgStatusCodeFrom = HPkgStatusCodeFrom
        self.HPkgAllStatus = HPkgAllStatus
        self.HPkgQrCode = HPkgQrCode
        self.HPkgCreatedD = HPkgCreatedD
        self.HPkgCreatedDT = HPkgCreatedDT
        self.HPkgCreatedBy = HPkgCreatedBy
        self.HPkgSlipName = HPkgSlipName

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def getById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def getByPkgName(cls, _PackageName):
        return cls.query.filter_by(HPkgName=_PackageName).first()

    @classmethod
    # Get Specific Package with Based on Status Code
    def getStatusCodeP(cls, _status):
        return cls.query.filter_by(HPkgStatusCodeFrom=_status)

    @classmethod
    # Get Specific Package with Based on Status Code
    def getbyBranch(cls, _Branch):
        return cls.query.filter_by(HPkgLocationFrom=_Branch).all()

    @classmethod
    def getByDates(cls, fdate, ldate):
        return cls.query.filter(cls.HPkgCreatedD.between(fdate, ldate)).all()

    @classmethod
    def getBranchGroups(cls, fdate, ldate):
        return cls.query.filter(cls.HPkgCreatedD.between(fdate, ldate)).group_by(cls.HPkgLocationFrom).all()

    # @classmethod
    # def getBikeCount(cls):
    #     return cls.query.with_entities(cls.HProinBikeID, func.count(cls.HProinBikeID)).group_by(cls.HProinBikeID).all()

    def saveDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteDB(self):
        db.session.delete(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()
