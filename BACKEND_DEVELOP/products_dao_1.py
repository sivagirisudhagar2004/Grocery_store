import mysql.connector
def get_all_products():
    cnx = mysql.connector.connect(user = "root",password = '9076',host = '127.0.0.1',database = "grocery_store")

    cursor = cnx.cursor()

    query = ("""
        SELECT p.product_id,p.name,p.uom_id,p.price_per_unit,u.uom_name
            FROM products AS p 
            INNER JOIN uom AS u ON p.uom_id = u.uom_id
    """)

    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()

    for(product_id, name, uom_id, price_per_unit,uom_name) in cursor:
        print(product_id, name, uom_id, price_per_unit,uom_name)


if(__name__ == "__main__"):
    
    print(get_all_products())
"""""
if(__name__ == "__main__"):
    connection = get_sql_connection()
    print(get_all_products(connection))

if(__name__ == "__main__"):
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        "name" : "potatoes",
        "uom_id" : "1",
        "price_per_unit" : "10"
    }))

"""""