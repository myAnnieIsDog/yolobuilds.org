from requests import get
import json
from os import path, listdir
from pathlib import Path
from pprint import pprint, pformat
from data.apns import apn_list_ids
from data.addresses import address_list_ids
import re


GIS_PUBLIC = (
    f"https://experience.arcgis.com/experience/1c0ae779a0f7456185f1910ef588d8fb"
)
GIS_INTERNAL = f"https://portal.yolocounty.org/portal/apps/webappviewer/index.html?id=88a748eaeb1f471e8294393adc3b0b21"
GIS_BUILDING = f"https://yolo.maps.arcgis.com/apps/View/index.html?appid=a36499d6ec8f494ba6974de0ca9b95d0"


def run():
    print("start run")
    # get_apn_ids()
    # get_apn_details()
    # get_address_ids()
    # get_addresses_details(address_list_ids)
    # extension("details_apns/test")
    # get_highest_apn_id("details_apns")
    replace_text("details_apns")

    print("run complete")


def extension(from_dir):
    for filename in listdir(from_dir):
        f = Path(from_dir, filename)
        f.rename(str(f).replace(".txt", ".py"))


def replace_text(from_dir):
    for filename in listdir(from_dir):
        with open(path.join(from_dir, filename), "w+") as f:
            d = f.read()
            f.write(re.sub(r"details_apns.*txt", "", re.escape(d)))


def get_highest_apn_id(from_dir):
    ids = {}
    d = {}
    for filename in listdir(from_dir):
        with open(path.join(from_dir, filename), "r") as f:
            d = dict(f.read())
            if type(d) != "dict":
                print(d, type(d))
                return
    #         z = {d["id"]: d["apn"]}
    #         ids.update(z)
    # pprint(ids)

    #     p = json.load(f"details_apns/003-130-031.txt")
    #     print(p)
    #     id = int(p["OBJECTID"])
    #     ids.add(id)
    # a = max(ids)
    # print(a)
    # return a


def hightest_address_id():
    pass


def get_address_ids():
    response = get(
        f"https://gis.yolocounty.org/ext/rest/services/GISViewer/Addresses/FeatureServer/0/query?where=ADDR_HN+LIKE+%27%25%27&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=true&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=pjson"
    )
    address_ids = response.json()
    with open(f"address_list/address_ids.txt", "w+") as f:
        f.write(f"{pformat(address_list_ids)}")


def get_addresses_details(list):
    for id in list:
        response = get(
            f"https://gis.yolocounty.org/ext/rest/services/GISViewer/Addresses/FeatureServer/0/query?where=&objectIds={id}&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=pjson"
        )
        p = response.json()["features"][0]["attributes"]
        with open(
            f"address_details/{str(p['ADDR_HN']).replace('/', '_')} {str(p['ADDR_SN']).replace('/', '_')}.txt",
            "w+",
        ) as f:
            f.write(f"{pformat(p)}")

    print("got ids")


def get_apn_ids():
    response = get(
        f"https://gis.yolocounty.org/ext/rest/services/GISViewer/Addresses/FeatureServer/0/query?where=ADDR_HN+LIKE+%27%25%27&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=true&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=pjson"
    )
    apn_ids = response.json()
    with open(f"data/addresses.txt", "w+") as f:
        f.write(f"{pformat(apn_ids)}")


def get_apn_details(list):
    for apn_id in list:
        response = get(
            f"https://gis.yolocounty.org/ext/rest/services/GISViewer/Parcels_public/FeatureServer/0/query?where=&objectIds={apn_id}&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=pjson"
        )
        p = response.json()["features"][0]["attributes"]
        with open(
            f"apn_details/{p['Name'][0:3]}-{p['Name'][3:6]}-{p['Name'][6:]}.txt", "w+"
        ) as f:
            f.write(f"{pformat(p)}")


print("loaded")
if __name__ == "__main__":
    run()
