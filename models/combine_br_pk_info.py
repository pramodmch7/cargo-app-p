from db import db
import datetime

from models.branchinfo import *
from models.packageinfo import *


class COMBINE_BR_PK_INFO(db.Model):
    __tablename__ = 'combine_br_pk_info_table'
    id1 = db.Column(db.Integer, primary_key=True)
    idBranch = db.Column(db.String, db.ForeignKey('branchinfo_table.id'))
    idPackage = db.Column(db.String, db.ForeignKey('packageinfo_table.id'))
    idBranchF = db.Column(db.String(128))
    idBranchT = db.Column(db.String(128))
    PackageTA = db.Column(db.Float())
    PackageAA = db.Column(db.Float())
    PackageBA = db.Column(db.Float())
    PackageBAR = db.Column(db.Float())
    PackageLRNo = db.Column(db.String(64))
    PackageCD = db.Column(db.Date())
    PackageDD = db.Column(db.Date())
    Spare1 = db.Column(db.Text())
    Spare2 = db.Column(db.Text())
    Comments = db.Column(db.Text())
    BranchsRe = db.relationship(
        'BranchinfoDetails', backref=db.backref('branchinfodetailsa'))
    PackagesRe = db.relationship(
        'PackageinfoDetails', backref=db.backref('packageinfodetailsa'))

    def __init__(self, PackageLRNo, PackageTA, PackageAA, PackageBA, PackageBAR, PackageCD):
        self.PackageLRNo = PackageLRNo
        self.PackageTA = PackageTA
        self.PackageAA = PackageAA
        self.PackageBA = PackageBA
        self.PackageBAR = PackageBAR
        self.PackageCD = PackageCD

    @classmethod
    def getAll(cls):
        return cls.query.all()

    @classmethod
    def getByBranchFromId(cls, _Bid):
        return cls.query.filter_by(idBranchF=_Bid).all()

    @classmethod
    def getByBranchToId(cls, _Bid):
        return cls.query.filter_by(idBranchT=_Bid).all()

    @classmethod
    def getByPackageId(cls, _Pid):
        return cls.query.filter_by(idPackage=_Pid).first()

    @classmethod
    def getByLRNO(cls, _LRno):
        return cls.query.filter_by(PackageLRNo=_LRno).first()

    def saveDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteDB(self):
        db.session.delete(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()
