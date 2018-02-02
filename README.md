# taxiapp project
Taxi app for drivers and passengers

#### Api documentaion
#### Authentication is not requred for GET, POST and PUT options

### GET option gives User profile http://127.0.0.1:8000/v1/user/1/

###Allow: GET, POST, HEAD, OPTIONS http://127.0.0.1:8000/v1/user/rides/
#this lists all rides of the user

### GET, POST, PUT, DELETE, OPTIONS http://127.0.0.1:8000/v1/user/rides/1/
#Example:

```{
        "id": 1,
        "user": 1,
        "start_place": "Tashkent",
        "finish_place": "Samarkand",
        "pickup_date": "2018-02-02",
        "pickup_time": "14:10:15",
        "offer_price": "100000",
        "location_from": "SRID=4326;POINT (-108.6920766200656 19.45750991969817)",
        "location_to": "SRID=4326;POINT (57.98172215765408 24.60707483599072)",
        "created": "2018-02-02T14:10:27.504654+05:00",
        "status": "completed"
}```
#Here Customers can post, put and delete, and Drivers can put json to change status of the offer and when the offer is completed driver change the status of the offer to completed and puts offer price
