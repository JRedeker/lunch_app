from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index-new.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')

@app.route("/new")
def test():
    return render_template('index-mdl.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
