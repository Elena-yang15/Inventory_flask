from flaskinventory import db
from datetime import datetime

class Product(db.Model):

    __tablename__ = 'products'
    product_id  = db.Column(db.Integer, primary_key=True)
    product_name   = db.Column(db.String(200), unique = True, nullable = False)
    product_num = db.Column(db.Integer, nullable = False)
    date_created  = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.product_id

class Location(db.Model):
    __tablename__   = 'locations'
    location_id  = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(200), unique = True ,nullable = False)
    
    def __repr__(self):
        return '<Location %r>' % self.location_id

class Shipments(db.Model):

    __tablename__   = 'shipments'
    ship_id  = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), db.ForeignKey('products.product_name'))
    ship_num = db.Column(db.Integer, nullable = False)
    from_loc = db.Column(db.String(200), db.ForeignKey('locations.location_name'))
    to_loc = db.Column(db.String(200), db.ForeignKey('locations.location_name'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    
    def __repr__(self):
        return '<Shipment %r>' % self.ship_id
db.create_all()
db.session.commit()
