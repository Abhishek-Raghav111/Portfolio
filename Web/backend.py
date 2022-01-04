import json
from click.core import Parameter
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/portfolio'
db = SQLAlchemy(app)

class Contacts(db.Model):
    # sno. ,name, email, Phone_num, Quiry, date....
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40),  nullable=False)
    Phone_num = db.Column(db.String(12), nullable=False)
    Quiry = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12),nullable=True)



@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")


# Get request se website fetch hoti h (refresh krne pr console m bhi dikhti h)
@app.route("/contact", methods=["GET","POST"])
def contact():

    if(request.method == 'POST'):
        # Add entry to the database
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        quiry = request.form.get('quiry')

        entry = Contacts(name = name, email = email, Phone_num = phone, Quiry = quiry,  date=datetime.now() )
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")

app.run(debug=True)