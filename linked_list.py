from collections import abc
from typing import Any


class Node:
    """
    Единица связанного списка - узел
    """
    def __init__(self, value: Any):
        self.next_node = None
        self.value = value

    def __eq__(self, other: 'Node') -> bool:
        return self.value == other.value

    def __repr__(self):
        return f"<Node: {self.value}>"


class ListNode:
    """
    Связанный список
    """
    def __init__(self, iterable: abc.Iterable = None):
        self._initialize_start_and_end(iterable=iterable)

    def _initialize_start_and_end(self, iterable: abc.Iterable) -> None:
        '''
        метод для создания связанного списка по итерируемому объекту
        '''
        if not iterable:
            self.start = None
            self.end = None
            return

        first_node = None
        for value in iterable:
            node = Node(value)
            try:
                first_node.next_node = node
                first_node = node
            except AttributeError:
                node = Node(value)
                first_node = node
                self.start = node

        self.end = node

    def __iter__(self):
        node = self.start
        while node:
            yield node
            node = node.next_node

    def __contains__(self, value: Any) -> bool:
        if not self.start:
            return False
        for node in self:
            if node.value == value:
                return True
        return False

    def __getitem__(self, index: int) -> Node:
        start_index = 0
        node = self.start
        while start_index < index:
            try:
                node = node.next_node
            except AttributeError:
                raise IndexError('ListNode index out of range')
            start_index += 1
        return node

    def remove(self, index: int) -> None:
        '''
        удаление node по индексу index 
        '''
        prev_node = self[index - 1]
        prev_node.next_node = prev_node.next_node.next_node

    def insert(self, value: Any, index: int) -> None:
        '''
        вставка node по индексу index 
        '''
        node = Node(value)
        prev_node = self[index - 1]
        node.next_node = prev_node.next_node
        prev_node.next_node = node

    def __len__(self) -> int:
        node = self.start
        if not node:
            return 0
        count = 0
        while node:
            count += 1
            node = node.next_node
        return count

    def append(self, value: Any) -> None:
        '''
        добавление в конец 
        '''
        node = Node(value)
        if not self.start:
            self.start = node
            self.end = node
            return
        self.end.next_node = node
        self.end = node

    def reverse(self) -> None:
        '''
        Перевернуть связанный список 
        '''
        prev = None
        node = self.start
        self.end = node
        while node:
            next_node = node.next_node
            node.next_node = prev
            prev = node
            node = next_node
        self.start = prev

    def popleft(self) -> Node:
        '''
        удалить node сначала и вернуть его 
        '''
        start_node = self.start
        self.start = self.start.next_node
        return start_node
