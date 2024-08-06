from django.db import models

zips = [
    "95605",
    "95606",
    "95607",
    "95612",
    "95615",
    "95616",
    "95618",
    "95620",
    "95627",
    "95637",
    "95645",
    "95653",
    "95679",
    "95691",
    "95694",
    "95695",
    "95697",
    "95698",
    "95776",
    "95816",
    "95937",
    "95961",
]


class District(models.Model):
    dist_type = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255, null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)
    city_state_zip = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} {self.type}"

    class Meta:
        ordering = ["name"]
        verbose_name = "District"
        verbose_name_plural = "Districts"


class FloodZone(models.Model):
    name = models.CharField("Flood Zone Code", max_length=7)
    description = models.CharField("Flood Zone Description", max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.zone_code

    def define_flood_zones():
        li = {
            "A": "Approximate A Zone",
            "AE": "Detailed AE Zone (Regulated)",
            "AO": "Shallow Flooding (Regulated)",
            "X": "Not Regulated",
        }
        for key, value in li:
            zone = FloodZone(zone_code=key, zone_description=value)
            zone.save()

    def list():
        list = {}
        zones = FloodZone.objects.all()
        for zone in zones:
            list[zone.zone_code] = zone.zone_description
        return list

    class Meta:
        verbose_name = "Flood Zone"
        verbose_name_plural = "Flood Zones"


class Jurisdiction(models.Model):
    name = models.CharField(max_length=55, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Jurisdiction"
        verbose_name_plural = "Jurisdictions"


def apn_string_to_display(input: str) -> str:
    book, page, parcel = input[:-6], input[-6:-3], input[-3:]
    return f"{book}-{page}-{parcel}"


class Parcel(models.Model):
    book = models.CharField(max_length=3, default="000")
    page = models.CharField(max_length=3, default="000")
    parcel = models.CharField(max_length=3, default="000")
    full = models.CharField(max_length=15, default="000-000-000")
    active = models.BooleanField(default=True)

    owner_name = models.CharField(max_length=100, null=True, blank=True)
    owner_address = models.CharField(max_length=100, null=True, blank=True)
    land_use_zone = models.CharField(max_length=10, default="A-N")
    wui_sra = models.BooleanField()
    wui_lra = models.BooleanField()
    wui_risk = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    wui_regulations = models.BooleanField()
    flood_a = models.BooleanField()
    flood_ae = models.BooleanField()
    flood_ao = models.BooleanField()
    flood_x = models.BooleanField()
    floodway = models.BooleanField()

    jurisdictions = models.CharField(max_length=255, blank=True)
    jurisdiction_link = models.ForeignKey(
        Jurisdiction, on_delete=models.PROTECT, null=True, blank=True
    )
    districts = models.CharField(max_length=255, blank=True)
    districts_link = models.ManyToManyField(District, blank=True)
    parcels = models.CharField(max_length=255, blank=True)
    parcels_link = models.ManyToManyField("self", symmetrical=True)

    def __str__(self) -> str:
        return f"{self.book}-{self.page}-{self.parcel}"

    class Meta:
        ordering = ["book", "page", "parcel"]
        verbose_name = "Parcel"
        verbose_name_plural = "Parcels"


class CityStZip(models.Model):
    city = models.CharField(max_length=55, blank=True)
    state = "CA"
    zip = models.CharField(max_length=25, blank=True)

    def __str__(self) -> str:
        return f"{self.city}, {self.state} {self.zip}"

    class Meta:
        ordering = ["city", "zip"]
        verbose_name = "City, State Zip"
        verbose_name_plural = "City, State Zip"


class SiteAddress(models.Model):
    parcel = models.CharField(max_length=55, blank=True)
    parcel_link = models.ForeignKey(
        Parcel, on_delete=models.PROTECT, null=True, blank=True
    )
    number = models.CharField(max_length=10, default="12345")
    street = models.CharField(max_length=50, default="County Road 98")
    city_st_zip = models.ForeignKey(
        CityStZip,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="City, State, Zip",
    )
    geolocation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.number} {self.street} {self.city_st_zip}"

    class Meta:
        ordering = ["city_st_zip", "street", "number"]
        verbose_name = "Site Address"
        verbose_name_plural = "Site Addresses"
