from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!!!!!!!!!!!!!!"

@application.route("/hello/<user>")
def hello_name(user):
   return render_template('hello.html', name = user)

@application.route('/student')
def student():
   return render_template('student.html')

@application.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("result.html",result = result)

if __name__ == "__main__":
    application.run()
