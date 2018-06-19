"""
题目描述：
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

""" 定义单链表 """
class ListNode():
    def __init__(self, node, val):
        self.node = node
        self.val = val

    def display(self, node_p):
        while node_p != None:
            print("display: ", node_p.val)
            node_p = node_p.node

    def clean_linkNode(self, pnode):
        if pnode == None:
            print("clean ok!")
        else:
            pnode.node = None
            print("clean ok!")

    def is_None(self, pnode):
        if pnode.node == None:
            print("Node")
            return True
        else:
            print("False")
            return False


def node2int(node_p):
    """ 把逆序链表转换为正序数字 测试通过"""
    count = 0;
    _sum = 0
    while node_p != None:
        temp = 10 ** count
        val = node_p.val
        temp = temp * val
        _sum = _sum + temp
        count += 1
        node_p = node_p.node
    return _sum

def create_linkNode(data):
    """
    创建链表
    :param data: 12345, 345, 675 etc..
    :return:
    """
    content = str(data);
    node_list = []
    for i in range(len(content)):
        value = int(content[i])
        print("value ", value)
        temp_node = ListNode(None, value) # 仅仅创建链表
        node_list.append(temp_node)
    count = 1
    length = len(node_list)
    sorted_list = node_list[:: -1]
    for i in range(length-1):
        first_node = sorted_list[i]
        second_node = sorted_list[i+1]
        second_node.node = first_node
    return second_node

if __name__ == "__main__":
    """ (2 -> 4 -> 3) """
    node_3 = ListNode(None, 3)
    node_4 = ListNode(node_3, 4)
    node_2 = ListNode(node_4, 2)
    print(node2int(node_2))
    """ (5 -> 6 -> 4) """
    node_last = ListNode(None, 4)
    node_middle = ListNode(node_last, 6)
    node_first = ListNode(node_middle, 5)
    print(node2int(node_first))
    """ 创建逆序链表 456 =》（6 -> 5 -> 4）"""
    node_test = create_linkNode(456)
    Node = ListNode(None, None)
    Node.display(node_test)


def solution(node1, node2):
    _sum = node2int(node1) + node2int(node2)
    data = str(_sum)
    index = 0
    for i in range(len(data)):
        index += 1





