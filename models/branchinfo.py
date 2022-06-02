from db import db
import datetime


class BranchinfoDetails(db.Model):
    __tablename__ = 'branchinfo_table'

    id1 = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String, unique=True)
    Spare1 = db.Column(db.Text())
    Spare2 = db.Column(db.Text())
    Spare3 = db.Column(db.Text())
    Spare4 = db.Column(db.Text())
    Spare5 = db.Column(db.Text())
    Spare6 = db.Column(db.Text())
    Spare7 = db.Column(db.Text())
    UpdatedD = db.Column(db.Date())
    UpdatedDT = db.Column(db.DateTime())
    UpdatedBy = db.Column(db.String(512))
    Deleted = db.Column(db.Boolean(), default=False)
    FDeleted = db.Column(db.Boolean(), default=False)
    HBrUniqueNo = db.Column(db.String(64), unique=True)
    HBrName = db.Column(db.String(512), unique=False)
    HBrLocation = db.Column(db.String(256), unique=False)
    HBrBranchCode = db.Column(db.String(128), unique=False)
    HBrAddress = db.Column(db.Text(), unique=False)
    HBrPhone = db.Column(db.String(64), unique=True)
    HBrLatitude = db.Column(db.Float(), unique=False)
    HBrLongitude = db.Column(db.Float(), unique=False)
    HBrAuthorizedUser = db.Column(db.String(256), unique=False)
    HBrAuthorizedUserName = db.Column(db.String(256), unique=False)
    HBrCreatedD = db.Column(db.Date(), unique=False)
    HBrCreatedDT = db.Column(db.DateTime(), unique=False)
    HBrCreatedBy = db.Column(db.String(256), unique=False)
    HBrLogPath = db.Column(db.Text(), unique=False)
    HBrDeleted = db.Column(db.Boolean(), unique=False)
    HBrForceDeleted = db.Column(db.Boolean(), unique=False)

    def __init__(self, id, HBrUniqueNo, HBrName, HBrLocation, HBrBranchCode, HBrAddress, HBrPhone, HBrLatitude, HBrLongitude, HBrAuthorizedUser, HBrAuthorizedUserName, HBrCreatedD, HBrCreatedDT, HBrCreatedBy):
        self.id = id
        self.HBrUniqueNo = HBrUniqueNo
        self.HBrName = HBrName
        self.HBrLocation = HBrLocation
        self.HBrBranchCode = HBrBranchCode
        self.HBrAddress = HBrAddress
        self.HBrPhone = HBrPhone
        self.HBrLatitude = HBrLatitude
        self.HBrLongitude = HBrLongitude
        self.HBrAuthorizedUser = HBrAuthorizedUser
        self.HBrAuthorizedUserName = HBrAuthorizedUserName
        self.HBrCreatedD = HBrCreatedD
        self.HBrCreatedDT = HBrCreatedDT
        self.HBrCreatedBy = HBrCreatedBy

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def getById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def getByBranchName(cls, _Bname):
        return cls.query.filter_by(HBrName=_Bname).first()

    @classmethod
    def getByLocation(cls, _BLocation):
        return cls.query.filter_by(HBrLocation=_BLocation).first()

    def saveDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteDB(self):
        db.session.delete(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()
