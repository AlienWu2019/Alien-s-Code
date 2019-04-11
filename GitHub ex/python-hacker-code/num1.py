def sum(string_num1,string_num2):
    int_num1 = integer_num(string_num1)
    int_num2 = integer_num(string_num2)
    result = int_num1+int_num2
    return result

def integer_num(string_num):
    int_num = int(string_num)
    return int_num

a = sum("5","1")
print(a)