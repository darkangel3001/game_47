import sqlite3


def show_students_by_city(city_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    """, (city_id,))

    students = cursor.fetchall()
    if students:
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Ученики не найдены в выбранном городе.")

    conn.close()


def main():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Выводим список городов
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    while True:
        try:
            city_id = int(input("Введите id города: "))
            if city_id == 0:
                print("Выход из программы.")
                break
            show_students_by_city(city_id)
        except ValueError:
            print("Пожалуйста, введите корректный id города.")

    conn.close()


if __name__ == "__main__":
    main()