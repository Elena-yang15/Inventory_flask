# Flask Inventory Tracking Management

This project is for [Shopify backend intern 2022 Challenge](https://docs.google.com/document/d/1PoxpoaJymXmFB3iCMhGL6js-ibht7GO_DkCF2elCySU/edit)

## Technologies
- Python
- Flask
- SQLALCHEMY
- WTForms
- HTML

## Key features
- View a list of available products and warehouses/locations 
- Add new products and warehouses
- Edit existing products and warehouses
- Delete existing products and warehouses
- Create "Shipment", assign available products to the shipment

## Get Started
- First, clone this repository and change your path to its folder.
```
git clone https://github.com/Elena-yang15/Inventory_flask.git
cd flask_inventory_tracking
```

- Then install all prerequirement.
```
pip install -r requirements.txt
```

- Run the app
```
python run.py
```

## Running the App
- The Overview Page shows the lists of available products and locations.
![screenshot for project](pictures/list.png)
![screenshot for project](pictures/available.png)

- Add new product
![screenshot for project](pictures/add.png)

- Edit product
![screenshot for project](pictures/edit.png)

- Delete product
![screenshot for project](pictures/delete.png)

- View products and locations
![screenshot for project](pictures/list2.png)
![screenshot for project](pictures/loc.png)

- Create new shipment, select the product and locations from the database
![screenshot for project](pictures/addship.png)
![screenshot for project](pictures/shipshow.png)


- Error: Same From location and To location
![screenshot for project](pictures/shiperr2.png)

- Error: Insufficient products for the shipment
![screenshot for project](pictures/shiperr.png)



