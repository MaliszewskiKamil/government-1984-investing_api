import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

buys = [
  {
  'id': 0,
  'stock': "APC"
  }
]

@app.route('/', methods=['GET'])
def home():
	return "<h1>xD</h1>"

@app.route('/another/', methods=['GET'])
def another():
	return "<h1>HAHA</h1>"

@app.route('/api/v1/resources/buys/all')
def allBuys():
  return jsonify(buys)
	


app.run()
