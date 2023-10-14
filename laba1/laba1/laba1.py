#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from random import randint
import time
import threading



def task1():
    ncomp = True
    while(ncomp):
        try:
            left = int(input("Левая граница: "))
            right = int(input("Правая граница: "))
            print(f"Угадайте число от {left} до {right}")
            guess_num = randint(left, right)
            inp_num = -1
            attemps = 0
            while(guess_num != inp_num):
                attemps += 1
                try:
                    inp_num = int(input("Введите число: "))
                    if (guess_num > inp_num):
                        print("Ваше число меньше загаданого")
                    elif (guess_num < inp_num):
                        print("Ваше число больше загадоного")
                    elif (guess_num == inp_num):
                        print(f"Вы угадали, вам понадобилось {attemps} попыток")
                        ncomp = False
                except ValueError:
                    print("Введено что-то не то, введите еще раз")
                    attemps -= 1

        except ValueError:
            print("Введено что-то не то, введите еще раз")



def task2(n,  n1 = 0):
    if(n<=n1):
        return 1
    else:
        return n*task2(n-1, n1)

def task3(arr):
    S = 0.0
    count = len(arr)
    if count > 0:

            for n in arr:
                if isinstance(n, (int, float)) != True:
                    raise Exception("В массиве значения не того типа")
                S += n
            return S/count
    else:
       raise Exception("Пустой массив")

def task4(a: float) -> float:
    def to(b: float) -> float:
        return a + b
    return to
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    return wrapper


@timer
def check_time(n):
    return task2(n)

res = 1
lock = threading.Lock()

def task6(n, num_threads):
    global res
    def task6_th(end, start):
        global res
        th_res = task2(end, start)
        lock.acquire()
        res *= th_res
        lock.release()
    if num_threads == 1:
        return task2(n)
    else:
        res = 1
        threads = []
        chunk_size = n // num_threads
        for i in range(num_threads):
            start = i * chunk_size
            end = (i+1) * chunk_size
            if i == num_threads - 1:
                end = n
            t = threading.Thread(target=task6_th, args=(end,start))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return res

flag = True
while (flag):
    comp = False
    try:
        mode = int(input("1) \"Угадай число\" \n2) Факториал "
                         "\n3) Среднее значение \n4) Сложить два числа "
                         "\n5) Время выполнения функции \n6) Посчитать факториал (параллельно) \n0) Выход\n"))
        if mode == 1:
            task1()
        elif mode == 2:
            while(comp == False):
                try:
                    num = int(input("Вычислить факториал от числа: "))
                    if(num >= 0):
                        print(task2(num))
                        comp = True
                    else:
                        print("Число должно быть положительным")
                except ValueError:
                    print("Введено что-то не то, введите еще раз")
        elif mode == 3:
            while (comp == False):
                try:
                    count = int(input("Введите количество чисел: "))
                    mas = []
                    print("Введите числа: ")
                    i = 0
                    if count > 0:
                        while(i<count):
                            try:
                                 mas.append(float(input()))
                                 i+=1
                            except ValueError:
                                print("Введено что-то не то, введите еще раз")
                        print(task3(mas))
                        comp = True
                    else:
                        print("Длина массива должна иметь положительную величину")
                except ValueError:
                    print("Введено что-то не то, введите еще раз")
        elif mode == 4:
            while(comp == False):
                try:
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    print(task4(a)(b))
                    comp = True
                except ValueError:
                    print("Введено что-то не то, введите еще раз")
        elif mode == 5:
            while (comp == False):
                try:
                    num = int(input("Вычислить факториал от числа: "))
                    if (num >= 0):
                        print(check_time(num))
                        comp = True
                    else:
                        print("Число должно быть положительным")
                except ValueError:
                    print("Введено что-то не то, введите еще раз")
        elif mode == 6:
            while (comp == False):
                 try:
                    n = int(input("Введите факториал какого числа хотите получить: "))
                    th = int(input("Введите количество потоков: "))
                    if(n>0 and th>0 and n>=th):
                        print(task6(n, th))
                        comp = True
                    else:
                        print("Оба числа должны быть положительными и n должен быть больше th")
                 except ValueError:
                    print("Введено что-то не то, введите еще раз")
        elif mode == 0:
            flag = False
        else:
            print("Неправильный ввод")
    except ValueError:
        print("Введено что-то не то, введите еще раз")