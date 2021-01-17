# WishList_API_Project

## A REST project with API endpoints consumable by the end user. 

### i) Endpoint for UUID access generator for private and public user: /api/access_level/

Data:

```json
{ 
  "access_level": <access_level> 
} 
```

### ii) Endpoint for Private API: /api/private_wish/<wish_number>

Data: 

```json

{
    "wish_id": <wish_number usually auto updated>,
    "wish": <wish>,
    "amount_wished": <The amount wished>,
    "destination_uri": <destination URI of the wish>,
    "image_uri": <Image URI of the wish>
}

```


### iii) Endpoint for Public API: /api/public_wish/<wish_number>

Data:

```json
{
    "amount_granted": <Enter amount to be granted>
}
```

Access Level can be either private or public. Depending on the type of access various operations can be performed.

Using Private API endpoint, GET, POST, UPDATE and DELETE operations can be performed and the amount granted cannot be viewed. Only the amount wished is visible.

Whereas using Public API endpoint, one can update the amount granted for a particular wish. Also GET can be used to view the amount granted for each of the wish along with other wish details. 

Using the access Level, a UUID can be generated for the public or private user and only that ID can be used to access the API endpoints that would be available.



