from db import db
import datetime


class BckTransportationinfoDetails(db.Model):
    __bind_key__ = 'bckkomitladb'
    __tablename__ = 'transportationinfo_table_bck'

    id1 = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String, unique=True)
    Spare1 = db.Column(db.Text())
    Spare2 = db.Column(db.Text())
    UpdatedD = db.Column(db.Date())
    UpdatedDT = db.Column(db.DateTime())
    UpdatedBy = db.Column(db.String(512))
    Deleted = db.Column(db.Boolean(), default=False)
    FDeleted = db.Column(db.Boolean(), default=False)
    HTrpTransportationName = db.Column(db.String(512), unique=False)
    HTrpBusNumber = db.Column(db.String(128), unique=False)
    HTrpCreatedD = db.Column(db.Date(), unique=False)
    HTrpCreatedDT = db.Column(db.DateTime(), unique=False)
    HTrpCreatedBy = db.Column(db.String(256), unique=False)

    def __init__(self, id, HTrpTransportationName,  HTrpCreatedD, HTrpCreatedDT, HTrpCreatedBy):
        self.id = id
        self.HTrpTransportationName = HTrpTransportationName
        self.HTrpCreatedD = HTrpCreatedD
        self.HTrpCreatedDT = HTrpCreatedDT
        self.HTrpCreatedBy = HTrpCreatedBy

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def getById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def getByTravelsName(cls, _TravelName):
        return cls.query.filter_by(HTrpTransportationName=_TravelName).first()

    def saveDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteDB(self):
        db.session.delete(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()
