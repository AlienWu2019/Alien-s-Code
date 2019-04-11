from datetime import datetime


def timer(func):
    '''Function Level Timer via Decorator'''

    def timed(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        elapse = (end - start).total_seconds()
        print("Processing time for {} is: {} seconds".format(func.__name__, elapse))
        return result

    return timed


@timer
def test_1(a,b):
    '''Function Level'''
    a *= 2
    b *= 3
    return a,b


if __name__ == '__main__':
    print(test_1(1,3))
