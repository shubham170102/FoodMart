def get_all_quantity(connect):
    cursor = connect.cursor()
    query = ("SELECT * FROM grocery_store.quantity;")
    cursor.execute(query)
    result = []
    for (quantity_id, quantity_name) in cursor:
        result.append(
            {
                'quantity_id': quantity_id,
                'quantity_name': quantity_name,
            }
        )
    return result

if __name__ == '__main__':
    from connection import sql_connection
    connection = sql_connection()
    print(get_all_quantity(connection))