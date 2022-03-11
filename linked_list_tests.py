from linked_list import Node, ListNode

import unittest


class LinkedListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.list_node = ListNode()

    def test_append_method(self):
        self.assertEqual(len(self.list_node), 0)
        self.list_node.append(self.node1)
        self.assertEqual(len(self.list_node), 1)
        self.list_node.append(self.node2)
        self.assertEqual(len(self.list_node), 2)

        self.assertEqual(self.list_node.start, self.node1)
        self.assertEqual(self.list_node.end, self.node2)

        self.assertEqual(self.node1.next_node, self.node2)

    def test_iter(self):
        self.list_node.append(self.node1)
        self.list_node.append(self.node2)
        expected_result = [self.node1, self.node2]
        iter_result = [node for node in self.list_node]
        self.assertEqual(iter_result, expected_result)

    def test_contains(self):
        self.assertFalse(self.node1 in self.list_node)
        self.list_node.append(self.node1)
        self.assertTrue(self.node1 in self.list_node)

    def test_getitem(self):
        self.list_node.append(self.node1)
        self.list_node.append(self.node2)
        self.assertEqual(self.list_node[1], self.node2)

        with self.assertRaises(IndexError):
            self.list_node[90]

    def test_remove(self):
        node3 = Node("node3")
        self.list_node.append(self.node1)
        self.list_node.append(self.node2)
        self.list_node.append(node3)
        self.list_node.remove(1)

        self.assertEqual(self.node1.next_node, node3)
        self.assertEqual(len(self.list_node), 2)
        self.assertEqual([node for node in self.list_node], [self.node1, node3])

    def test_insert(self):
        self.list_node.append(self.node1)
        self.list_node.append(self.node2)
        new_node = Node("node3")
        self.list_node.insert(new_node, 1)

        self.assertEqual([node for node in self.list_node], [self.node1, new_node, self.node2])

    def test_reverse(self):
        self.list_node.append(self.node1)
        self.list_node.append(self.node2)
        new_node = Node("node3")
        self.list_node.append(new_node)

        self.list_node.reverse()
        expected_result = [new_node, self.node2, self.node1]
        result = [node for node in self.list_node]
        self.assertEqual(result, expected_result)

    def test_popleft(self):
        self.list_node.append(self.node1)
        self.list_node.append(self.node2)

        node3 = Node('node3')
        self.list_node.append(node3)

        start_node = self.list_node.popleft()
        self.assertEqual(start_node, self.node1)

        self.assertEqual(list(iter(self.list_node)), [self.node2, node3])

    def test__initialize_start_and_end(self):
        a = [10, 20, 30]
        self.list_node._initialize_start_and_end(a)
        self.assertEqual(self.list_node.start, Node(10))
        self.assertEqual(self.list_node.end, Node(30))

        a = []
        self.list_node._initialize_start_and_end(a)
        self.assertEqual(self.list_node.start, None)
        self.assertEqual(self.list_node.end, None)
