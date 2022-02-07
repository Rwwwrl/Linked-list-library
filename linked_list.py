class Node:
    """
    Единица связанного списка - узел
    """

    def __init__(self, value):
        self.next_node = None
        self.value = value

    def __repr__(self):
        return f"<Node: {self.value}>"


class ListNode:
    """
    Связанный список
    """
    __slots__ = ('start', 'end')

    def __init__(self):
        # start - указатель на самый первый узел списка
        self.start = None
        self.end = None

    def __iter__(self):
        node = self.start
        while node:
            yield node
            node = node.next_node

    def __contains__(self, value) -> bool:
        if not self.start:
            return False
        for node in self:
            if node.value == value:
                return True
        return False

    def __getitem__(self, index):
        start_index = 0
        node = self.start
        while start_index < index:
            node = node.next_node
            start_index += 1
        return node

    def remove(self, index):
        """
        удалить node с индексом index
        """
        prev_node = self[index - 1]
        prev_node.next_node = self[index + 1]

    def insert(self, node, index):
        """
        вставить node в связанный список на позицию index
        """
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

    def append(self, node: Node):
        if not self.start:
            self.start = node
            self.end = node
            return
        self.end.next_node = node
        self.end = node

    def reverse(self):
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
