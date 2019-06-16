"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""


import os


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        
        def func(path, count=0):
            result = ['V ' + os.path.basename(path)]
            content = os.listdir(path)
            folders = [elem for elem in content
                       if os.path.isdir(os.path.join(path, elem))]
            files = [elem for elem in content
                     if not os.path.isdir(os.path.join(path, elem))]
            st = '|   ' * count 
            for fold in folders:
                result.append(st + '|-> ' + func(os.path.join(path,
                                                    fold), count=count+1))
            for file in files:
                result.append(st + str(PrintableFile(file)))        
            return '\n'.join(result)
        
        curr_path = self.content[0]
        result = func(curr_path)   
        return result

    def __contains__(self, item):
        return [file for file in self.content[2] if file == item.name]


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '|-> ' + self.name

if __name__ == '__main__':
    test = PrintableFolder('test', ('test',
                            ['test_fold1', 'test_fold2'], ['123.txt']))
    test_fold1 = PrintableFolder('test_fold1',
                             ('test\\test_fold1', ['test_sub'], ['312.txt']))
    file1 = PrintableFile('123.txt')
    file2 = PrintableFile('333.txt')

    print(test)
    print()
    print(test_fold1)
    print(file1 in test)
    print(file2 in test)

