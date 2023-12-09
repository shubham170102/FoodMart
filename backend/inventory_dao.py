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
    connect.commit()


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
    # print(delete_from_inventory(connection, 17))
    updated_product_info = {
        'product_name': 'lemonade',
        'quantity_id': '4',
        'price_per_quantity': '3.00'
    }
    product_id_to_update = 26
    print(update_inventory(connection, product_id_to_update, updated_product_info))


# inventory_dao.py
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import create_engine, Column, Integer, String, Float
#
# # Set up the engine and session
# engine = create_engine('mysql+mysqlconnector://root:@localhost/grocery_store')
# Session = sessionmaker(bind=engine)
#
# Base = declarative_base()
#
#
# class Inventory(Base):
#     __tablename__ = 'inventory'
#     product_id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     quantity_id = Column(Integer)
#     price_per_quantity = Column(Float)
#
#     def serialize(self):
#         """Serialize the object into a dictionary."""
#         return {
#             'product_id': self.product_id,
#             'name': self.name,
#             'quantity_id': self.quantity_id,
#             'price_per_quantity': self.price_per_quantity
#         }
#
#
# # Create tables in the database
# Base.metadata.create_all(engine)
#
#
# def get_all_inventory():
#     """Get all items from the inventory."""
#     session = Session()
#     try:
#         inventory_items = session.query(Inventory).all()
#         return [item.serialize() for item in inventory_items]
#     finally:
#         session.close()
#
#
# def insert_new_inventory(product):
#     """Insert a new item into the inventory."""
#     session = Session()
#     try:
#         new_product = Inventory(name=product['product_name'],
#                                 quantity_id=product['quantity_id'],
#                                 price_per_quantity=product['price_per_quantity'])
#         session.add(new_product)
#         session.commit()
#         return new_product.product_id
#     finally:
#         session.close()
#
#
# def delete_from_inventory(product_id):
#     """Delete an item from the inventory."""
#     session = Session()
#     try:
#         product = session.query(Inventory).filter(Inventory.product_id == product_id).one()
#         session.delete(product)
#         session.commit()
#     finally:
#         session.close()
#
#
# def update_inventory(product_id, updated_product):
#     """Update an item in the inventory."""
#     session = Session()
#     try:
#         product = session.query(Inventory).filter(Inventory.product_id == product_id).one()
#         product.name = updated_product['product_name']
#         product.quantity_id = updated_product['quantity_id']
#         product.price_per_quantity = updated_product['price_per_quantity']
#         session.commit()
#     finally:
#         session.close()
#
#
# def main():
#     # Test for inserting a new inventory item
#     print("\nInserting a new inventory item...")
#     new_item_id = insert_new_inventory({
#         'product_name': 'Test Product',
#         'quantity_id': 1,
#         'price_per_quantity': 15.50
#     })
#     print(f"Inserted item with ID: {new_item_id}")
#
#     # Uncomment the following lines to test other operations
#     # # Test for updating an inventory item
#     # print("\nUpdating an inventory item...")
#     # update_inventory(new_item_id, {
#     #     'product_name': 'Updated Product',
#     #     'quantity_id': 2,
#     #     'price_per_quantity': 20.00
#     # })
#     # print(f"Updated item with ID: {new_item_id}")
#
#     # # Test for getting all inventory items again
#     # print("\nGetting all inventory items after update...")
#     # items = get_all_inventory()
#     # for item in items:
#     #     print(item)
#
#     # # Test for deleting an inventory item
#     # print("\nDeleting an inventory item...")
#     # delete_from_inventory(new_item_id)
#     # print(f"Deleted item with ID: {new_item_id}")
#
#     # # Final check for inventory
#     # print("\nFinal check for inventory items...")
#     # items = get_all_inventory()
#     # for item in items:
#     #     print(item)
#
#
# if __name__ == "__main__":
#     main()
