# 13
#Классы «ПЕРСОНА», «АБИТУРИЕНТ», «СТУДЕНТ»,
#«ПРЕПОДАВАТЕЛЬ» Класс ПЕРСОНА, экземпляр класса
#инициализируется аргументами фамилия, дата рождения и содержит
#методы, позволяющие вывести информацию о персоне, а также определить
#ее возраст. Дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения,
#факультет), СТУДЕНТ(фамилия, дата рождения, факультет, курс),
#ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность,
#стаж), содержат свои методы вывода информации. Создайте список из n
#персон, выведите полную информацию из базы, а также организуйте поиск
#персон, чей возраст попадает в заданный диапазон.
import datetime
class Persona:
    def __init__(self, surname, birthday):
        self.surname = surname
        self.birthday = birthday
    def info(self):
        print(f'Фамилия: {self.surname}')
        print(f'Дата рождения: {self.birthday}')
        print(f'возраст: {self.get_age()}')
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1
        return age
class Abiturient(Persona):
    def __init__(self, surname, birthdate, faculty):
        super().__init__(surname, birthdate)
        self.faculty = faculty
    def info(self):
        super().info()
        print(f'Факультет: {self.faculty}')

class Student(Persona):
    def __init__(self, surname, birthdate, faculty, course):
        super().__init__(surname, birthdate)
        self.faculty = faculty
        self.course = course

    def info(self):
        super().info()
        print(f"Факультет: {self.faculty}")
        print(f"Курс: {self.course}")
class Teacher(Persona):
    def __init__(self, surname, birthdate, faculty, position, experience):
        super().__init__(surname, birthdate)
        self.faculty = faculty
        self.position = position
        self.experience = experience
    def info(self):
        super().info()
        print(f"Факультет: {self.faculty}")
        print(f"Должность: {self.position}")
        print(f"Опыт: {self.experience}")
people = [
    Abiturient("Nartov", datetime.date(2006, 5, 23), "Python"),
    Student("Krdyan", datetime.date(2005, 6, 12), "Physics", 1),
    Teacher("Babchenock", datetime.date(1998, 3, 3), "Programming", "Prepodavatel", 2)
]
for person in people:
    person.info()

age_min = 15
age_max = 28
for person in people:
    age = person.get_age()
    if age >= age_min and age <= age_max:
        person.info()