from collections import Counter

def add_x():
    namber = int(input("Ввод:\n"))
    for i in range(namber):
        X.append(input())

def add_y():
    namber = int(input())
    for i in range(namber):
        Y.append(input())

def readfile():
    with open("file_task_2.txt", "r") as file:
        b = int(input("Введите количество строк X --> "))
        for line in file:
            X.append(line.split()[0])
            if len(line.split()) > 1:
                Y.append(line.split()[-1])
            b -= 1

def sort():

    Res = [x for x in X if x in Y]
    for value in Y:
        print(f'{value} -> {Res.count(value)}')



# def new_sort():
#     Res = [x for x in X if x in Y]
#     b = Counter(Res)
#     print(b)

def menu():
    a = input("Выберете тип ввода данных:\n"
              "1: С клавиатуры\n"
              "2: С файла\n"
              "--> ")
    if a == '1':
        add_x()
        add_y()
    elif a == '2':
        readfile()


if __name__ == '__main__':
    X = []
    Y = []
    menu()
    sort()
    # new_sort()