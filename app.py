##app.py for mysite_app

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/about")
def about():
    return " <h3> About Page </h3>"  

@app.route("/contact")
def contact():
    return " <h3> Contact Us </h3>"  


##This is where we run our app

if __name__  == "__main__":
    app.run(
        debug = True,
        port = 3000
    )


    ## importing our libraries
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

## instantiating the app object
app = Flask(__name__)

# connecting to our database called product.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'

# instantiating the database object
db = SQLAlchemy(app)

# creating the database "model" or class called Languages
class Products(db.Model):
    Product_id = db.Column(db.String, primary_key=True)
    Image = db.Column(db.String, nullable=False)
    Name = db.Column(db.String)
    Cost = db.Column(db.Integer)
    Desc = db.Column(db.String)

# this creates the model (or "columns") for our db object
db.create_all()

# adding data to our database by creating objects from the above class
# in total, we are adding 3 objects or rows to our database
product_1 = Product(
    Product_id = "1",
    Image = "../static/1.png",
    Name = "Anklet",
    Cost = 20,
    Desc = "Ileke anklets are made out of crystal beads and precious stones."
)
product_2 = Product(
    Product_id = "2",
    Image = "../static/2.png",
    Name = "Earrings",
    Cost = 15,
    Desc = "Our beautiful handmade earrings are just the piece you need  to add to your collection ."
)
product_3 = Product(
    Product_id = "3",
    Image = "../static/3.png",
    Name = "Waistbeads",
    Cost = 25,
    Desc = "Whether you want to accessorize your waist or own a beautiful weight tracker, our ileke waistbeads are your to go to make you feeling beautiful all day long "

# these lines add each of our objects to the session
db.session.add(product_1)
db.session.add(product_2)
db.session.add(product_3)

# and then the db.session.commit() line commits the changes to the .db file
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()

# here is the list of dictionaries we are using for our API
api_data = [
    {
        "product_id": "1",
        "Image": "../static/1.png",
        "Name": "Anklet",
        "Cost": 20,
        "Desc": "Ileke anklets are made out of crystal beads and precious stones."
    },
    {
        "product_id": "2",
        "Image": "../static/2.png",
        "Name": "earrings",
        "Cost": 15,
        "Desc": "Our beautiful handmade earrings are just the piece you need  to add to your collection ."
    },
    {
        "product_id": "3",
        "Image": "../static/3.png",
        "Name": "Waistbeads",
        "Cost": 25,
        "Desc": "Whether you want to accessorize your waist or own a beautiful weight tracker, our ileke waistbeads are your to go to make you feeling beautiful all day long "

    }
]

# here is our default route
@app.route("/")
def index():
    # this line grabs all the rows in our database and saves it as a list called product_data
    prod_data = Product.query.all()
    # don't forget to pass the list prod_data to the template!
    return render_template("index.html", Prod_list=prod_data)

# here is our about route
@app.route("/about")
def about():
    return render_template("about.html")

# here is our API endpoint
@app.route("/api")
def api():
    return jsonify(api_data)

# here is our dynamic route!
# in this route, <slug> is a variable that gets passed to the function below
@app.route("/details/<slug>")
def details(slug):
    # python takes the variable slug, and asks the database for the row with that as a primary key
    prod_item = Product.query.get(slug)
    # then we pass that row to the template "details"
    return render_template("details.html", prod_item=prod_item)

## this is where we run our app
# it goes at the bottom and we don't need to touch it!
if __name__ == "__main__":
    app.run(
        debug = True,
        port = 3000
    ) 
