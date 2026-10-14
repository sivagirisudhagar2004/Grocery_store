from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor(dictionary = True)

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

        response = []

    for (product_id, name, uom_id, price_per_unit,uom_name) in cursor:

        response.append(
        {
            "product":product_id,

            "name":name,

            "uom_id":uom_id,

            "price_per_unit":price_per_unit,

            "uom_name":uom_name
        }
    )

    return response

def insert_new_product(connection,product):

    name = (product.get("name") or "").strip()

    uom_raw = product.get("uom_id")

    price_raw = product.get("price_per_unit")

    if(not name):

        raise ValueError("Product name is required")
    
    if(uom_raw in(None,"")):

        raise ValueError("Unit of measure is required")
    
    if(price_raw in (None,"")):

        raise ValueError("Price is required")

    try:
        uom_id = int(uom_raw)

        price = float(price_raw)
        
    except(TypeError,ValueError):

        raise ValueError("uom_id must be an integer and price_per_unit a number")
    
    cursor = connection.cursor()

    query = ("""
        INSERT INTO products (name , uom_id, price_per_unit)
        VALUES (%s, %s, %s)
    """)

    data = (product['product_name'],product['uom_id'],product['price_per_unit'])

    cursor.execute(query,data)

    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):

    cursor = connection.cursor()

    query = ("DELETE FROM products WHERE product_id=" + str(product_id))

    cursor.execute(query)

    connection.commit()
    
if(__name__ == "__main__"):

    connection = get_sql_connection()

    print(delete_product(connection,5))