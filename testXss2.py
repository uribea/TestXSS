#testXss2.py
import os
from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

#based
@app.route('/h2')
def hello_ssti():
	person = {'name':"world", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
	# if request.args.get('name'):
	# 	person['name'] = request.args.get('name')
	person['name'] = request.args.get('name')
	template = '''<h2>Hello %s!</h2>''' % person['name']
	return render_template_string(template, person=person)

#Attack:
#http://localhost:4996/h2?name=Ry.%20%3Cscript%3Ealert(%22Full%20protection%20not%20yet%20achieved.%22)%3C/script%3E
if __name__ == "__main__":
	app.run(debug=False, port=4996)
