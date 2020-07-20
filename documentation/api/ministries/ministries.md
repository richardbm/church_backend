## Ministries

## Ministries list
*url:* `/v1/ministries/ministries/`

*method:* GET

*headers:* 
* `Content-Type: application/json`

#### Response:

*status code:* `200`

*body:*

```
[
    {
        "id": 1,
        "name": "Biblical School",
        "description": "The biblical school...",
        "contact_information": {
            "id": 3,
            "name": "Biblical school",
            "description": "",
            "contact_parameters": [
                {
                    "id": 2,
                    "label": "Email",
                    "value": "john@doe.com"
                },
                {
                    "id": 1,
                    "label": "Phone number",
                    "value": "+56 912345678"
                }
            ]
        }
    }
]
``` 


## Ministry detail
*url:* `/v1/ministries/ministries/:id`

*method:* GET

*headers:* 
* `Content-Type: application/json`

#### Response:

*status code:* `200`

*body:*

```
{
    "id": 1,
    "name": "Biblical School",
    "description": "The biblical school...",
    "contact_information": {
        "id": 3,
        "name": "Biblical school",
        "description": "",
        "contact_parameters": [
            {
                "id": 2,
                "label": "Email",
                "value": "john@doe.com"
            },
            {
                "id": 1,
                "label": "Phone number",
                "value": "+56 912345678"
            }
        ]
    }
}
``` 