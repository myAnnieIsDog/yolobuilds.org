from dataclasses import dataclass, field


@dataclass
class User():
    first: str
    last: str
    email: str
    group: str = ""
    review: bool = False
    inspect: bool = False
    admin: bool = False
    fiscal: bool = False


def new_user():
    def create() -> list:
        first = input("First Name:\n")
        last = input ("Last Name:\n")
        email = input("Email Address:\n")
        group = input("User Group:\n")
        review = input(f"Is {first} a Plan Reviewer?")
        inspect = input(f"Is {first} an Inspector?")
        admin = input(f"Will {first} make administrative changes?")
        fiscal = input(f"Does {first} work with fiscal reports?")
        return [first, last, email, group, review, inspect, admin, fiscal, f"{first[0]}{last}"]

    new = create()
    nickname = new.pop()
    with open(f"{nickname}.pickle", "wb") as f:
        new.dump(f)


### Building
AEspinoza = User(
    "Angelina", "Espinoza", 
    "angelina.espinoza@yolocounty.org",
    "Building",
    True, True, True, True)
AYepez = User(
    "Angelica", "Yepez", 
    "angelica.yepez@yolocounty.org",
    "Building",
    True, True, True, True)
CRice = User(
    "Chris", "Rice", 
    "chris.rice@yolocounty.org",
    "Building",
    True, True, True, True)
DKoranda = User(
    "Dawne", "Koranda", 
    "dawne.koranda@yolocounty.org",
    "Building",
    True, True, True, True)
MNardiello = User(
    "Marlin", "Nardiello", 
    "marlin.lee@yolocounty.org",
    "Building",
    True, True, True, True)
SuLee = User(
    "Su", "Lee", 
    "su.lee@yolocounty.org",
    "Building",
    True, True, True, True)
SCastagnola = User(
    "Stacey", "Castagnola", 
    "stacey.castagnola@yolocounty.org",
    "Building",
    True, True, True, True)
SDoolittle = User(
    "Scott", "Doolittle", 
    "scott.doolittle@yolocounty.org",
    "Building",
    True, True, True, True)
ToLee = User(
    "Touyer", "Lee", 
    "touyer.lee@yolocounty.org",
    "Building",
    True, True, True, True)
building = [
    AEspinoza,
    AYepez,
    CRice,
    DKoranda,
    MNardiello,
    SuLee,
    SCastagnola,
    SDoolittle,
    ToLee]


### Env Health
CMendoza = User(
    "Cassandra", "Mendoza", 
    "cassandra.mendoza@yolocounty.org",
    "Env. Health",
    True, True, True, True,
)
JHuang = User(
    "Jianmin", "Huang", 
    "jianmin.huang@yolocounty.org",
    "Env. Health",
    True, True, True, True,
)
JVanHorn = User(
    "Jeremy", "VanHorn", 
    "jeremy.vanhorn@yolocounty.org",
    "Env. Health",
    True, True, True, True,
)
SDawley = User(
    "Suzie", "Dawley", 
    "suzie.dawley@yolocounty.org",
    "Env. Health",
    True, True, True, True,
)
eh = [
    CMendoza,
    JHuang,
    JVanHorn,
    SDawley,
]



### Fiscal
KGoradia = User(
    "Kaanan", "Gordia", 
    "kaanan.gordia@yolocounty.org",
    "Fiscal",
    True, True, True, True,
)
KNicholson = User(
    "Kyler", "Nicholson", 
    "kyler.nicholson@yolocounty.org",
    "Fiscal",
    True, True, True, True,
)
KPiazza = User(
    "Krista", "Piazza", 
    "krista.piazza@yolocounty.org",
    "Fiscal",
    True, True, True, True,
)
MFarhoudi = User(
    "Maryam", "Farhoudi", 
    "maryam.farhoudi@yolocounty.org",
    "Fiscal",
    True, True, True, True,
)
SJeet = User(
    "Shriti", "Jeet", 
    "shriti.jeet@yolocounty.org",
    "Fiscal",
    True, True, True, True,
)
SMilliren = User(
    "Shelby", "Milliren", 
    "shelby.milliren@yolocounty.org",
    "Fiscal",
    True, True, True, True,
)
fiscal = [
    KGoradia,
    KNicholson,
    KPiazza,
    MFarhoudi,
    SJeet,
    SMilliren,
]


### Planning
CTschudin = User(
    "Charlie", "Tschudin", 
    "charlie.tschudin@yolocounty.org",
    "Planning",
    True, True, True, True,
)
JAnderson = User(
    "Jeff", "Anderson", 
    "jeff.anderson@yolocounty.org",
    "Planning",
    True, True, True, True,
)
JDTrebec = User(
    "JD", "Trebec", 
    "jd.trebec@yolocounty.org",
    "Planning",
    True, True, True, True,
)
SCormier = User(
    "Stephanie", "Cormier", 
    "stephanie.cormier@yolocounty.org",
    "Planning",
    True, True, True, True,
)
TGonzalez = User(
    "Tracy", "Gonzalez", 
    "tracy.gonzalez@yolocounty.org",
    "Planning",
    True, True, True, True,
)
planning = [
    CTschudin,
    JAnderson,
    JDTrebec,
    SCormier,
    TGonzalez,
]


### Public Works
JBautista = User(
    "Jair", "Bautista", 
    "jair.bautista@yolocounty.org",
    "Public Works",
    True, True, True, True,
)

JPMorra = User(
    "Josue", "Pimentel-Morra", 
    "josue.pmorra@yolocounty.org",
    "Public Works",
    True, True, True, True,
)

SSood = User(
    "Sambhav", "Sood", 
    "smbhav.sood@yolocounty.org",
    "Public Works",
    True, True, True, True,
)
pw = [
    JBautista,
    JPMorra,
    SSood,
]



### Reviewers
JAcevedo = User(
    "Assessor", "Office", 
    "josephine.acevedo@yolocounty.org",
    "Assessor",
    True, True, True, True,
)
KVilla = User(
    "Kim", "Villa", 
    "kim.villa@yolocounty.org",
    "CSA",
    True, True, True, True,
)
PHedrick = User(
    "Pamela", "Hedrick", 
    "pamela.hedrick@yolocounty.org",
    "Int. Waste Management",
    True, True, True, True,
)
ysaqmd = User(
    "Air", "District", 
    "notify@ysaqmd.org",
    "Air District",
    True, True, True, True,
)
reviewers = [
    JAcevedo,
    KVilla,
    PHedrick,
    ysaqmd,
    # ClarksburgFD,
    # DavisFD,
    # DunniganFD,
    # ElkhornFD,
    # EspartoFD,
    # MadisonFD,
    # SpringlakeFD,
    # WoodlandFD,
    # YoloFD,
    # ZamoraFD,
]


usergroups = [
    building,
    eh,
    fiscal,
    planning,
    pw,
    reviewers,
]

