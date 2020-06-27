from flask import Flask 
from models import Schema 
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hi(name):
    return "Hi " + name

if __name__ == "__main__":
	Schema()
	app.run(debug=True)

# Also need a primary key
# Create an item (title - text, description - text, createdon - date, duedate - date)
# Delete an item (is_deleted - boolean)
# Mark an item done (is_done - boolean)
# Update an item (update? )