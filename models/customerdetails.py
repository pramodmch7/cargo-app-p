from db import db
import datetime


class CustomerDetails(db.Model):
    __tablename__ = 'customer_details'
    id1 = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String, unique=True)

    HcustUniqueNo = db.Column(db.String(256), unique=True)
    HcustName = db.Column(db.String(256))
    HcustPhone = db.Column(db.String(256), unique=False)
    HcustEmail = db.Column(db.String(256), unique=False)
    HcustStatus = db.Column(db.String(512))
    HcustLocation = db.Column(db.String())
    HcustCreatedDate = db.Column(db.Date())
    HcustCreatedDateTime = db.Column(db.DateTime())
    HcustLogPath = db.Column(db.Text())
    HcustDeleted = db.Column(db.Boolean(), default=False)
    HcustForceDeleted = db.Column(db.Boolean(), default=False)
    HcustUpdatedDate = db.Column(db.Date())
    HcustUpdatedDate = db.Column(db.DateTime())
    HcustSpare1 = db.Column(db.Text())
    HcustSpare2 = db.Column(db.Text())

    def __init__(self, id, HcustUniqueNo, HcustName, HcustPhone, HcustStatus, HcustLocation, HcustCreatedDate,
                 HcustCreatedDateTime
                 ):

        self.id = id
        self.HcustUniqueNo = HcustUniqueNo
        self.HcustName = HcustName
        self.HcustPhone = HcustPhone
        self.HcustStatus = HcustStatus
        self.HcustLocation = HcustLocation
        self.HcustCreatedDate = HcustCreatedDate
        self.HcustCreatedDateTime = HcustCreatedDateTime

    @classmethod
    # Get All List of User
    def getAllCustomer(cls):
        return cls.query.all()

    @classmethod
    # Get Specific User with ID
    def getIdCustomer(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    # Get Specific User with Name
    def getNameCustomer(cls, _name):
        return cls.query.filter_by(HcustName=_name).first()

    @classmethod
    # Get Specific User with Email
    def getEmailCustomer(cls, _email):
        return cls.query.filter_by(HCerem=_email).first()

    @classmethod
    # Get Specific User with Email
    def getUniquenoCustomer(cls, _email):
        return cls.query.filter_by(HcustEmail=_email).first()

    def saveCustomer(self):
        db.session.add(self)
        db.session.commit()
        print('User Added to Clint DB')

    def deleteCustomer(self):
        db.session.delete(self)
        db.session.commit()
        print('User Deleted from Clint DB')

    def updateCustomer(self):
        db.session.commit()
        print('User update from Clint DB!')
