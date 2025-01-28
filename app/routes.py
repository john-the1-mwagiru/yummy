from flask import flash, request,render_template, url_for,redirect, session
from app import app
from app.database import users,category
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
@app.route('/index')
def index():

    return  render_template("index.html")
@app.route('/log-in', methods=['POST', 'GET'])
def log_in():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        session["username"]=username
        password = request.form["password"]
        all =users.UserModel.get_all()
        for user in all:
            if user.email == username and user.password == password  :
                flash("You were successfully logged in")
                return redirect(url_for("index"))
            error = "Invalid credentials"    
            return render_template("login.html", username=username, password=password, error=error)
    
    return render_template("login.html")



        
