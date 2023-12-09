from connection import sql_connection
from datetime import datetime


def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = "INSERT INTO grocery_store.orders (customer_name, total_price, timestamp) VALUES (%s, %s, %s)"
    order_data = (order['customer_name'], order['total_price'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid
    order_details_query = "INSERT INTO grocery_store.orderInfo (order_id, product_id, quantity, total) VALUES (%s, %s, %s, %s) "
    order_detail_data = []
    for order_detail_record in order['order_details']:
        order_detail_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total'])
        ])

    cursor.executemany(order_details_query, order_detail_data)
    connection.commit()
    return order_id


if __name__ == '__main__':
    connection = sql_connection()
    print(insert_order(connection, {
        'customer_name': 'Shubham',
        'total_price': '501',
        'order_details': [
            {
                'product_id': 3,
                'quantity': 2,
                'total': 50
            },
            {
                'product_id': 21,
                'quantity': 6,
                'total': 30
            }

        ]
    }))
