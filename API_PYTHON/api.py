import pandas as pd
from flask import Flask, jsonify 

app = Flask(__name__)

# build functionality
@app.route('/')
def homepage():
    return('Starting API.')

@app.route('/sales')
def sales(): 
    worksheet = pd.read_csv('advertising.csv')
    sales_amount = worksheet['Sales'.sum()]
    resp = {'sales_amount' + sales_amount}
    return jsonify(resp)

# loading api
app.run(host='0.0.0.0')