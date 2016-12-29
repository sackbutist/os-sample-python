from flask import Flask
application = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" % name

if __name__ == "__main__":
    application.run()
