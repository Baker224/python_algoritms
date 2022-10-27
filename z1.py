"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def haff_tree(node, code=""):
    if isinstance(node, str):
        return {node: code}
    l, r = node.children()
    result = {}
    result.update(haff_tree(l, code + "0"))
    result.update(haff_tree(r, code + "1"))
    return result


def coding_string(orig):
    frequencies = {}
    for char in orig:
        if char not in frequencies:
            frequencies[char] = 0

        frequencies[char] += 1

    tree = frequencies.items()

    while len(tree) > 1:
        tree = sorted(tree, reverse=True, key=lambda x: x[1])
        char1, count1 = tree[-1]
        char2, count2 = tree[-2]
        tree = tree[:-2]
        tree.append((Node(char1, char2), count1 + count2))

    code_table = haff_tree(tree[0][0])

    coded = []
    for char in orig:
        coded.append(code_table[char])
    return print(f"Закодированная строка: {''.join(coded)}")


orig_string = "I like beer!"
print("Исходная строка: " + orig_string)
coding_string(orig_string)

