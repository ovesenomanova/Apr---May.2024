import string

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, item):
        self.items.append(str(item))

    def pop(self):                          #удаляет последний элемент в стеке
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def pop2(self):                        #удаляет n-последних элементов в стеке
        pop_items = []
        if not self.is_empty():
            for j in range(2):
                pop_items.append(self.items.pop())
            return pop_items
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def show(self):
        print(*self.items)


class StackFix(Stack):
    def __init__(self, stack_size):
        super().__init__()
        self.stack_size = stack_size

    def push(self, item):
        if self.size() >= self.stack_size:
            self.pop()
        self.items.append(str(item))

    def is_full(self):
        return len(self.items) == self.stack_size


stack1 = Stack()
stack2 = StackFix(20)
for i in range(50):
    stack1.push(string.ascii_letters[:i])
    stack2.push(string.ascii_letters[:i])

print("stack1:")
stack1.show()
print(*stack1.pop2())
stack1.show()

print("stack2:")
stack2.show()
print(*stack2.pop2())
stack2.show()


