# class Node:#Last In First Out
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node=next_node
# class Stack:
#     def __init__(self):
#         self.top = None
#
#     def push(self, data):
#         new_top=Node(data, self.top)
#         self.top = new_top
#
#     def pop(self):
#         if self.top is Node:
#             return None
#         removed_data = self.top.data
#         self.top = self.top.next_node
#         return removed_data
#
#     def __str__(self):
#         l=[]
#         if self.top is None:
#             return str(l)
#         node = self.top
#         while node:
#             l.append(node.data)
#             node = node.next_node
#         return str(l)
#
#
# if __name__ == '__main__':
#     s = Stack()
#     for i in range(1, 10):
#         s.push(i)
#         print(s)
#     for i in range(1, 10):
#         s.pop()
#         print(s)
###########################################################################
# class Node:#Ochered Queue
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node = next_node
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def enqueue(self, data):
#         if self.tail is None and self.head is None:
#             self.tail = self.head = Node(data, None)
#             return
#         self.tail.next_node = Node(data, None)
#         self.tail = self.tail.next_node
#     def dequeue(self):
#         if self.head is None:
#             return None
#         removed_data = self.head.data
#         self.head = self.head.next_node
#         if self.head is None:
#             self.tail = None
#         return removed_data
#
#     def __str__(self):
#             l=[]
#             if self.head is None:
#                 return str(l)
#             node = self.head
#             while node:
#                 l.append(node.data)
#                 node = node.next_node
#             return str(l)
# if __name__ == '__main__':
#     s = Queue()
#     for i in range(0, 10):
#         s.enqueue(i)
#         print(s)
#     for i in range(1, 14):
#         s.dequeue()
#         print(s)
##### Odnosviaznii Spisok############
# class Node:
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node = next_node
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def insert_begining(self, data):
#         if self.head is None:
#             self.head = self.tail = Node(data, None)
#             return
#         new_node = Node(data, self.head)
#         self.head = new_node
#     def insert_end(self, data):
#         if self.head is None:
#             self.head = self.tail = Node(data, None)
#             return
#         self.tail.next_node = Node(data, None)
#         self.tail = self.tail.next_node
#     def search_by_id(self, id):
#         node = self.head
#         while node:
#             if node.data['id'] == id:
#                 return node.data
#             node=node.next_node
#         return None
#
#     def __str__(self):
#         l = []
#         if self.head is None:
#             return str(l)
#         node = self.head
#         while node:
#             l.append(node.data)
#             node = node.next_node
#         return str(l)
# if __name__ == '__main__':
#
#     s = LinkedList()
#     for i in range(5):
#      # s.insert_end({'id':1,'company name': 'name'})
#      s.insert_begining({'id': 1, 'company name': 'name'})
#      print(s)
# print((s.search_by_id(1)))
# print((s.search_by_id(11)))
#######################Hesh Tablica#############################
# Реализация хеш-таблицы в Python
#
# hashTable = [[],] * 10
#
# def checkPrime(n):
#     if n == 1 or n == 0:
#         return 0
#
#     for i in range(2, n//2):
#         if n % i == 0:
#             return 0
#     return 1
#
# def getPrime(n):
#     if n % 2 == 0:
#         n = n + 1
#     while not checkPrime(n):
#         n += 2
#     return n
#
# def hashFunction(key):
#     capacity = getPrime(10)
#     return key % capacity
#
# def insertData(key, data):
#     index = hashFunction(key)
#     hashTable[index] = [key, data]
#
# def removeData(key):
#     index = hashFunction(key)
#     hashTable[index] = 0
#
# insertData(123, "apple")
# insertData(432, "mango")
# insertData(213, "banana")
# insertData(654, "guava")
# insertData(654, "guava")
#
# print(hashTable)
# # removeData(123)
# print(hashTable)
##############################
# hashtable.py

# ...
# hashtable.py

# from typing import NamedTuple, Any
#
# class Pair(NamedTuple):
#     key: str
#     value: int
#
#
# class HashTable:
#     def __init__(self, capacity):
#         self._pairs = capacity * [None]
#
#     def __len__(self):
#         return len(self._pairs)
#
#     def __delitem__(self, key):
#         if key in self:
#             self._pairs[self._index(key)] = None
#         else:
#             raise KeyError(key)
#
#     def __setitem__(self, key, value):
#         self._pairs[self._index(key)] = Pair(key, value)
#
#     def __getitem__(self, key):
#         pair = self._pairs[self._index(key)]
#         if pair is None:
#             raise KeyError(key)
#         return pair.value
#
#     def __contains__(self, key):
#         try:
#             self[key]
#         except KeyError:
#             return False
#         else:
#             return True
#
#     def get(self, key, default=None):
#         try:
#             return self[key]
#         except KeyError:
#             return default
#
#     @property
#     def pairs(self):
#         return self._pairs.copy()
#
#     def _index(self, key):
#         return hash(key) % len(self)
#
# if __name__ == '__main__':
#     s = HashTable(5)

#     for i in range(5):
#      # s.insert_end({'id':1,'company name': 'name'})
#      s.insert_begining({'id': 1, 'company name': 'name'})
#      print(s)
# print((s.search_by_id(1)))
# print((s.search_by_id(11)))
#####################################################Hash Table#################################
# class Data:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#
# class Node:
#     def __init__(self, data = None, next_node = None):
#         self.data = data
#         self.next_node = next_node
#
# class HashTable:
#     def __init__(self, table_size):
#         self.table_size = table_size
#         self.hash_table = [None]*table_size
#
#     def custom_hash(self, key):
#         hash_value = 0
#         for  i in key:
#             hash_value += ord(i)
#             hash_value = (hash_value*ord(i))%self.table_size
#         return hash_value
#     def add_key_value(self, key, value):
#         hash_key = self.custom_hash(key)
#         if self.hash_table[hash_key] is None:
#             self.hash_table[hash_key] = Node(Data(key, value), None)
#         else:
#             node = self.hash_table[hash_key]
#             while node.next_node:
#                 node = node.next_node
#             node.next_node = Node(Data(key, value), None)
#     def get_value(self, key):
#         hash_key = self.custom_hash(key)
#         if self.hash_table[hash_key] is not None:
#             node = self.hash_table[hash_key]
#             # if node.next_node:
#             while node.next_node:
#                 if key == node.data.key:
#                     return node.data.value
#                 node = node.next_node
#             return node.data.value
#
#         return None
#
#     def print_ht(self):
#         print('{')
#         for i, node in enumerate(self.hash_table):
#             if node:
#                 ll_str = ''
#                 if node.next_node:
#                     while node.next_node:
#                         ll_str += str(node.data.key) + ': ' + str(node.data.value) + '-->'
#                         node = node.next_node
#                     ll_str += str(node.data.key) + ': ' + str(node.data.value) + '--> None'
#                     print(f'    [{i}]   +     {ll_str} ')
#                 else:
#                     print(f'    [{i}]         {node.data.key}: {node.data.value} ')
#             else:
#                 print(f'    [{i}]         None')
#         print('}')
"""""
{
    [0] None
    [1] key: value --> key2: value2 --> None
}
"""
#n1 = Node(Data('Den', '33-33', None))
# ht = HashTable(5)
# ht.add_key_value('DEN', '11-11')
# ht.add_key_value('DET', '22-11')
# ht.add_key_value('DEM', '33-11')
# ht.add_key_value('DEN', '11-11')
#
# ht.print_ht()

#HashTable.custom_hash('Den')#Vizivaem cheres eksemplyar a ne cherez class
# print(ht.custom_hash('Dev'))
# print(ht.custom_hash('Dez'))
# print(ht.custom_hash('Den'))
####################################################
########################Odnosviaznii spisok
class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.length += 1
            return element
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(element)
        self.length += 1
        return element
    def __str__(self):
        node = self.head
        line = '['
        while node.next_node:
            line += str(node.element) + ','
            node = node.next_node
        line += str(node.element) + ']'
        return line
    def __getitem__(self, key):
        i = 0
        node = self.head
        while i < key:
            node = node.next_node
            i += 1
        return node.element
    def insert(self, key, value):
        i = 0
        node = self.head
        prev_node = self.head
        if key == 0:
            old_head = self.head
            self.head = self.Node(value, next_node=old_head)
            return  value
        while i < key:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = self.Node(value, next_node=node)
        self.length += 1
        return value
    def __delitem__(self, key):
        i=0
        node = self.head
        prev_node = node

        if key == 0:
            old_head = self.head
            element = self.head.element
            self.head = self.head.next_node
            self.length -= 1

            del old_head
            return element

        while i < key:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = node.next_node
        element = node.element
        self.length -= 1

        del node
        return element

a = LinkedList()
a.append(4)
a.append(8)

a.insert(1,2)
print(a, a.length)
del a[2]
print(a, a.length)
# print(a[1])

###############################