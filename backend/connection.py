import mysql.connector

__cnx = None


def sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='',
                                        host='localhost',
                                        database='grocery_store')
    return __cnx
