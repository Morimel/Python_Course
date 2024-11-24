import sqlite3

products_list = [
    ('Snickers', 60, 10),
    ('Mars', 50, 15),
    ('Bounty', 55, 20),
    ('KitKat', 45, 25),
    ('Twix', 40, 30),
    ('Milky Way', 35, 5),
    ('Alpen Gold', 70, 12),
    ('Ritter Sport', 85, 8),
    ('Ferrero Rocher', 200, 5),
    ('Lindt', 150, 6),
    ('Hershey\'s', 90, 14),
    ('Milka', 95, 18),
    ('Toblerone', 120, 10),
    ('Kinder Bueno', 75, 11),
    ('Oreo', 60, 15)
]


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_product(db_name, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as error:
        print(error)


def search_products_by_name(db_name, search_term):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (f"%{search_term}%",))
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as error:
        print(error)
        return []


def update_product(db_name, product_id, updated_values):
    sql = '''UPDATE products 
    SET product_title = ?, price = ?, quantity = ? 
    WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (*updated_values, product_id))
            connection.commit()
            print(f"Product with ID {product_id} updated successfully.")
    except sqlite3.Error as error:
        print(error)


def delete_product(db_name, product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_id,))
            connection.commit()
            print(f"Product with ID {product_id} deleted successfully.")
    except sqlite3.Error as error:
        print(error)


def fetch_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as error:
        print(error)
        return []


def insert_multiple_products(db_name, products):
    sql = '''INSERT INTO products 
    (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, products)
            connection.commit()
            print(f"{len(products)} products were successfully added to the database.")
    except sqlite3.Error as error:
        print(error)


sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

database_name = 'hw.db'
my_connection = create_connection(database_name)

if my_connection is not None:
    print('Connection established')

    insert_multiple_products(database_name, products_list)

    create_table(my_connection, sql_to_create_products_table)

    insert_product(database_name, ('Snickers', 60, 10))

    update_product(database_name, 1, ('Mars', 50, 15))

    delete_product(database_name, 2)

    search_term = "Мыло"
    found_products = search_products_by_name(database_name, search_term)
    print(f"Products matching '{search_term}':")
    for product in found_products:
        print(product)

    products = fetch_all_products(database_name)
    print("Products in the database:")
    for product in products:
        print(product)

    my_connection.close()
