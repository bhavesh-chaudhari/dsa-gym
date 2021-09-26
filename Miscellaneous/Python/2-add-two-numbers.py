# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "Node({}, {})".format(self.val, self.next)

    def __repr__(self):
        return self.__str__()


def create_node_list(number):
    str_num = str(number)[::-1]
    # print(str_num)
    start_node = Node(int(str_num[0]))
    current_node = start_node
    # print(start_node)
    # print(current_node)

    for num in str_num[1:]:
        tmp_node = Node(int(num))
        current_node.next = tmp_node
        current_node = tmp_node
        print(current_node)
    #         print(start_node)
    return start_node


def addTwoNumbers(l1, l2):
    result_start_node = Node(0)
    node = result_start_node
    n1 = l1
    n2 = l2
    c = Node(0)  # carry
    while not (n1.next is None and n2.next is None):
        if n1.next is None:
            n1.next = Node(0)
        if n2.next is None:
            n2.next = Node(0)
        addition = n1.val + n2.val + c.val
        carr, val = divmod(addition, 10)
        tmp_node = Node(val)
        node.next = tmp_node
        node = tmp_node

        n1 = n1.next
        n2 = n2.next
        c.val = carr

    # handle corner case: when both the next elements are None, take sum of the current nodes.
    addition = n1.val + n2.val + c.val
    carr, val = divmod(addition, 10)
    tmp_node = Node(val)
    node.next = tmp_node
    node = tmp_node
    # make extra node for carry
    if carr != 0:
        node.next = Node(carr)

    return result_start_node.next

num1 = 97987
num2 = 97987
l1 = create_node_list(num1)
l2 = create_node_list(num2)
print(addTwoNumbers(l1,l2))