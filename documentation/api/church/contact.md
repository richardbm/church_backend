## Conact information

## Contact list
*url:* `/v1/church/contact/`

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
        "name": "John Doe",
        "description": "Main Pastor",
        "contact_parameters": []
    },
    {
        "id": 2,
        "name": "John Doe",
        "description": "Main Pastor",
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
]
``` 


## Contact detail
*url:* `/v1/church/contact/:id`

*method:* GET

*headers:* 
* `Content-Type: application/json`

#### Response:

*status code:* `200`

*body:*

```
{
    "id": 2,
    "name": "John Doe",
    "description": "Main Pastor",
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
``` 