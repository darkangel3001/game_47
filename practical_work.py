import sqlite3


def connect_db():
    # Подключение к базе данных SQLite
    conn = sqlite3.connect('database.db.')  # Убедитесь, что database.db находится в корневой папке проекта
    return conn


def get_stores(conn):
    # Получение списка магазинов из базы данных
    cursor = conn.cursor()
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    return stores


def get_products_by_store(conn, store_id):
    # Получение продуктов из выбранного магазина
    cursor = conn.cursor()
    query = """
    SELECT p.title, c.title AS category, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()
    return products


def display_stores(stores):
    # Отображение списка магазинов
    print(
        "Вы можете отобразить список продуктов по выбранному из магазина из перечня магазинов ниже, для выхода из программы введите цифру 0")
    for store in stores:
        print(f"{store[0]}. {store[1]}")


def display_products(products):
    # Отображение информации о продуктах
    if not products:
        print("Продукты для выбранного магазина не найдены.")
    else:
        for product in products:
            print(f"\nНазвание продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")


def main():
    conn = connect_db()
    stores = get_stores(conn)

    while True:
        display_stores(stores)
        choice = input("\nВведите id магазина или 0 для выхода: ")

        if choice == '0':
            print("Выход из программы.")
            break

        try:
            store_id = int(choice)
            products = get_products_by_store(conn, store_id)
            display_products(products)
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректный id магазина.")

    conn.close()


if __name__ == "__main__":
    main()