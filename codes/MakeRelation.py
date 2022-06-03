from models.combine_br_pk_info import COMBINE_BR_PK_INFO
from models.packageinfo import PackageinfoDetails
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

        print(
            f"BFid={BFid}, BTid={BTid}, Pid={Pid}, PLR={PLR}, TA={TA}, AA={AA}, BA={BA}, Comm={Comm}")

        COMBINE_BR_PK_INFO.saveDB(New_Combine)


def Make_Relations_Update(Pid, Comm):

    SelectPackage = COMBINE_BR_PK_INFO.getByPackageId(Pid)
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
            print('TA')
            print(TA)
            print('TA')
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


def Make_Relations_Dlvr(Pid, Comm):

    SelectPackage = COMBINE_BR_PK_INFO.getByPackageId(Pid)
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
