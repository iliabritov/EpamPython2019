from datetime import datetime, timedelta
from collections import defaultdict


class Homework():

    def __init__(self, text, number_of_days):
        self.text = text
        self.deadline = timedelta(days=number_of_days)
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.now()


class Person():

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError('You are late')


class Teacher(Person):
    homework_done = defaultdict(dict)

    @staticmethod
    def create_homework(text, days):
        return Homework(text, days)

    @classmethod
    def check_homework(cls, hw_result):
        solution = hw_result.solution
        if len(solution) > 5 and hw_result.solution not in cls.homework_done:
            cls.homework_done[hw_result.homework][hw_result.solution] = hw_result
            return True
        return False

    @classmethod
    def reset_results(cls, hw=None):
        if hw:
            del cls.homework_done[hw]
        else:
            cls.homework_done = {}


class HomeworkResult():

    def __init__(self, autor, homework, solution):
        self.autor = autor
        self.homework = homework
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.solution = solution
        self.created = datetime.now()


class DeadlineError(Exception):
    """This homework not active"""


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
