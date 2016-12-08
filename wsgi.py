from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!!!!!!!!!!!!!!"

@application.route("/hello/<user>")
def hello_name(user):
   return render_template('hello.html', name = user)

@application.route("/result")
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == "__main__":
    application.run()
