import json

dummy_users = [
    {
        "_id": 1,
        "url": "http://initech.tokoin.io.com/api/v2/users/1.json",
        "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
        "name": "Francisca Rasmussen",
        "alias": "Miss Coffey",
        "created_at": "2016-04-15T05:19:46 -10:00",
        "active": True,
        "verified": True,
        "shared": False,
        "locale": "en-AU",
        "timezone": "Sri Lanka",
        "last_login_at": "2013-08-04T01:03:27 -10:00",
        "email": "coffeyrasmussen@flotonic.com",
        "phone": "8335-422-718",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 119,
        "tags": [
            "Springville",
            "Sutton",
            "Hartsville/Hartley",
            "Diaperville"
        ],
        "suspended": True,
        "role": "admin"
    },
    {
        "_id": 2,
        "url": "http://initech.tokoin.io.com/api/v2/users/2.json",
        "external_id": "c9995ea4-ff72-46e0-ab77-dfe0ae1ef6c2",
        "name": "Cross Barlow",
        "alias": "",
        "created_at": "2016-06-23T10:31:39 -10:00",
        "active": True,
        "verified": True,
        "shared": False,
        "locale": "zh-CN",
        "timezone": "Armenia",
        "last_login_at": "2012-04-12T04:03:28 -10:00",
        "email": "jonibarlow@flotonic.com",
        "phone": "9575-552-585",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 106,
        "tags": [
            "Foxworth",
            "Woodlands",
            "Herlong",
            "Henrietta"
        ],
        "suspended": False,
        "role": "admin"
    },
    {
        "_id": 11,
        "url": "http://initech.tokoin.io.com/api/v2/users/11.json",
        "external_id": "f844d39b-1d2c-4908-8719-48b5930bc6a2",
        "name": "Shelly Clements",
        "alias": "Miss Campos",
        "created_at": "2016-06-10T06:50:13 -10:00",
        "active": True,
        "verified": True,
        "shared": True,
        "locale": "zh-CN",
        "timezone": "Moldova",
        "last_login_at": "2016-02-28T04:06:24 -11:00",
        "phone": "9494-882-401",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 103,
        "tags": [
            "Camptown",
            "Glenville",
            "Harleigh",
            "Tedrow"
        ],
        "suspended": False,
        "role": "agent"
    },
    {
        "_id": 19,
        "url": "http://initech.tokoin.io.com/api/v2/users/19.json",
        "external_id": "68e35e26-7b1f-46ec-a9e5-3edcbcf2aeb9",
        "name": "Francis Rodrigüez",
        "alias": "Mr Lea",
        "created_at": "2016-05-05T01:56:24 -10:00",
        "active": False,
        "verified": False,
        "shared": False,
        "locale": "zh-CN",
        "timezone": "Brazil",
        "last_login_at": "2012-05-25T01:55:34 -10:00",
        "phone": "8275-873-442",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 124,
        "tags": [
            "Vicksburg",
            "Kilbourne",
            "Gorham",
            "Gloucester"
        ],
        "suspended": False,
        "role": "agent"
    }
]

dummy_organizations = [
    {
        "_id": 106,
        "url": "http://initech.tokoin.io.com/api/v2/organizations/106.json",
        "external_id": "2355f080-b37c-44f3-977e-53c341fde146",
        "name": "Qualitern",
        "domain_names": [
            "gology.com",
            "myopium.com",
            "synkgen.com",
            "bolax.com"
        ],
        "created_at": "2016-07-23T09:48:02 -10:00",
        "details": "Artisân",
        "shared_tickets": False,
        "tags": [
            "Nolan",
            "Rivas",
            "Morse",
            "Conway"
        ]
    },
    {
        "_id": 119,
        "url": "http://initech.tokoin.io.com/api/v2/organizations/119.json",
        "external_id": "2386db7c-5056-49c9-8dc4-46775e464cb7",
        "name": "Multron",
        "domain_names": [
            "bleeko.com",
            "pulze.com",
            "xoggle.com",
            "sultraxin.com"
        ],
        "created_at": "2016-02-29T03:45:12 -11:00",
        "details": "",
        "shared_tickets": False,
        "tags": [
            "Erickson",
            "Mccoy",
            "Wiggins",
            "Brooks"
        ]
    }
]

dummy_tickets = [
    {
        "_id": "fc5a8a70-3814-4b17-a6e9-583936fca909",
        "url": "http://initech.tokoin.io.com/api/v2/tickets/fc5a8a70-3814-4b17-a6e9-583936fca909.json",
        "external_id": "e8cab26b-f3b9-4016-875c-b0d9a258761b",
        "created_at": "2016-07-08T07:57:15 -10:00",
        "type": "problem",
        "subject": "A Nuisance in Kiribati",
        "description": "Ipsum reprehenderit non ea officia labore aute. Qui sit aliquip ipsum nostrud anim qui pariatur ut anim aliqua non aliqua.",
        "priority": "high",
        "status": "open",
        "submitter_id": 1,
        "assignee_id": 19,
        "organization_id": 120,
        "tags": [
            "Minnesota",
            "New Jersey",
            "Texas",
            "Nevada"
        ],
        "has_incidents": True,
        "via": "voice"
    },
    {
        "_id": "cb304286-7064-4509-813e-edc36d57623d",
        "url": "http://initech.tokoin.io.com/api/v2/tickets/cb304286-7064-4509-813e-edc36d57623d.json",
        "external_id": "df00b850-ca27-4d9a-a91a-d5b8d130a79f",
        "created_at": "2016-03-30T11:43:24 -11:00",
        "type": "task",
        "subject": "A Nuisance in Saint Lucia",
        "description": "Nostrud veniam eiusmod reprehenderit adipisicing proident aliquip. Deserunt irure deserunt ea nulla cillum ad.",
        "priority": "urgent",
        "status": "pending",
        "submitter_id": 1,
        "assignee_id": 11,
        "organization_id": 106,
        "tags": [
            "Missouri",
            "Alabama",
            "Virginia",
            "Virgin Islands"
        ],
        "has_incidents": False,
        "due_at": "2016-08-03T04:44:08 -10:00",
        "via": "chat"
    },
    {
        "_id": "cb304286-7064-4509-813e-edc36d57622d",
        "url": "http://initech.tokoin.io.com/api/v2/tickets/cb304286-7064-4509-813e-edc36d57623d.json",
        "external_id": "df00b850-ca27-4d9a-a91a-d5b8d130a79f",
        "created_at": "2016-03-30T11:43:24 -11:00",
        "type": "task",
        "subject": "A Nuisance in Saint Lucia",
        "description": "",
        "priority": "urgent",
        "status": "pending",
        "submitter_id": 1,
        "assignee_id": 11,
        "organization_id": 106,
        "tags": [
            "Missouri",
            "Alabama",
            "Virginia",
            "Virgin Islands"
        ],
        "has_incidents": False,
        "due_at": "2016-08-03T04:44:08 -10:00",
        "via": "chat"
    },
]

# data type: bytes
dummy_user_data = json.dumps(dummy_users).encode()
dummy_organization_data = json.dumps(dummy_organizations).encode()
dummy_ticket_data = json.dumps(dummy_tickets).encode()
