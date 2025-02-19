from flask import flash, request, render_template, url_for, redirect, session
from app import app
from app.database import users, category

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/log-in", methods=["POST", "GET"])
def log_in():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        all_users = users.UserModel.saved_users
        for active_user in all_users:
            if active_user.email == username and active_user.password == password:
                return redirect(url_for("index", username=username))
        error = "Invalid credentials"
        return render_template(
            "login.html", error=error, username=username, password=password
        )
    else:
        return render_template("login.html")


@app.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"


@app.route("/categories")
def username():
    if "username" in session:
        username = session["username"]
        all = users.UserModel.get_all()
        categories = category.CategoryModel.get_all()
        user = [logged_user for logged_user in all if logged_user.email == username]

        for a_user in user:
            user_category = [
                category
                for category in categories
                if category.user_id == a_user.user_id
            ]
            return render_template("categories.html", user_category=user_category)
    else:
        return redirect(url_for("index"))
