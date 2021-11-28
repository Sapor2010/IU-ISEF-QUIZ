from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/menu", methods=['GET'])
def menu():
    return render_template('menu.html')


@app.route("/help", methods=['GET'])
def help():
    return render_template('help.html')

#Error Handling
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

