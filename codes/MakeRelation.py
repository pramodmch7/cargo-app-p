from models.combine_br_pk_info import COMBINE_BR_PK_INFO
from models1.bckcombine_br_pk_info import BckCOMBINE_BR_PK_INFO
from models.packageinfo import PackageinfoDetails
from models1.bckpackageinfo import BckPackageinfoDetails
from models.branchinfo import BranchinfoDetails


def Make_Relations(Pid, Comm):

    CreatedPackage = PackageinfoDetails.getById(Pid)

    if CreatedPackage:

        BFid = BranchinfoDetails.getByLocation(
            CreatedPackage.HPkgLocationFrom).id
        BTid = BranchinfoDetails.getByLocation(
            CreatedPackage.HPkgLocationTo).id

        PLR = CreatedPackage.HPkgLRNo
        TA = float(CreatedPackage.HPkgTransportingCharges) + \
            float(CreatedPackage.HPkgLoadingCharges)

        AA = float(CreatedPackage.HPkgAdvanceAmount)
        BA = TA - AA
        BAR = CreatedPackage.HPkgBalAmtReceived
        CD = CreatedPackage.HPkgCreatedD

        New_Combine = COMBINE_BR_PK_INFO(
            PackageLRNo=PLR,
            PackageTA=TA,
            PackageAA=AA,
            PackageBA=BA,
            PackageBAR=BAR,
            PackageCD=CD
        )

        New_Combine.idBranch = BFid
        New_Combine.idBranchF = BFid
        New_Combine.idBranchT = BTid
        New_Combine.idPackage = Pid
        New_Combine.Comments = Comm

        COMBINE_BR_PK_INFO.saveDB(New_Combine)

        New_Combine1 = BckCOMBINE_BR_PK_INFO(
            PackageLRNo=PLR,
            PackageTA=TA,
            PackageAA=AA,
            PackageBA=BA,
            PackageBAR=BAR,
            PackageCD=CD
        )

        New_Combine1.idBranch = BFid
        New_Combine1.idBranchF = BFid
        New_Combine1.idBranchT = BTid
        New_Combine1.idPackage = Pid
        New_Combine1.Comments = Comm

        BckCOMBINE_BR_PK_INFO.saveDB(New_Combine1)


def Make_Relations_Update(Pid, Comm):

    SelectPackage = COMBINE_BR_PK_INFO.getByPackageId(Pid)
    SelectPackage1 = BckCOMBINE_BR_PK_INFO.getByPackageId(Pid)
    CreatedPackage = PackageinfoDetails.getById(Pid)

    if SelectPackage:
        if CreatedPackage:
            BFid = BranchinfoDetails.getByLocation(
                CreatedPackage.HPkgLocationFrom).id
            BTid = BranchinfoDetails.getByLocation(
                CreatedPackage.HPkgLocationTo).id

            PLR = CreatedPackage.HPkgLRNo
            TA = float(CreatedPackage.HPkgTransportingCharges) + \
                float(CreatedPackage.HPkgLoadingCharges)
            AA = float(CreatedPackage.HPkgAdvanceAmount)
            BA = TA - AA
            BAR = CreatedPackage.HPkgBalAmtReceived
            CD = CreatedPackage.HPkgUpdatedD

            SelectPackage.PackageLRNo = PLR
            SelectPackage.PackageTA = TA
            SelectPackage.PackageAA = AA
            SelectPackage.PackageBA = BA
            SelectPackage.PackageBAR = BAR
            SelectPackage.PackageCD = CD
            SelectPackage.idBranch = BFid
            SelectPackage.idBranchF = BFid
            SelectPackage.idBranchT = BTid
            SelectPackage.idPackage = Pid
            SelectPackage.Comments = Comm

            COMBINE_BR_PK_INFO.updateDB(COMBINE_BR_PK_INFO)

            SelectPackage1.PackageLRNo = PLR
            SelectPackage1.PackageTA = TA
            SelectPackage1.PackageAA = AA
            SelectPackage1.PackageBA = BA
            SelectPackage1.PackageBAR = BAR
            SelectPackage1.PackageCD = CD
            SelectPackage1.idBranch = BFid
            SelectPackage1.idBranchF = BFid
            SelectPackage1.idBranchT = BTid
            SelectPackage1.idPackage = Pid
            SelectPackage1.Comments = Comm

            BckCOMBINE_BR_PK_INFO.updateDB(BckCOMBINE_BR_PK_INFO)


def Make_Relations_Dlvr(Pid, Comm):

    SelectPackage = COMBINE_BR_PK_INFO.getByPackageId(Pid)
    SelectPackage1 = BckCOMBINE_BR_PK_INFO.getByPackageId(Pid)
    PackageDetails = PackageinfoDetails.getById(Pid)

    if SelectPackage:
        if PackageDetails:
            BA = PackageDetails.HPkgBalanceAmount
            BAR = PackageDetails.HPkgBalAmtReceived
            DD = PackageDetails.HPkgDeliveryD

            SelectPackage.PackageBA = BA
            SelectPackage.PackageBAR = BAR
            SelectPackage.PackageCD = DD
            SelectPackage.Comments = Comm

            COMBINE_BR_PK_INFO.updateDB(COMBINE_BR_PK_INFO)

            SelectPackage1.PackageBA = BA
            SelectPackage1.PackageBAR = BAR
            SelectPackage1.PackageCD = DD
            SelectPackage1.Comments = Comm

            BckCOMBINE_BR_PK_INFO.updateDB(BckCOMBINE_BR_PK_INFO)
