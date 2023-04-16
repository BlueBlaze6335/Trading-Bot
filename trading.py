import pandas as pd
from flask import Flask, jsonify


data = pd.ExcelFile("OC (1).xlsx")
data = pd.read_excel(data, 'Sheet4')
json_data = data.to_json(orient='records')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)