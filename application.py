from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')


@app.route("/help")
def help():
    return render_template('help.html')

#Error Handling
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

