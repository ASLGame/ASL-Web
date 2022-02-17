from api import app

@app.route("/hello")
def hello_world():
    return "Hello World"