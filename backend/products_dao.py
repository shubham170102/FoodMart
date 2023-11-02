from connection import sql_connection


def insert_new_inventory(connect, product):
    cursor = connect.cursor()
    query = "INSERT INTO grocery_store.inventory (name, quantity_id, price_per_quantity) VALUES (%s, %s, %s)"
    data = (product['product_name'], product['quantity_id'], product['price_per_quantity'])
    cursor.execute(query, data)
    connect.commit()
    return cursor.lastrowid


def delete_from_inventory(connect, product_id):
    cursor = connect.cursor()
    query = ("DELETE FROM grocery_store.inventory WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()


def update_inventory(connect, product_id, updated_product):
    cursor = connect.cursor()
    query = """
    UPDATE grocery_store.inventory 
    SET 
        name = %s, 
        quantity_id = %s, 
        price_per_quantity = %s 
    WHERE 
        product_id = %s;
    """
    data = (updated_product['product_name'], updated_product['quantity_id'], updated_product['price_per_quantity'], product_id)

    cursor.execute(query, data)
    connect.commit()

    return cursor.rowcount


def get_all_inventory(connect):
    cursor = connect.cursor()

    query = (
        "SELECT inventory.product_id, inventory.name, inventory.quantity_id, inventory.price_per_quantity,"
        "quantity.quantity_name "
        "FROM grocery_store.inventory INNER JOIN grocery_store.quantity on inventory.quantity_id = "
        "quantity.quantity_id;")

    cursor.execute(query)

    result = []

    for (product_id, name, quantity_id, price_per_quantity, quantity_name) in cursor:
        result.append(
            {
                'product_id': product_id,
                'name': name,
                'quantity_id': quantity_id,
                'price_per_quantity': price_per_quantity,
                'quantity_name': quantity_name
            }
        )

    return result


if __name__ == '__main__':
    connection = sql_connection()
    # print(get_all_inventory(connection))
    # print(insert_new_inventory(connection, {
    #     'product_name': 'wipes',
    #     'quantity_id': '1',
    #     'price_per_quantity': '8.00'
    # }))
    # print(delete_from_inventory(connection, 14))
    updated_product_info = {
        'product_name': 'lemonade',
        'quantity_id': '4',
        'price_per_quantity': '3.00'
    }

    product_id_to_update = 6
    print(update_inventory(connection, product_id_to_update, updated_product_info))