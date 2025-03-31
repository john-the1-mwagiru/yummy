import re
from flask import flash, request, render_template, url_for, redirect, session
from app import app
from app.database import users, category, recipe

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/registration", methods=["POST", "GET"])
def registration():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        all_users = users.UserModel.get_all()
        existing_user = [auser for auser in all_users if auser.email == username]
        if (
            len(existing_user) != 0
            or not password
            or not confirm_password
            or password != confirm_password
            or not re.fullmatch(email_regex, username)
        ):
            error = "Please check your input"
            return render_template(
                "registration.html",
                error=error,
                username=username,
                password=password,
                confirm_password=confirm_password,
            )
        else:
            new_user = users.User(
                id=None, email=username, password=password, user_id=None
            )
            users.UserModel.create(new_user)
            return redirect(url_for("log_in"))
    else:
        return render_template("registration.html")


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
                return redirect(url_for("index"))
        error = "Invalid credentials"
        return render_template(
            "login.html", error=error, username=username, password=password
        )
    else:
        return render_template("login.html")


@app.route("/categories")
def categories():
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


@app.route("/categories/<int:id>")
def single_category(id):
    acategory = category.CategoryModel.get(id)
    all_recipes = recipe.RecipeModel.get_all()
    user_recipes = [
        recipe for recipe in all_recipes if recipe.user_id == acategory.user_id
    ]
    return render_template(
        "category.html", acategory=acategory, user_recipes=user_recipes
    )


@app.route("/categories/<int:id>/edit", methods=["POST", "GET"])
def edit_category(id):
    acategory = category.CategoryModel.get(id)

    if request.method == "POST":
        category_name = request.form["category-name"]
        category_description = request.form["category-description"]
        acategory.name = category_name
        acategory.description = category_description
        updated_category = category.CategoryModel.update(id, acategory)
        return redirect(url_for("categories"))
    return render_template("edit-category.html", acategory=acategory)

@app.route("/categories/create", methods=["POST", "GET"])
def create_category():
    if request.method == "POST" and "username" in session:
        username = session["username"]
        all_users = users.UserModel.get_all()
        categories = category.CategoryModel.get_all()
        category_name = request.form["category-name"]
        category_description = request.form["category-description"]
        active_user = [logged_user for logged_user in all_users if logged_user.email == username]
        for a_user in active_user:
            new_category = category.Category(id=None,name=category_name,description=category_description,user_id=a_user.user_id)
            category.CategoryModel.create(new_category)
            return redirect(url_for("categories"))
    return render_template("create-category.html")

