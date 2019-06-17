import os
import pytest

from tasks.task1 import PrintableFile, PrintableFolder
from tasks.task2 import Graph
from tasks.task3 import CeasarSipher


# task1
@pytest.fixture()
def task1_case_preparing():
    """Preparing data for testing __contains__ method in task1"""
    result = []
    for path, folders, files in os.walk('test_folder'):
        if files:
            folder = PrintableFolder(os.path.basename(path), [path, folders, files])
            file = PrintableFile(files[0])
            result.append([folder, file])
    return result


@pytest.mark.parametrize('path, expected', [
    ('test_folder', """V test_folder\n|-> V test_fold1\n|   |-> V test_sub\n|   |   |-> finish.txt\n|   |-> 312.txt\n|-> V test_fold2\n|   |-> V test_sb\n|   |-> 333.txt\n|   |-> 444.txt\n|-> 123.txt"""),
    ('test_folder\\test_fold1' , """V test_fold1\n|-> V test_sub\n|   |-> finish.txt\n|-> 312.txt""")
])
def test_task1_num1(path, expected):
    """testing __str__ method in task1"""
    content = os.listdir(path)
    folders = [elem for elem in content
               if os.path.isdir(os.path.join(path, elem))]
    files = [elem for elem in content
             if not os.path.isdir(os.path.join(path, elem))]
    result = str(PrintableFolder(os.path.basename(path),
                                 (path, folders, files)))
    assert result == expected


def test_task1_num2(task1_case_preparing):
    """testing __contains__ method in task1"""
    for folder, file in task1_case_preparing:
        assert (file in folder) == True

# task2
@pytest.mark.parametrize('graph, expected', [
    ({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}, 'ABCD'),
    ({'A': ['B', 'D'], 'B': ['C'], 'C': ['H'], 'D': ['A'], 'H': []}, 'ABDCH'),
    ({'A': ['B'], 'B': ['C'], 'C': ['H', 'N'], 'D': ['A'], 'H': ['D'], 'N': []}, 'ABCHND')
])
def test_task2(graph, expected):
    """test task2 based on parametrize"""
    assert ''.join([element for element in Graph(graph)]) == expected


# task3
@pytest.fixture()
def ceasarObj():
    """prepare data for testing task3"""
    obj = CeasarSipher()
    obj.message = 'qwe'
    obj.another_message = 'hello'
    return obj


def test_task3(ceasarObj):
    """testing task3"""
    assert ceasarObj.message == 'uai'
    assert ceasarObj.another_message == 'olssv'
