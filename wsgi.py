from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!!!!!!!!!!!!!!"

@application.route("/hello/<user>")
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == "__main__":
    application.run()
