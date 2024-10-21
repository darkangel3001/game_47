import sqlite3


# Функция для создания базы данных и таблицы products
def create_db():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    # Создание таблицы products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
        price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
        quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
    );
    ''')

    conn.commit()
    conn.close()


# Функция для добавления 15 товаров
def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ("Мыло жидкое", 50.0, 10),
        ("Мыло детское", 25.5, 30),
        ("Шампунь", 100.0, 20),
        ("Крем для рук", 120.0, 15),
        ("Гель для душа", 75.0, 50),
        ("Зубная паста", 40.0, 60),
        ("Маска для лица", 200.0, 5),
        ("Лосьон для тела", 150.0, 25),
        ("Дезодорант", 80.0, 40),
        ("Крем для лица", 300.0, 10),
        ("Пена для бритья", 90.0, 35),
        ("Масло для волос", 250.0, 12),
        ("Гель для бритья", 110.0, 22),
        ("Зубная щетка", 20.0, 100),
        ("Мочалка", 10.0, 150)
    ]

    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()


# Функция для изменения количества товара по id
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, product_id))

    conn.commit()
    conn.close()


# Функция для изменения цены товара по id
def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, product_id))

    conn.commit()
    conn.close()


# Функция для удаления товара по id
def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (product_id,))

    conn.commit()
    conn.close()


# Функция для вывода всех товаров
def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


# Функция для выбора товаров дешевле лимита и с количеством больше лимита
def get_products_under_price_limit(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


# Функция для поиска товаров по названию
def search_products_by_title(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


# Тестирование функций
if __name__ == "__main__":
    create_db()
    add_products()
    get_all_products()

    print("\nИзменение количества товара с id=1 на 50")
    update_quantity(1, 50)
    get_all_products()

    print("\nИзменение цены товара с id=2 на 55.0")
    update_price(2, 55.0)
    get_all_products()

    print("\nУдаление товара с id=3")
    delete_product(3)
    get_all_products()

    print("\nТовары дешевле 100 сом и с количеством больше 5")
    get_products_under_price_limit(100, 5)

    print("\nПоиск товаров по названию 'мыло'")
    search_products_by_title("мыло")