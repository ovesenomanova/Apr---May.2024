import threading


a = input('Введите путь к файлу: ')

file = open(a, 'r', encoding='utf-8')
data = file.read().split()
b = input('Введите слово для поиска: ')
file.close()


def find_word(x):
    if x in data:
        print('Слово найдено!')
    else:
        print('Слово не найдено!')


t1 = threading.Thread(target=find_word(b), args=(data, ))
t1.start()
t1.join()

