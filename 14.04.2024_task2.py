class Book:
                                    # Реализуйте класс «Книга».Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
    def __init__(self, title, year_of_issue, publisher, genre, author, price):
        self.title = title
        self.year_of_issue = year_of_issue
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
                                                                # Реализуйте методы класса для ввода данных, вывода данных
    def print(self):
        print(
            f'Книга {self.title}, год выпуска - {self.year_of_issue}, издательство {self.publisher}, жанр {self.genre}, автор {self.author} и стоимостью {self.price} рублей')

    def input(self):
        input(f'Книга {self.title}, год выпуска - {self.year_of_issue}, издательство {self.publisher}, жанр {self.genre}, автор {self.author} и стоимостью {self.price} рублей')

                                                                # Реализуйте доступ к отдельным полям через методы класса
    def set_title(self, title_new):
        self.title = title_new

    def get_title(self):
        return self.title

    def set_year_of_issue(self, year_of_issue_new):
        self.year_of_issue = year_of_issue_new

    def get_year_of_issue(self):
        return self.year_of_issue

    def set_publisher(self, publisher_new):
        self.publisher = publisher_new

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre_new):
        self.genre = genre_new

    def get_genre(self):
        return self.genre

    def set_author(self, author_new):
        self.author = author_new

    def get_author(self):
        return self.author

    def set_price(self, price_new):
        self.price = price_new

    def get_price(self):
        return self.price

    def __repr__(self):
        return f'{self.title, self.year_of_issue, self.publisher, self.genre, self.author, self.price}'

i1 = Book('Война и мир', 2010, 'Booknet', 'Проза', 'Лев Толстой', 1000)
print(i1)