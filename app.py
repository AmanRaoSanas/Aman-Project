from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('Dashboard.html')

@app.route("/log")
def log():
    return render_template('Login.html')

@app.route("/login", methods=['POST', "GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        print(email,password)
        return render_template('Dashboard.html', email=email)
    return render_template('Login.html')

@app.route("/register", methods=['POST', "GET"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        print(name, email, password)
        return render_template('Login.html')
    return render_template('Register.html')

if __name__ =="__main__":
    app.run(debug=True)