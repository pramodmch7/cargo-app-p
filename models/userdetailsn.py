from db import db
import datetime


class UserdetailsnDetails(db.Model):
    __tablename__ = 'userdetailsn_table'

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
    HUsrUniqueNo = db.Column(db.String(256), unique=True)
    HUsrFirstName = db.Column(db.String(256), unique=False)
    HUsrLastName = db.Column(db.String(256), unique=False)
    HUsrMiddleName = db.Column(db.String(256), unique=False)
    HUsrPhone = db.Column(db.String(128), unique=False)
    HUsrAddress = db.Column(db.Text(), unique=False)
    HUsrEmail = db.Column(db.String(256), unique=True)
    HUsrPassword = db.Column(db.String(256), unique=False)
    HUsrAdmin = db.Column(db.Boolean(), unique=False, default=False)
    HUsrActive = db.Column(db.Boolean(), unique=False, default=False)
    HUsrRoleId = db.Column(db.Integer(), unique=False)
    HUsrRoleName = db.Column(db.String(128), unique=False)
    HUsrAvatar = db.Column(db.Text(), unique=False)
    HUsrLocation = db.Column(db.String(512), unique=False)
    HUsrCreatedD = db.Column(db.Date(), unique=False)
    HUsrCreatedDT = db.Column(db.DateTime(), unique=False)
    HUsrLogPath = db.Column(db.Text(), unique=False)
    HUsrDeleted = db.Column(db.Boolean(), unique=False, default=False)
    HUsrFDeleted = db.Column(db.Boolean(), unique=False, default=False)

    def __init__(
        self,
        id,
        HUsrUniqueNo,
        HUsrFirstName,
        HUsrLastName,
        HUsrPhone,
        HUsrAddress,
        HUsrEmail,
        HUsrPassword,
        HUsrAdmin,
        HUsrActive,
        HUsrRoleId,
        HUsrRoleName,
        HUsrAvatar,
        HUsrCreatedD,
        HUsrCreatedDT
    ):
        self.id = id
        self.HUsrUniqueNo = HUsrUniqueNo
        self.HUsrFirstName = HUsrFirstName
        self.HUsrLastName = HUsrLastName
        self.HUsrPhone = HUsrPhone
        self.HUsrAddress = HUsrAddress
        self.HUsrEmail = HUsrEmail
        self.HUsrPassword = HUsrPassword
        self.HUsrAdmin = HUsrAdmin
        self.HUsrActive = HUsrActive
        self.HUsrRoleId = HUsrRoleId
        self.HUsrRoleName = HUsrRoleName
        self.HUsrAvatar = HUsrAvatar
        self.HUsrCreatedD = HUsrCreatedD
        self.HUsrCreatedDT = HUsrCreatedDT

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def getAllAsc(cls, sortValue):
        return cls.query.order_by(sortValue).all()

    @classmethod
    def getAllDsc(cls):
        return cls.query.all()

    @classmethod
    def getById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def getByEmail(cls, _Email):
        return cls.query.filter_by(HUsrEmail=_Email).first()

    def saveDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteDB(self):
        db.session.delete(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()
