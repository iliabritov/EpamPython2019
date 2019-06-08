from datetime import datetime, timedelta


class Homework():
    
    def __init__(self, text, number_of_days):
        self.text = text
        self.deadline = timedelta(days=number_of_days)
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.now()

    
class Student():

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework):
        if homework.is_active():
            return homework
        print('You are late')


class Teacher():
    
    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, days):
        return Homework(text, days)
    

if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
