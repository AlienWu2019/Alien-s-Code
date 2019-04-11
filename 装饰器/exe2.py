def outer(func):
    def inner(*args,**kwargs):
        print('call %s:'%func.__name__)
        return func(*args,**kwargs)
    return inner

@outer  #相当于now ===>outer(now)
def now():
    print ('2019-3-5')

now()


