from flask import  (
    Flask,
    render_template
)

app = Flask(__name__)

@app.route('/')
def  index():
    return "<h1> Flask 001 - Hi </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")
@app.route('/employ')
def  employ():
    return render_template("employee.html")
@app.route('/order')
def  order():
    return render_template("order.html")  
@app.route('/manage')
def  manage():
    return render_template("manage.html")
@app.route('/report')
def  report():
    return render_template("report.html")