bp24_0001 = {
    "division":"Bldg",
    "recordNumber": "BP24-0000",
    "recordType": "Demolition",
    "description":"Demo SFD for future replacement.",
    "location": {
        "apns": ["000-000-001", "000-000-002"],
        "addresses": ["12345 CR 89", "54321 CR 98"],
        "town": ["Woodland", "Yolo"],
        "landZones": ["A-N", "A-X"],
        "floodZone": ["X", "A", "AE", "AO"],
        "expansive_soil": ["Normal", "Moderate", "High"],
        "wui": ["No", "Yes"],
        "fire_dist": "Springlake Fire District",
        "school_dist": "Woodland Unified School District",
        "service_dist": False,
    },
    "alerts": False,
    "notes": False,
    "plan_location": "Electronic Submittal",
    "contacts": [
        {
            "role": "Owner",
            "cslb": False,
            "designer": False,
            "company": False,
            "firstName": "John Jacob",
            "lastName": "Smith",
            "address": "19999 CR 85",
            "cityStZip": "Woodland, CA 95695",
            "phone": "530-666-0000",
            "email": "owner@home.com",
            "alerts": False,
        },
        {
            "role": "Contractor",
            "cslb": {
                "number": "1299000", 
                "class": ["A", "B", "C-10"]},
            "designer": {
                "number": "1299000", 
                "class": ["Civil", "Structural"]},
            "company": "Golden Hammers",
            "firstName": "George",
            "lastName": "Jones",
            "address": "19949 CR 25",
            "cityStZip": "Woodland, CA 95695",
            "phone": "530-666-1111",
            "email": "golden@hammers.com",
            "alerts": True,
        },
        {
            "role": "Applicant",
            "owner": False,
            "contractor": True
        }
    ],
    "demolitionDetails": {"": ""},
    "reviews": [
        {
            "type": "Building",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            "cycle_1": {
                "result": "Comments",
                "reviewer": "sdoolittle",
                "due": "2024-04-23T18:25:43.511Z",
                "completed": "2024-04-23T18:25:43.511Z",
                "notes": "See attached email.",
            },
            "cycle_2": {
                "result": False,
                "reviewer": "First Available",
                "due": False,
                "completed": False,
                "notes": False,
            },
            },
        {
            "type": "Env. Health",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            },
        {
            "type": "Fire",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            },
        {
            "type": "Flood",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            },
        {
            "type": "Int. Waste Management",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            },
        {
            "type": "Planning",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            "cycle_1": {
                "result": "Under Review",
                "reviewer": "tgonzalez",
                "due": "2024-04-23T18:25:43.511Z",
                "completed": False,
                "notes": False,
                },
                },
        {
            "type": "Public Works",
            "status": "Waiting for resubmittal",
            "notes": "See attached email.",
            },
    ],
    "inspections": [{
            "inspection": "Bldg Pre-Demolition",
            "stopNum": "1",
            "result": "Comments",
            "inspector": "sdoolittle",
            "date": "2024-04-23T00:00:00.000Z",
            "window": "2024-04-23T00:10:00.000Z",
            "notes": ""
        },{
            "inspection": "Bldg Pre-Demolition",
            "stopNum": "2",
            "result": "Approved",
            "inspector": "sdoolittle",
            "date": "2024-05-23T00:00:00.000Z",
            "window": "2024-05-23T00:10:00.000Z",
            "notes": ""
        },{
            "inspection": "IWM C&D Recycling Receipts",
            "stopNum": "1",
            "result": "",
            "inspector": "",
            "date": "",
            "window": "",
            "notes": "This inspection has not been requested."
        }
    ],
    "fiscal": {
        "summary":{
            "total": "6,000.00",
            "paid": "3,500.00",
            "remaining": "2,500.00"
        },
        "details":[
            {
                "description": "Plan Review",
                "rate": "$0.80",
                "units": "Square Feet",
                "quantity": "3,000",
                "amount": "$2,400.00",
                "paid": "2024-05-23T00:00:00.000Z",
                "invoice": "0000000001",
                "acct": "06695940302349083459834592302348934598345982345"
            },
            {
                "description": "Inspection",
                "rate": "$1.20",
                "units": "Square Feet",
                "quantity": "3,000",
                "amount": "$3,600.00",
                "paid": "NO",
                "invoice": "",
                "acct": "06695940302349083459834592302348934598345982345"
            }
        ],
        "payments": {
            "date": "2024-05-23T00:00:00.000Z",
            "amount": "2,400.00",
            "invoice": "00980987"
        }
    },
    "documents": {
        "apps": [
            "path1.pdf",
            "path2.pdf",
            "path3.pdf",
            "path4.pdf"
        ],
        "calcs": [
            "path1.pdf",
            "path2.pdf",
            "path3.pdf",
            "path4.pdf"
        ],
        "plans": [
            "path1.pdf",
            "path2.pdf",
            "path3.pdf",
            "path4.pdf"
        ],
    },
}