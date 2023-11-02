from flask import Flask, request, jsonify
import products_dao
from connection import sql_connection

app = Flask(__name__)

connection = sql_connection()


@app.route('/getInventory', methods=['GET'])
def get_inventory():
    result = products_dao.get_all_inventory(connection)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteFromInventory', methods=['POST'])
def delete_from_inventory():
    result = products_dao.delete_from_inventory(connection, request.form['product_id'])
    response = jsonify({
        'product_id': result
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Flask")
    app.run(port=5000)
