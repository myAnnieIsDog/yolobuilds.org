from requests import get
import json
from pprint import pprint, pformat
from apn_list_ids import apn_ids

# apn_ids = [13938016, 13938017, 13938018, 13938019, 13938020, 13938021, 13938022,]


apn_data = []
for object in apn_ids:
    response = get(f"https://gis.yolocounty.org/ext/rest/services/GISViewer/Parcels_public/FeatureServer/0/query?where=&objectIds={object}&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false&quantizationParameters=&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&featureEncoding=esriDefault&datumTransformation=&f=pjson")
    p = response.json()["features"][0]["attributes"]
    print(type(p))
    apn_data.append(p)

    with open(f"apn/{p['Name'][0:3]}-{p['Name'][3:6]}-{p['Name'][6:9]}.py", "w+") as f:
        f.write(f'{pformat(p)}')


def parcel_list(apn_data):
    list = []
    for apn in apn_data:
        parcel_list.append(apn["Name"])
        
    with open(f"apn/apn_list.py", "w+") as f:
        f.write(f'parcel_list = {pformat(parcel_list)}')