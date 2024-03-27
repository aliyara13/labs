import os

def task1(path):
    '''
   Напишите программу на Python, которая будет выводить список только каталогов, файлов и всех каталогов, файлов по указанному пути.
    '''

    print([name for name in os.listdir(path)]) # lists dirs and files 
    print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) # lists dirs
    print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]) # lists files


def task2(path):
   

    if os.path.exists(path):
        result = 'Path is '

        result += 'readable, ' if os.access(path, os.R_OK) else 'not readable, '

        result += 'writable, ' if os.access(path, os.W_OK) else 'not writable, '

        result += 'executable' if os.access(path, os.X_OK)else 'not executable.'

        print(f'Path {path} exists\n{result}')

    else:
        print(f'Path {path} does not exists')



def task3(path):
   

    if os.path.exists(path):
        print(f'Path {path} exists')
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f'Path {path} does not exists')
#если путь существует он разделяет имя файла и часть каталога указанного пути
def task4(path):

    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'Numbers of lines = {len(lines)}')

def task5(path, l):
    '''
    Write a Python program to write a list to a file.
    '''

    with open(path, 'w') as file: 
        file.write(' '.join(l)) 

def task6():


    from string import ascii_uppercase
    for letter in ascii_uppercase:
        with open(f'{letter}.txt', 'w'):
            pass

    
        

def task7(path1, path2):
    '''
    Write a Python program to copy the contents of a file to another file
    '''

    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        file2.write(file1.read()) #записываем содержимое во второй файл

def task8(path):
    

    if os.access(path, os.F_OK):#проверка существует ли  файл
        os.remove(path)
        print('File exists and has been removed')
    else:
        print(f"Error: File '{path}' does not exist.")