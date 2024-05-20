class Model:
    def __init__(self):
        self.__RECEIPTS = {
            "Хот-Дог": {
                "price": 100,
                "amount": 10
            },
            "Хот-Дог По Датски": {
                "price": 120,
                "amount": 8
            }
        }
        self.__profit = 0

    def get_receipts(self):
        return self.__RECEIPTS

    def sell(self, meal: str):
        self.__RECEIPTS[meal]["amount"] -= 1
        self.__profit += self.__RECEIPTS[meal]["price"]

    def get_name_from_num(self, num):
        return list(self.__RECEIPTS.keys())[num - 1]


class View:
    @staticmethod
    def greetings():
        print("Здравствуйте, чтобы вы хотели заказать?")

    @staticmethod
    def show_receipts(receipts):
        k = 1
        for name, item in receipts.items():
            print(f"{k}: {name}\t{item['price']} руб.")
            k += 1

    @staticmethod
    def bye():
        print("Спасибо за покупку. Приходите еще!")


class Control:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.greetings()
        self.view.show_receipts(
            self.model.get_receipts()
        )
        k = int(input("Укажите номер: "))
        meal = self.model.get_name_from_num(k)
        self.model.sell(meal)
        self.view.bye()


m = Model()
control = Control(m, View)
control.start()
