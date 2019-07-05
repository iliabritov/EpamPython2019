"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""

import yaml
import io

from abc import ABC, abstractmethod


# Factories
class AbstractMenuFactory(ABC):

    def __init__(self, week_day):
        self.week_day = week_day

    @abstractmethod
    def create_first_courses(self, menu):
        pass

    @abstractmethod
    def create_second_courses(self, menu):
        pass

    @abstractmethod
    def create_drinks(self, menu):
        pass


class VeganMenuFactory(AbstractMenuFactory):

    def create_first_courses(self, menu):
        position = menu[self.week_day]['first_courses']['vegan']
        return VeganFirstCourses(position)

    def create_second_courses(self, menu):
        position = menu[self.week_day]['second_courses']['vegan']
        return VeganSecondCourses(position)

    def create_drinks(self, menu):
        position = menu[self.week_day]['drinks']['vegan']
        return VeganDrinks(position)


class ChildMenuFactory(AbstractMenuFactory):

    def create_first_courses(self, menu):
        position = menu[self.week_day]['first_courses']['child']
        return ChildFirstCourses(position)

    def create_second_courses(self, menu):
        position = menu[self.week_day]['second_courses']['child']
        return ChildSecondCourses(position)

    def create_drinks(self, menu):
        position = menu[self.week_day]['drinks']['child']
        return ChildDrinks(position)


class ChinaMenuFactory(AbstractMenuFactory):

    def create_first_courses(self, menu):
        position = menu[self.week_day]['first_courses']['china']
        return ChinaFirstCourses(position)

    def create_second_courses(self, menu):
        position = menu[self.week_day]['second_courses']['china']
        return ChinaSecondCourses(position)

    def create_drinks(self, menu):
        position = menu[self.week_day]['drinks']['china']
        return ChinaDrinks(position)


# FirstCourses
class AbstractFirstCourses(ABC):

    def __init__(self, position_name):
        self.position_name = position_name

    def __str__(self):
        return f'Has been added first course - {self.position_name}'

class VeganFirstCourses(AbstractFirstCourses):
    pass


class ChildFirstCourses(AbstractFirstCourses):
    pass


class ChinaFirstCourses(AbstractFirstCourses):
    pass


# SecondCourses
class AbstractSecondCourses(ABC):

    def __init__(self, position_name):
        self.position_name = position_name

    def __str__(self):
        return f'Has been added second course - {self.position_name}'


class VeganSecondCourses(AbstractSecondCourses):
    pass


class ChildSecondCourses(AbstractSecondCourses):
    pass


class ChinaSecondCourses(AbstractSecondCourses):
    pass


# Drinks
class AbstractDrinks(ABC):

    def __init__(self, position_name):
        self.position_name = position_name

    def __str__(self):
        return f'Has been added drink- {self.position_name}'



class VeganDrinks(AbstractDrinks):
    pass


class ChildDrinks(AbstractDrinks):
    pass


class ChinaDrinks(AbstractDrinks):
    pass


def make_order(type, day):
    order = []
    process = lunch_type[type](day)
    order.append(process.create_first_courses(menu))
    order.append(process.create_second_courses(menu))
    order.append(process.create_drinks(menu))
    return order

if __name__ == '__main__':
    day_list = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    lunch_type = {'vegan': VeganMenuFactory, 'child': ChildMenuFactory,
                  'china': ChinaMenuFactory}

    with io.open('menu.yml', 'r', encoding='utf-8') as file:
        menu = yaml.safe_load(file)

    order_visitor = make_order(input('What lunch you want: '), day_list[3])
    for element in order_visitor:
        print (element)
