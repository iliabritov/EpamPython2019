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

    def __init__(self):
        self.shopping_count = 0
    
    def set_next(self, handle):
        self.next_check = handle

    def handle(self, fridge):
        pass


class CheckEggs(BaseCheck):
    def handle(self, fridge):
        self.ingr = 'eggs'
        if fridge.content_list[self.ingr] < 2:
            self.shopping_count = 2 - fridge.content_list[self.ingr]
        self.next_check.handle(fridge)


class CheckMilk(BaseCheck):
    def handle(self, fridge):
        self.ingr = 'milk'
        if fridge.content_list[self.ingr] < 0.5:
            self.shopping_count = 0.5 - fridge.content_list[self.ingr]
        self.next_check.handle(fridge)


class CheckOil(BaseCheck):
    def handle(self, fridge):
        self.ingr = 'oil'
        if fridge.content_list[self.ingr] < 10:
            self.shopping_count = 10 - fridge.content_list[self.ingr]
        self.next_check.handle(fridge)


class CheckButter(BaseCheck):
    def handle(self, fridge):
        self.ingr = 'butter'
        if fridge.content_list[self.ingr] < 120:
            self.shopping_count = 120 - fridge.content_list[self.ingr]
        self.next_check.handle(fridge)


class CheckFlour(BaseCheck):
    def handle(self, fridge):
        self.ingr = 'flour'
        if fridge.content_list[self.ingr] < 300:
            self.shopping_count = 300 - fridge.content_list[self.ingr]
        self.next_check.handle(fridge)


class CheckSugar(BaseCheck):
    def handle(self, fridge):
        self.ingr = 'sugar'
        if fridge.content_list[self.ingr] < 100:
            self.shopping_count = 100 - fridge.content_list[self.ingr]


if __name__ == '__main__':
    #shopping_list = {}
    fridge_list = {'eggs':3, 'milk':0, 'oil': 100,
                   'butter': 50, 'flour': 200, 'sugar': 250}
    fridge = Fridge(fridge_list)
    check1 = CheckEggs()
    check2 = CheckMilk()
    check3 = CheckOil()
    check4 = CheckButter()
    check5 = CheckFlour()
    check6 = CheckSugar()

    check1.set_next(check2)
    check2.set_next(check3)
    check3.set_next(check4)
    check4.set_next(check5)
    check5.set_next(check6)

    check_list = [check1, check2, check3,
                  check4, check5, check6]
    
    check1.handle(fridge)

    for check in check_list:
        if check.shopping_count:
            print(f'{check.ingr} - {check.shopping_count}')
    else:
        print('It\'s time to cook!')
