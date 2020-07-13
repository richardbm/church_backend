## Information about the church

## About list
*url:* `/v1/church/about/`

*method:* GET

*headers:* 
* `Content-Type: application/json`

#### Response:

*status code:* `200`

*body:*

```
[
    {
        "id": 2,
        "label": "Mission",
        "description": "This is the mission of the church..."
    },
    {
        "id": 1,
        "label": "Vision",
        "description": "This is the vision of the church..."
    },
    {
        "id": 3,
        "label": "History",
        "description": "This is the history of the church..."
    }
]
``` 

## About detail
*url:* `/v1/church/about/:id`

*method:* GET

*headers:* 
* `Content-Type: application/json`

#### Response:

*status code:* `200`

*body:*

```
{
    "id": 2,
    "label": "Mission",
    "description": "This is the mission of the church..."
}
``` 