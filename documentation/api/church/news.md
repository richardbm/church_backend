## News information

The news in the list endpoint only retries news that haven't expired

## News list
*url:* `/v1/church/news/`

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
        "subject": "Changes in biblical shcool schedule since April 22",
        "content": "Next week the schedule will be on Sunday at 11am",
    },
]
``` 


## Contact detail
*url:* `/v1/church/news/:id`

*method:* GET

*headers:* 
* `Content-Type: application/json`

#### Response:

*status code:* `200`

*body:*

```

{
    "id": 1,
    "subject": "Changes in biblical shcool schedule since April 22",
    "content": "Next week the schedule will be on Sunday at 11am",
}

``` 