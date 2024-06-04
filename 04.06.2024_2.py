import threading


def get_sum(arr, ):
    print(sum(arr))


def get_mean(arr, ):
    mean = sum(arr, )/len(arr, )
    print(mean)


nums = input("Введите числа через пробел: ").split()
nums = [int(x) for x in nums]


t1 = threading.Thread(target=get_sum, args=(nums, ))
t2 = threading.Thread(target=get_mean, args=(nums, ))
t1.start()
t2.start()
t1.join()
t2.join()




