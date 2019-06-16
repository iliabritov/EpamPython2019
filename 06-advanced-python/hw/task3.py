"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""
import string


class ShiftDescriptor:

    def __init__(self, shift):
        self.shift = shift
        self.result = None
        self.translate_table = {x:y for x, y in zip(string.ascii_lowercase,
        list(string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]))}
    
    def __get__(self, instance, owner):
        return self.result

    def __set__(self, instance, value):
        self.result = ''.join([self.translate_table[i] for i in value])


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


if __name__ == '__main__':
    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    assert a.message == 'efg'
    assert a.another_message == 'olssv'
