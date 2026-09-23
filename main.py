from flask import Flask
app = Flask(__name__)
app.route('/')
def home():
	return "Hello world from render !"
if __name__=="__main__":
	app.run(debug=True)

