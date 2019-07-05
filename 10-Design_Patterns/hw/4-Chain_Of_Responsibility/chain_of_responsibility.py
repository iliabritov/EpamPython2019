"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""

class Fridge():
    def __init__(self, content_list):
        self.content_list = content_list


class BaseCheck():
    def set_next(self, handle):
        self.next_check = handle

    def handle(self, fridge):
        pass


class Check_eggs(BaseCheck):
    def handle(self, fridge):
        ingr = 'eggs'
        if fridge.content_list[ingr] < 2:
            shopping_list[ingr] = 2 - fridge.content_list[ingr]
        self.next_check.handle(fridge)


class Check_milk(BaseCheck):
    def handle(self, fridge):
        ingr = 'milk'
        if fridge.content_list[ingr] < 0.5:
            shopping_list[ingr] = 0.5 - fridge.content_list[ingr]
        self.next_check.handle(fridge)


class Check_oil(BaseCheck):
    def handle(self, fridge):
        ingr = 'oil'
        if fridge.content_list[ingr] < 10:
            shopping_list[ingr] = 10 - fridge.content_list[ingr]
        self.next_check.handle(fridge)


class Check_butter(BaseCheck):
    def handle(self, fridge):
        ingr = 'butter'
        if fridge.content_list[ingr] < 120:
            shopping_list[ingr] = 120 - fridge.content_list[ingr]
        self.next_check.handle(fridge)


class Check_flour(BaseCheck):
    def handle(self, fridge):
        ingr = 'flour'
        if fridge.content_list[ingr] < 300:
            shopping_list[ingr] = 300 - fridge.content_list[ingr]
        self.next_check.handle(fridge)


class Check_sugar(BaseCheck):
    def handle(self, fridge):
        ingr = 'sugar'
        if fridge.content_list[ingr] < 100:
            shopping_list[ingr] = 100 - fridge.content_list[ingr]


if __name__ == '__main__':
    shopping_list = {}
    fridge_list = {'eggs':3, 'milk':0, 'oil': 100,
                   'butter': 50, 'flour': 200, 'sugar': 250}
    fridge = Fridge(fridge_list)
    check1 = Check_eggs()
    check2 = Check_milk()
    check3 = Check_oil()
    check4 = Check_butter()
    check5 = Check_flour()
    check6 = Check_sugar()

    check1.set_next(check2)
    check2.set_next(check3)
    check3.set_next(check4)
    check4.set_next(check5)
    check5.set_next(check6)

    check1.handle(fridge)

    if shopping_list:
        print('Shopping list:')
        for elem in shopping_list:
            print(f'{elem} - {shopping_list[elem]}')
    else:
        print('It\'s time to cook!')
