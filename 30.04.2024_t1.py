class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):                                          #забирает элемент из стэка и удаляет
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):                                           #добавляет элемент в стэк
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def show(self):
        print(*self.items)                                      #убираем скобки - через *



s1 = Stack()
s1.push(5)
s1.push(10)
s1.push(25)
s1.push(20)
print(s1.size())
print(s1.peek())
print(s1.size())
print(s1.pop())
print(s1.size())
s1.show()

