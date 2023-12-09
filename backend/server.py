from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import inventory_dao
import quantity_dao
from connection import sql_connection

app = Flask(__name__)
CORS(app)
connection = sql_connection()

@app.route('/getInventory', methods=['GET'])
def get_inventory():
    result = inventory_dao.get_all_inventory(connection)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteFromInventory', methods=['POST'])
def delete_from_inventory():
    result = inventory_dao.delete_from_inventory(connection, request.form['product_id'])
    response = jsonify({
        'product_id': result
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getQuantity', methods=['GET'])
def get_quantity():
    result = quantity_dao.get_all_quantity(connection)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/addToInventory', methods=['POST'])
def add_product():
    data = json.loads(request.form['data'])
    product_id = inventory_dao.insert_new_inventory(connection, data)
    result = jsonify({
        'product_id': product_id
    })
    result.headers.add('Access-Control-Allow-Origin', '*')
    return result

@app.route('/updateInventory/<int:product_id>', methods=['PUT'])
def update_inventory(product_id):
    data = json.loads(request.form['data'])
    updated = inventory_dao.update_inventory(connection, product_id, data)
    if updated:
        return jsonify({'status': 'success', 'product_id': product_id})
    else:
        return jsonify({'status': 'error', 'message': 'Update failed'}), 400


if __name__ == '__main__':
    print("Starting Flask")
    app.run(port=5000)