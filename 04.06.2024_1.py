import threading
import time

def func_max(ls):
    print(max(ls))


def func_min(ls):
    print(min(ls))


ls = input('Введите значения через пробел: ').split()
ls = [int(x) for x in ls]
print(ls)


t1 = threading.Thread(target=func_max, args=(ls, ))
t2 = threading.Thread(target=func_min, args=(ls, ))
t1.start()
t2.start()


# import threading
#
#
# def get_min(arr, ):
#     print( min(arr) )
#
#
# def get_max(arr, ):
#     print( max(arr) )
#
#
# nums = input("Введите числа через пробел: ").split()
# nums = [int(x) for x in nums]
#
#
# t1 = threading.Thread(target=get_min, args=(nums, ))
# t2 = threading.Thread(target=get_max, args=(nums, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()




