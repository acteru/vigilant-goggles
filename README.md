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

## Query all Couverts
``` bash
http http://127.0.0.1:5000/couverts
```
## Query Couvert ID 1
``` bash
http http://127.0.0.1:5000/couvert/1
```
## Create new Order
``` bash
http POST http://127.0.0.1:5000/orders couvert_id=1 amount=5
```
## Query Orders
``` bash
http http://127.0.0.1:5000/orders
```
## Delete Order <id> 2
``` bash
http DELETE http://127.0.0.1:5000/order/2
```

