import mysql.connector
from mysql.connector import Error

__cnx = None


def sql_connection():
    global __cnx
    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(user='root', password='',
                                        host='localhost',
                                        database='grocery_store')
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            # Handle the error or re-raise
            raise
    return __cnx
