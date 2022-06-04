from db import db
import datetime

from models1.bckbranchinfo import *
from models1.bckpackageinfo import *


class BckCOMBINE_BR_PK_INFO(db.Model):
    __bind_key__ = 'bckkomitladb'
    __tablename__ = 'combine_br_pk_info_table_bck'

    id1 = db.Column(db.Integer, primary_key=True)
    idBranch = db.Column(db.String, db.ForeignKey('branchinfo_table_bck.id'))
    idPackage = db.Column(db.String, db.ForeignKey('packageinfo_table_bck.id'))
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
        'BckBranchinfoDetails', backref=db.backref('branchinfodetailsa'))
    PackagesRe = db.relationship(
        'BckPackageinfoDetails', backref=db.backref('packageinfodetailsa'))

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
