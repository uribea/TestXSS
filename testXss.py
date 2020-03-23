# #testXss.py

# from flask import Flask, render_template, redirect, request
# app = Flask(__name__)

# @app.route('/')
# def hi():
#     return render_template('landing.html')
# # $env:FLASK_APP = "flaskr"
# # $env:FLASK_ENV = "development"
# # flask run
# if __name__ == "__main__":
#     app.run(port=4996)

#from: https://nvisium.com/blog/2015/12/07/injecting-flask.html
from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

#based
@app.route('/h')
def hello_ssti():
	person = {'name':"world", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	template = '''<h2>Hello %s!</h2>''' % person['name']
	return render_template_string(template, person=person)

####
# Private function if the user has local files.
###
def get_user_file(f_name):
	with open(f_name) as f:
		return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file # Allows for use in Jinja2 templates

if __name__ == "__main__":
	app.run(debug=False, port=4996)
