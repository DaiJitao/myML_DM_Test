# _*_ coding:utf-8 _*_


class Node():
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.next_node
    def set_data(self, newData):
        self.data = newData
    def set_next_node(self, newNextNode):
        self.next = newNextNode

class Link_list():
    def __init__(self, _index, next_node):
        self._index = _index
        self.next_node = next_node
    def get(self,value, ):
        pass
    def init_list(self, _list, data_len):
        index = 0
        temp_list = []
        for i in range(data_len):
            temp_list[i] = 0
        for j in _list:
            node = Node(j, None)
            temp_list[index] = node

class HashDemo(object):

    def get_head_list(self, _data_len):
        temp_list = []
        for i in range(0, _data_len):
            node = Node(i,None)
            temp_list.append(node)
        return temp_list

    def get_hash_key(self, _p1, data_len):
        return _p1 % data_len

    def find(self, value):
        hashDemo = HashDemo()
        key = hashDemo.get_hash_key(value, 8)
        head_list = hashDemo.get_hash_key(8)
        pass

    def init_list(self):
        pass


data = [17,24,28,29,31,67,90,83]

def save_head_list(data):
    hash = HashDemo()
    for i in data:
        key = hash.get_hash_key(8)


node = Node(83,None)
node_67 = Node(67, node)
head = Node(None,node_67)

while head.next != None:
    temp = head.next
    print temp.get_data()
    head = temp



