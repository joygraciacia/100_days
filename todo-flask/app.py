from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route("/<name>")
def hello_name(name):
	return "Hello " + name


if __name__ == "__main__":        # on running python app.py
	Schema()
    app.run(debug=True)  		  # run flask app