# dropit-backend-test

### The stack I use for this project:

- API Gateway as routing API (AWS)
- Lambda functions to handle requests (AWS)
- MongoDB as NoSQL database
- Written in Python

#### API Endpoint Base URI
https://6n1dhvs6hc.execute-api.us-east-1.amazonaws.com/develop/

#### POST:

#### /resolve-address

`````
{
    "searchTerm" : "jabotinsky ramat gan israel"
}
`````
##
#### /timeslots

(working request)
`````
{
    "address" : {
        "postcode": "5200100"
    }
}
`````
(not working request)
`````
{
    "address" : {
        "postcode": "500"
    }
}
`````
##
#### /deliveries

(working request)
`````
{
    "user" : {
        "name": "yoel"
    },
    "timeslot_id": "1"
}
`````
##
#### /deliveries/{delivery_id}/complete

(working request)
`````
delivery_id = 62efd520fb4bc28de6f85f77
`````

(non working request)
`````
delivery_id = yoel
delivery_id = 62efd520fb4bc28de6f85f74

`````
##
#### DELETE:
#### /deliveries/{delivery_id}

(working request)
`````
delivery_id = 62efd520fb4bc28de6f85f77
`````

(non working request)
`````
delivery_id = yoel
delivery_id = 62efd520fb4bc28de6f85f74

`````
