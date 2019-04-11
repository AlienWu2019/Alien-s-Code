#在pthon中，所有以“_”双下划线包起来的方法，都统称为“魔术方法”。

class User(object):
    pass

if __name__ == "__main__":
    print(dir(User()))
