# Test sending data;
# curl -X POST -H "Content-Type: application/json" -d '{"server": "node4", "data": ["data1", "data2", "data3"]}' http://localhost:5000/api/data
# Test getting all data;
# curl http://localhost:5000/api/data
# Test getting specific node data
# curl http://localhost:5000/data?server=node1

from db_coms import insert_data
from db_coms import extract_data
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_data():
    json_data = request.get_json()
    server_name = json_data['server']
    data_array = json_data['data']
    
    # Call the Python script to insert data into the database
    insert_data(server_name, data_array)

    return 'Data inserted successfully!'

@app.route('/api/data')
def get_data():
    server_name = request.args.get('server')

    data = extract_data(server_name) 
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)