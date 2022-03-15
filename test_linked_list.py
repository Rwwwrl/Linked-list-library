from linked_list import Node, ListNode

import unittest


class LinkedListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.list_node = ListNode()

    def test_append_method(self):
        self.assertEqual(len(self.list_node), 0)
        self.list_node.append('node1')
        self.assertEqual(len(self.list_node), 1)
        self.list_node.append('node2')
        self.assertEqual(len(self.list_node), 2)

        self.assertEqual(self.list_node.start, Node('node1'))
        self.assertEqual(self.list_node.end, Node('node2'))

    def test_iter(self):
        self.list_node.append('node1')
        self.list_node.append('node2')
        expected_result = [Node('node1'), Node('node2')]
        iter_result = [node for node in self.list_node]
        self.assertEqual(iter_result, expected_result)

    def test_contains(self):
        self.assertFalse('node1' in self.list_node)
        self.list_node.append('node1')
        self.assertTrue('node1' in self.list_node)

    def test_getitem(self):
        self.list_node.append('node1')
        self.list_node.append('node2')
        self.assertEqual(self.list_node[1], Node('node2'))

        with self.assertRaises(IndexError):
            self.list_node[90]

    def test_remove(self):
        self.list_node.append('node1')
        self.list_node.append('node2')
        self.list_node.append('node3')
        self.list_node.remove(1)

        self.assertEqual(len(self.list_node), 2)
        self.assertEqual([node for node in self.list_node], [Node('node1'), Node('node3')])

    def test_insert(self):
        self.list_node.append('node1')
        self.list_node.append('node2')
        self.list_node.insert('node3', 1)

        self.assertEqual([node for node in self.list_node], [Node('node1'), Node('node3'), Node('node2')])

    def test_reverse(self):
        self.list_node.append('node1')
        self.list_node.append('node2')
        self.list_node.append('node3')

        self.list_node.reverse()
        expected_result = [Node('node3'), Node('node2'), Node('node1')]
        result = [node for node in self.list_node]
        self.assertEqual(result, expected_result)

    def test_popleft(self):
        self.list_node.append('node1')
        self.list_node.append('node2')
        self.list_node.append('node3')

        start_node = self.list_node.popleft()
        self.assertEqual(start_node, Node('node1'))

        self.assertEqual(list(iter(self.list_node)), [Node('node2'), Node('node3')])

    def test_init(self):
        # для упорядоченного типа данных
        a = [10, 20, 30]
        list_node = ListNode(a)
        self.assertEqual(list_node.start, Node(10))
        self.assertEqual(list_node.end, Node(30))
        self.assertEqual(list(iter(list_node)), [Node(10), Node(20), Node(30)])

        # при пустом списке
        a = []
        list_node = ListNode(a)
        self.assertEqual(list_node.start, None)
        self.assertEqual(list_node.end, None)
        self.assertEqual(list(iter(list_node)), [])

        # при не упорядоченном типе данных
        a = set([10, 20, 30])
        list_node = ListNode(a)
        self.assertEqual(list_node.start, Node(10))
        self.assertEqual(list_node.end, Node(30))
        self.assertEqual(list(iter(list_node)), [Node(10), Node(20), Node(30)])