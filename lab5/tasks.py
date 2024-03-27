import re


def task1():
    
    
    pattern = re.compile(r'ab*')
    
    text = input()

    print("YES" if pattern.search(text) else "NO")



def task2():
    
    
    pattern = re.compile(r'ab{2,3}')

    text = input()

    print("YES" if pattern.search(text) else "NO")


def task3():
    
  
    

    pattern = re.compile(r'[a-z]+\_')

    text = input()

    print(pattern.findall(text))

    
def task4():
    
    
    

    pattern = re.compile(r'[A-Z]{1}[a-z]+')

    text = input()

    print(pattern.findall(text))

def task5():
    
    

    pattern = re.compile(r'a.+b\Z')

    text = input()

    print("YES" if pattern.search(text) else "NO")

def task6():
    
    
    

    pattern = re.compile(r'[ ,.]')

    text = input()

    print(pattern.sub(':', text))


def task7():
    
    
    def snake_to_camel(snake_case):
        return re.sub(r"_([a-z])", lambda s: s.group(1).upper(), snake_case)
    

    snakeCase = input()

    camelCase = snake_to_camel(snakeCase)

    print(camelCase)

#hello_world",  "helloWorld".

def task8():

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())
#snakeCase.

#snake case 

def task9():
    
    #Write a Python program to insert spaces between words starting with capital letters.
    

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())

def task10():
    
    #Write a Python program to convert a given camel case string to snake case.
    

    def camelToSnake(snake_case):
        return re.sub(r"\B([A-Z])", lambda s: '_'+s.group(1), snake_case).lower()
    
    camelCase = input()

    snakeCase = camelToSnake(camelCase)

    print(snakeCase)
#snakeCase.

#snake_case 