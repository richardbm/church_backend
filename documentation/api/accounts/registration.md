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
	"client_id": "F4EQh8ah8vjH6OcL3lz54DmAxeJOMAnzjwxqBH3y",
	"client_secret": "fdhwJ9y2c1um7vdVz0r7bxCNtSLRc1m0vXs98GOwQe3kBienF2nRiKJCcAYXIxgfM8DgQDW5Ii9q1crKq4cGp3lnuLiYxSYLzkf1fL5nqPipqqh5CkpDohB2K124ca16",
	"grant_type": "password",
	"username": "richard",
	"password": "123456"
} 
``` 

#### Response:

*status code:* `201`

*body:*

```
{
	"client_id": "F4EQh8ah8vjH6OcL3lz54DmAxeJOMAnzjwxqBH3y",
	"client_secret": "fdhwJ9y2c1um7vdVz0r7bxCNtSLRc1m0vXs98GOwQe3kBienF2nRiKJCcAYXIxgfM8DgQDW5Ii9q1crKq4cGp3lnuLiYxSYLzkf1fL5nqPipqqh5CkpDohB2K124ca16",
	"grant_type": "password",
	"username": "richard",
	"password": "123456"
} 
``` 