#встроенные функции
def task1(numbers):
    

    return eval('*'.join(list(map(str, numbers))))


def task2(s):
    
    uppercasse = len([i for i in s if i.isupper()])

    lowercase = len([i for i in s if i.islower()])

    print(f'uppercase letters = {uppercasse}\nlowercase letters = {lowercase}')



def task3(s):
    

    print(True if s == s[::-1] else False)

def task4():
   
    
    from time import sleep

    num = int(input())
    sleepTime = int(input())

    sleep(sleepTime / 1000)

    print(f'Square root of {num} after {sleepTime} miliseconds is {num**0.5}')

def task5(tup):
    '''
    Напишите программу на Python со встроенной функцией, которая возвращает значение True, если все элементы кортежа равны true.
    '''
    return True if all(tup) else False