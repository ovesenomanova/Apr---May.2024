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
        while last_node.next and last_node.data != data:
            last_node = last_node.next
        if last_node.data == data:
            print("Число уже есть!")
        else:
            last_node.next = new_node

    def display(self):
        while True:
            print(f"1. Удалить все вхождения числа из списка;\n"
                  f"2. Показать список;\n"
                  f"3. Есть ли значение в списке;\n"
                  f"4. Заменить значение в списке.\n")
            get_choice = int(input("Ваш выбор: "))
            if get_choice == 1:
                remel = int(input("Введите элемент, который хотите удалить: "))
                self.remove(remel)
            elif get_choice == 2:
                self.show()
            elif get_choice == 3:
                pass
            elif get_choice == 4:
                pass

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


user_data = map(int, input("Введите вашу последовательность: ").split())
l_list = LinkedList()

for el in user_data:
    l_list.append(el)

l_list.display()


