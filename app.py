from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# DB creation
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route("/")
def index():
    return render_template('Dashboard.html')

@app.route("/login", methods=['POST', "GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.todos.find_one({"email": email})
        if email==user.get('email') and password == user.get('password'):
            return render_template('Dashboard.html', user=user)
    return render_template('Login.html')

@app.route("/register", methods=['POST', "GET"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        db.todos.insert_one({'name':name, 'email':email, 'password':password})
        print(name, email, password)
        return render_template('Login.html')
    return render_template('Register.html')

if __name__ =="__main__":
    app.run(debug=True)