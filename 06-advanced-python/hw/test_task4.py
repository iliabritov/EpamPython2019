import os
import pytest

from tasks.task1 import PrintableFile, PrintableFolder
from tasks.task2 import Graph
from tasks.task3 import CeasarSipher


# task1
@pytest.fixture()
def task1_contains_method_case_preparing():
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
def test_task1_str_method(path, expected):
    """testing __str__ method in task1"""
    content = os.listdir(path)
    folders = [elem for elem in content
               if os.path.isdir(os.path.join(path, elem))]
    files = [elem for elem in content
             if not os.path.isdir(os.path.join(path, elem))]
    result = str(PrintableFolder(os.path.basename(path),
                                 (path, folders, files)))
    assert result == expected


def test_task1_contains_method(task1_contains_method_case_preparing):
    """testing __contains__ method in task1"""
    for folder, file in task1_contains_method_case_preparing:
        assert (file in folder) == True

# task2
@pytest.mark.parametrize('graph, expected', [
    ({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}, 'ABCD'),
    ({'A': ['B', 'D'], 'B': ['C'], 'C': ['H'], 'D': ['A'], 'H': []}, 'ABDCH'),
    ({'A': ['B'], 'B': ['C'], 'C': ['H', 'N'], 'D': ['A'], 'H': ['D'], 'N': []}, 'ABCHND')
])
def test_graph_iteration(graph, expected):
    """test task2 based on parametrize"""
    assert ''.join([element for element in Graph(graph)]) == expected


# task3
@pytest.fixture()
def ceasar_obj():
    """prepare data for testing task3"""
    obj = CeasarSipher()
    obj.message = 'qwe'
    obj.another_message = 'hello'
    return obj


def test_caesar_descriptor(ceasar_obj):
    """testing task3"""
    assert ceasar_obj.message == 'uai'
    assert ceasar_obj.another_message == 'olssv'
