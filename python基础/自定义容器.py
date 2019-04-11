class FunctionalList:
    """
        实现了内置类型list的功能，并且丰富了一些其他方法：head，tail，init，last，drop，take
    """
    def __init__(self,value = None):
        if value is None:
            self.value = []
        else:
            self.value =value

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __iter__(self):
        return iter(self.value)

    def __reversed__(self):
        return FunctionalList(reversed(self.value))

    def append(self,value):
        self.value.append(value)

    def head(self):
        #获取第一个元素
        return self.value[0]

    def tail(self):
        #获取第一个元素之后的所有元素
        return self.value[1:]

    def inti(self):
        #获取最后一个元素之前的所有元素
        return self.value[:-1]

    def last(self):
        #获取最后一个元素
        return self.value[-1]

    def drop(self,n):
        #获取所有元素，除了前N个
        return self.value[n:]

    def take(self,n):
        #获取钱N个元素
        return self.value[:n]
