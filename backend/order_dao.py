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

def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM grocery_store.orders"
    cursor.execute(query)

    response = []
    for (order_id, customer_name, total_price, timestamp) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total_price': total_price,
            'timestamp': timestamp
        })

    return response

# Queries for building report

def get_total_sales_per_day(connection):
    cursor = connection.cursor()
    query = """
    SELECT DATE(timestamp) as date, SUM(total_price) as total_sales FROM grocery_store.orders GROUP BY DATE(timestamp);
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_top_selling_products(connection):
    cursor = connection.cursor()
    query = """
    SELECT p.name, COUNT(*) as total_orders
    FROM grocery_store.orderInfo od
    JOIN grocery_store.inventory p ON od.product_id = p.product_id
    GROUP BY p.product_id
    ORDER BY total_orders DESC
    LIMIT 10;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def get_average_order_value(connection):
    cursor = connection.cursor()
    query = """
    SELECT AVG(total_price) as avg_order_value
    FROM grocery_store.orders;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result


if __name__ == '__main__':
    connection = sql_connection()
    print(get_all_orders(connection))
    print(get_total_sales_per_day(connection))
    print(get_average_order_value(connection))
    print(get_top_selling_products(connection))

