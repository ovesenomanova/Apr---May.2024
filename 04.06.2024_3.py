import threading


a = input('Введите путь к файлу: ')

file = open(a, 'r', encoding='utf-8')
data = file.read().split()
data = [int(x) for x in data]
file.close()


def open_even(nums):
    res = list()
    for x in nums:
        if (x % 2) == 0:
            res.append(str(x))
    print(len(res))
    file_even = open('C:/Users/Stud/Desktop/eov/file_even.txt', 'w', encoding='utf-8')
    file_even.write( ' '.join(res))
    file_even.close()


def open_odd(nums):
    res = list()
    for x in nums:
        if (x % 2) != 0:
            res.append(str(x))
    print(len(res))
    file_odd = open('C:/Users/Stud/Desktop/eov/file_odd.txt', 'w', encoding='utf-8')
    file_odd.write(' '.join(res))
    file_odd.close()



t1 = threading.Thread(target=open_even, args=(data, ))
t2 = threading.Thread(target=open_odd, args=(data, ))
t1.start()
t2.start()
t1.join()
t2.join()
