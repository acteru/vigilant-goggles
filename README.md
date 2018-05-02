# vigilant-goggles
python rest-api (mini project)

# Requirements on Arch
``` bash
sudo pacman -S python python-virtualenv
```

# Setup
``` bash
cd <path>/vigilant-goolges
virtualenv flaskapp
pip install -r flaskapp/requirements.txt
```

# Create db
``` bash
source <env>/bin/activate
python model.py
```
# Examples
try it out with httpie or curl

### Query all Couverts
``` bash
http http://127.0.0.1:5000/couverts
curl http://127.0.0.1:5000/couverts
```
### Query Couvert ID 1
``` bash
curl http://127.0.0.1:5000/couvert/1
http http://127.0.0.1:5000/couvert/1
```
### Create new Order
``` bash
http POST http://127.0.0.1:5000/orders couvert_id=1 amount=5
curl -H "Content-Type: application/json" -X POST -d '{"amount":"5", "couvert_id":"1"}' http://127.0.0.1:5000/orders
```
### Query Orders
``` bash
http http://127.0.0.1:5000/orders
curl http://127.0.0.1:5000/orders
```
### Delete Order <id> 2
``` bash
http DELETE http://127.0.0.1:5000/order/2
curl -v -X DELETE http://127.0.0.1:5000/order/2
```
