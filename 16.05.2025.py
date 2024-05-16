class Node:                  #элемент связанного списка, структура данных
    def __init__(self, value, next_):
        self.value = value
        self.next_ = next_

    def as_list(self):
        res = [self.value, ]
        elem = self.next_
        while elem is not None:
            res.append(elem.value)
            elem = elem.next_
        return res

    def delete(self, index):
        elem = self
        for x in range(index - 1):
            elem = elem.next_
        if elem.next_ is not None:
            elem.next_ = elem.next_.next_
        else:
            elem.next_  = None

    def append(self, value):
        elem = self
        while elem.next_ is not None:
           elem = elem.next_
        elem.next_ = Node(value, None)

    def insert(self, index, value):
        left = self
        for x in range(index - 1):
            left = left.next_

        right = left.next_
        new = Node(value, right)
        left.next_ = new



b = Node(2, Node(1, Node(3, Node(9, None))))
print(b.value)
print(b.delete(2))
print(b.as_list())
print(b.append(45))
print(b.as_list())
print(b.insert(2, 8))
print(b.as_list())






