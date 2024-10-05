class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marriage_status = "женат" if self.is_married else "не женат"
        print(f"Меня зовут {self.fullname}, мне {self.age} лет, я {marriage_status}.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks)
        return 0


class Teacher(Person):
    base_salary = 50000  # Пример базовой зарплаты

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = 0.05 * max(0, self.experience - 3)
        return self.base_salary * (1 + bonus)


def create_students():
    students = [
        Student("Иван Иванов", 16, False, {"Математика": 5, "Физика": 4, "Химия": 3}),
        Student("Алексей Попов", 17, False, {"Математика": 4, "Физика": 5, "Химия": 4}),
        Student("Сергей Смирнов", 15, False, {"Математика": 3, "Физика": 2, "Химия": 4}),
    ]
    return students


# Создание объекта учителя
teacher = Teacher("Александр Васильев", 40, True, 6)
print("Информация о учителе:")
teacher.introduce_myself()
print(f"Зарплата: {teacher.calculate_salary()}")

# Создание учеников и вывод их информации
students = create_students()
for student in students:
    print("\nИнформация о студенте:")
    student.introduce_myself()
    print(f"Оценки: {student.marks}")
    print(f"Средняя оценка: {student.average_mark():.2f}")
