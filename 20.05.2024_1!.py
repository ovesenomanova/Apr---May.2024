class Model:
    def __init__(self, name, author, num_of_symboles, publishing, theme):
        self.name = name
        self.author = author
        self.num_of_symboles = num_of_symboles
        self.publishing = publishing
        self.theme = theme

    def get_article(self):
        return self.na\

    def new_article(self, new_article):
        new_article = self.__article


class View:
    @staticmethod
    def greetings():
        print("Здравствуйте,введите название статьи или автора?")

    @staticmethod
    def show_article(__article):
        for name, item, x, i, j in __article.items():
            print(f"Статья{name}, автор статья {item}, количество знаков \t{i}, впервые опубликована: {i}, краткое содержание: {j}")

    @staticmethod
    def bye():
        print("Спасибо за проявленный интерес. Приходите еще!")


class Control:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.greetings()
        self.view.show_article()
        self.model.get_article()
        self.view.bye()

https://youtu.be/glzG2809cUk?si=9mfEBm6IrZsS8yhH
