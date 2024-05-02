#################### №1 ####################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
        while True:
            print(f"1. Добавить новое число;\n"
                  f"2. Удалить все вхождения числа из списка;\n"
                  f"3. Показать список;\n"
                  f"4. Есть ли значение в списке;\n"
                  f"5. Заменить значение в списке.\n")
            get_choice = int(input("Ваш выбор: "))
            if get_choice == 1:
                val = int(input("Введите новое значение: "))
                self.append(val)
            elif get_choice == 2:
                val = int(input("Введите элемент, который хотите удалить: "))
                self.remove(val)
            elif get_choice == 3:
                self.show()
            elif get_choice == 4:
                val = int(input("Введите искомый элемент: "))
                self.find(val)
            elif get_choice == 5:
                val = int(input("Введите число для замены: "))
                print(f"Заменить ли все значения или только первое вхождение?\n"
                      f"1. Все;\n"
                      f"2. Только первое.\n")
                choice = bool(int(input("Вы выбираете...: ")) - 1)
                self.replace(choice, val)

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        cur = self.head
        prev = None
        if cur is not None and cur.data == val:
            if cur.next is not None:
                self.head = cur.next
                cur = self.head
            else:
                self.head = None
                return
        else:
            prev = cur
            cur = cur.next

        while cur is not None:
            if cur.data == val:
                prev.next = cur.next
                cur = None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

    def find(self, val):
        cur = self.head
        while cur is not None:
            if cur == val:
                print("Значение есть в списке!")
        print("Значения нет в списке!")

    def replace(self, choice, val):
        if choice:
            self.head.data = val
        else:
            cur =


user_data = map(int, input("Введите вашу последовательность: ").split())
l_list = LinkedList()

for el in user_data:
    l_list.append(el)

l_list.display()