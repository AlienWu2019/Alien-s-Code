import time
def test (message,sec):
    while True:
        print(time.time(),message,sec)
        now = time.time()
        end = now+sec
        while True:
            yield
            if time.time()>end:
                break

a=test("lupython",1)
b=test("ilyws",1)
list_test = [a,b]
while True:
    for i in list_test:
        next(i)