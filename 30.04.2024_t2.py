class Node:                  #элемент связанного списка, структура данных
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


l_list = Linkedlist()
l_list.append(5)
l_list.append(10)
l_list.append(15)
l_list.append(20)
l_list.display()
