import time


def fun1(x):
    print('fun1 boshlandi')
    x**2
    time.sleep(3)
    print('fun1 bajarildi')


def fun2(x):
    print('fun2 boshlandi')
    x**0.5
    time.sleep(3)
    print('fun2 bajarildi')


def main():
    fun1(4)
    fun2(4)


start = time.time()

main()

end = time.time()

print('sarflangan vaqt: {:.2f}s'.format(end - start))
