class Node(object):
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    """ LinkedList или связный список – это структура данных.
    Связный список обеспечивает возможность создать двунаправленную очередь из каких-либо элементов.
    Каждый элемент такого списка считается узлом.
    По факту в узле есть его значение, а также две ссылки – на предыдущий и на последующий узлы.
    То есть список «связывается» узлами, которые помогают двигаться вверх или вниз по списку.
    Из-за таких особенностей строения из связного списка можно организовать стек, очередь или двойную очередь."""

    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def list_print(self):
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next


ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()
