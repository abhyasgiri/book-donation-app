from application import app, db
from application.models import Books, Shops
from application.forms import BookForm, ShopForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_books = Books.query.all()
    all_shops = Shops.query.all()               #to view my tasks READ
    return render_template("index.html", title="Home", all_books=all_books, all_shops=all_shops)

@app.route("/create", methods = ["GET", "POST"])                       
def create():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_book = Books(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add.html", title="Create a book", form=form)

@app.route("/update/<int:id>", methods = ["GET", "POST"])              #to update something on the to do list
def updateshop(id):
    form = Form()
    shop = Shops.query.filter_by(id=id).first()
    if request.method == "POST":
        shop.shop_name = form.shop_name.data
        shop.location = form.location.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Shop", shop=shop)


@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def delete(id):
    book = Books.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home")) 

@app.route("/createshop", methods = ["GET", "POST"])
def createshop():
    form = ShopForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_shop = Shops(shop_name=form.shop_name.data, location=form.location.data)
            db.session.add(new_shop)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add.html", title="Create a shop", form=form)