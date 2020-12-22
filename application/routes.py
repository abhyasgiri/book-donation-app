from application import app, db
from application.models import Books
from application.forms import BookForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_books = Books.query.all()               #to view my tasks READ
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)

@app.route("/create", methods = ["GET", "POST"])                       
def create():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_book = Books(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add.html", title="Create a task", form=form)

@app.route("/watchlist/<int:id>")            #to set a task to do as complete
def watchlist(id):
    book = Books.query.filter_by(id=id).first()
    book.watchlisted = True
    db.session.commit()
    return f"Book {id} has been added to the watchlist"

@app.route("/update/<int:id>", methods = ["GET", "POST"])              #to update something on the to do list
def update(id):
    form = Form()
    book = Books.query.filter_by(id=id).first()
    if request.method == "POST":
        book.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Book", book=book)


@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def delete(id):
    book = Books.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home")) 