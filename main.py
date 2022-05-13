from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sgs/inactives')
def sgs_inatives():
    return jsonify(test = 'testing')