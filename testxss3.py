#testxss3.py
import os
from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

#based
@app.route('/h2')
def hello_ssti():
	person = {'name':"world", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
	# if request.args.get('name'):
	# 	person['name'] = request.args.get('name')
	t = request.args.get('name')
	template = '''<h2>Hello %s!</h2>''' % t
	return render_template_string(template, person=person)


if __name__ == "__main__":
	app.run(debug=False, port=4996)
