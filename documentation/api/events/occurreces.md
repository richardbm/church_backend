## Events

## Event occurrences list
*url:* `/v1/events/occurrences/`

*method:* GET

*headers:* 
* `Content-Type: application/json`

*query params:*
* `start_date: datetime`
* `end_date: datetime`
* `ministry_id: integer`

if you don't pass `start_date` and `end_date` the endpoint will response a 400 status code error with this error detail:

```
{
    "error_message": "start_date date is required"
}
```

#### Response:

*status code:* `200`

*body:*

```
[
    {
        "id": "497867f3-5d52-4a86-ba4c-89f13090eb4e",
        "title": "Servicio domincal",
        "start": "2020-07-26T11:30:00Z",
        "end": "2020-07-26T13:30:00Z",
        "existed": false,
        "event_id": 1,
        "color": "#000000",
        "description": "El servicio",
        "ministries": [],
        "cancelled": false
    },
    {
        "id": "16d67295-8c5e-4f9e-b370-336e3805f092",
        "title": "Biblical school",
        "start": "2020-09-05T10:00:00Z",
        "end": "2020-09-05T12:00:00Z",
        "existed": false,
        "event_id": 4,
        "color": "#000000",
        "description": "This is the biblical school",
        "ministries": [
            {
                "id": 2,
                "name": "Biblical School",
                "description": "The biblical school...",
                "contact_information": {
                    "id": 4,
                    "name": "Biblical school",
                    "description": "",
                    "contact_parameters": []
                }
            }
        ],
        "cancelled": false
    }
]
``` 

Ministries is only returned when the event is associated with a ministry
