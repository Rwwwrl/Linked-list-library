from linked_list import ListNode, Node

from datetime import datetime, timedelta

def gen_list():
    '''
    сгенерировать большой список 
    '''
    return [i for i in range(10 ** 7)]

def gen_list_node():
    '''
    сгенероровать большой связанныый список 
    '''
    list_node = ListNode()
    for i in range(10 ** 7):
        node = Node(f'node{i}')
        list_node.append(node)
    return list_node

def get_time_of_operation(func):
    '''
    получить время выполнения операции в мс 
    '''
    before = datetime.now()
    func()
    after = datetime.now()
    return (before - after).microseconds


if __name__ == '__main__':
    list_node = gen_list_node()
    arr = gen_list()

    list_node_remove_time = get_time_of_operation(lambda: list_node.remove(10 ** 2))
    list_remove_time = get_time_of_operation(lambda: arr.remove(10 ** 2))
    print({
        'list_node_remove_time': list_node_remove_time,
        'list_remove_time': list_remove_time
    })

    list_node_insert_time = get_time_of_operation(lambda: list_node.insert(Node('new_node'), 10 ** 2))
    list_insert_time = get_time_of_operation(lambda: arr.insert(10 ** 2, 10))
    print({
        'list_node_insert_time': list_node_insert_time,
        'list_insert_time': list_insert_time,
    })







