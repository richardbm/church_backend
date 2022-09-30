## User registration

## Registration
*url:* `/v1/accounts/registration/`

*method:* POST

*headers:* 
* `Content-Type: application/json`

#### Request

*body:*

```
{
    "first_name": "Richard",
    "last_name": "Barrios",
    "email": "rhrichardbm@gmail.com",
	"password": "123456"
}
``` 

#### Response:

*status code:* `201`

*body:*

```
{
    "id": 6,
    "email": "rhrichardbm@gmail.com",
    "first_name": "Richard",
    "last_name": "Barrios",
    "phone_number": null
}
``` 