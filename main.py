from flask import flask
app = flask(__name__)
app.route('/')
	return "Hello world from render !"
if __name__="__main__":
	app.run(debug=True)

