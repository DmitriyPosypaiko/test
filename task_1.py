def sort(func):
    def wrapper():
        func()
        for people in info:
            if people[2] == 'М':
                people[2] = "Г-н"
            elif people[2] == 'Ж':
                people[2] = "Г-жа"

    return wrapper

class Worker:
    def __init__(self, firstname, lastname, typ, age):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__typ = typ
        self.__age = age
    @property
    def info(self):
        info.extend([[self.__firstname, self.__lastname, self.__typ, self.__age]])
        return [self.__firstname, self.__lastname, self.__typ, self.__age]


@sort
def test():
    b = int(input("Введите целое число --> "))
    for i in range(b):
        piople = input().split()
        firstname = piople[0]
        lastname = piople[1]
        typ = piople[2]
        age = piople[3]
        s = Worker(firstname,lastname,typ,age)
        s.info



@sort
def readfile():
    with open("file_task_1.txt", "r") as file:
        b = int(input("Введите целое число --> "))
        for line in file:
            piople = line.split()
            firstname = piople[0]
            lastname = piople[1]
            typ = piople[2]
            age = piople[3]
            s = Worker(firstname, lastname, typ, age)
            s.info
            b -= 1
            if b == 0:
                break



def menu():
    a = input("Выберете тип ввода данных:\n"
          "1: С клавиатуры\n"
          "2: С файла\n"
          "--> ")
    return a

if __name__ == '__main__':
    info = []
    if menu() == '1':
        test()
        sort = sorted(info, key=lambda x: x[3])
        for i in sort:
            i.pop()
            i.insert(0, i.pop())
            c = ' '.join(map(str, i))
            print[i]

    else:
        readfile()
        sort = sorted(info, key=lambda x: x[3])
        for i in sort:
            i.pop()
            i.insert(0, i.pop())
            c = ' '.join(map(str, i))
            print(c)


