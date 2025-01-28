from flask import Flask, redirect, url_for, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def index():  # Renamed to 'index'
    return render_template("home.html")

@app.route('/home')
def home():  # Kept as 'home'
    return "Hello, Yash Pandey!"

@app.route('/<name>')
def user(name):  # Kept as 'user'
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
