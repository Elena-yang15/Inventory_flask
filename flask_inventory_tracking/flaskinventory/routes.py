from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from flaskinventory import app, db
from flaskinventory.models import Product, Location, Shipments
from flaskinventory.forms import editproduct, editlocation, deleteproduct, deletelocation

@app.route('/')
def home_page():  # home page: view a list of products and locations
    products = Product.query.order_by(Product.product_id).all()
    locations = Location.query.order_by(Location.location_id).all()
    return render_template("home.html", products = products, locations = locations)

@app.route('/products/', methods=["POST", "GET"])
def product_page():
    eform = editproduct()
    dform = deleteproduct()
    if request.method == "POST":
        if 'product_name' in request.form: # add new product
            product_name = request.form["product_name"]
            product_num = request.form["product_num"]
            new_product = Product(product_name=product_name, product_num=product_num)
            try:
                db.session.add(new_product)
                db.session.commit()
                flash(f'Your product has been added!', 'success')
            except:
                flash(f"Something wrong!", "danger")
        elif eform.validate_on_submit(): # edit existing product
            chosen_productname = request.form.get("productname","")
            chosen_product = Product.query.filter_by(product_name = chosen_productname).first()
            chosen_product.product_name = eform.editname.data
            chosen_product.product_num = eform.editnum.data
            try:
                db.session.commit()
                flash(f'Your product has been edited!', 'success')
            except:
                flash(f"Something wrong!", "danger")
        elif dform.validate_on_submit(): # delete product
            chosen_productname = request.form.get("productname")
            chosen_product = Product.query.filter_by(product_name = chosen_productname).first()
            try:
                db.session.delete(chosen_product)
                db.session.commit()
                flash(f'Your product has been deleted!', 'danger')
            except:
                flash(f"Something wrong!", "danger")
        return redirect("/products/")    

    products = Product.query.order_by(Product.product_id).all()
    return render_template("products.html", products=products, eform = eform, dform = dform)

@app.route('/locations/', methods=["POST", "GET"])
def location_page():
    eform = editlocation()
    dform = deletelocation()
    if request.method == "POST":  
        if 'location_name' in request.form:  # add new location
            location_name = request.form["location_name"]
            new_location = Location(location_name=location_name)
            try:
                db.session.add(new_location)
                db.session.commit()
                flash(f'The location has been added!', 'success')
            except:
                flash(f"Something wrong!", "danger")
        elif eform.validate_on_submit(): # edit location
            chosen_locationname = request.form.get("locationname","")
            chosen_location = Location.query.filter_by(location_name = chosen_locationname).first()
            chosen_location.location_name = eform.editname.data
            try:
                db.session.commit()
                flash(f'The location has been edited!', 'success')
            except:
                flash(f"Something wrong!", "danger")
        elif dform.validate_on_submit(): # delete location
            chosen_locname = request.form.get("locationname")
            chosen_loc = Location.query.filter_by(location_name = chosen_locname).first()
            try:
                db.session.delete(chosen_loc)
                db.session.commit()
                flash(f'The location has been deleted!', 'danger')
            except:
                flash(f"Something wrong!", "danger")
        return redirect("/locations/")
    locations = Location.query.order_by(Location.location_id).all()
    return render_template("locations.html", locations=locations, eform=eform, dform = dform)

@app.route("/shipments/", methods=["POST", "GET"])
def shipment_page():
    if request.method == "POST" :
        product_name = request.form["productName"]
        ship_num = request.form["shipNum"]
        fromLoc = request.form["fromLocation"]
        toLoc = request.form["toLocation"]
        chosen_product = Product.query.filter_by(product_name = product_name).first()
        if fromLoc == toLoc:
            flash(f"Same locations! Please change a different one.", "danger")
        elif chosen_product.product_num < int(ship_num):
            flash(f"Not enough products for shipping. Please add some products first.", "danger")
        else:
            new_shipment = Shipments(product_name=product_name, ship_num=ship_num, 
                                 from_loc=fromLoc, to_loc=toLoc)
            chosen_product.product_num -= int(ship_num)
            try:
                db.session.add(new_shipment)
                db.session.commit()
                flash(f'New shipment has been added!', 'success')
            except:
                flash(f"Something wrong!", "danger")
        return redirect("/shipments/")

    else:
        products = Product.query.order_by(Product.product_id).all()
        locations = Location.query.order_by(Location.location_id).all()
        shipments = Shipments.query\
        .join(Product, Shipments.product_name == Product.product_name)\
        .add_columns(
            Shipments.ship_id,
            Shipments.ship_num,
            Shipments.product_name, 
            Shipments.from_loc,
            Shipments.to_loc,
            Shipments.date)\
        .all()

        return render_template("shipments.html", shipments=shipments, products=products, locations=locations)


