while True:
    N = int(input())
    if N == 0:
        exit()
    else:
        string1 = input()
        string2 = input()
        string1_list = string1.split()
        string2_list = string2.split()
        string1_list_new = []
        string2_list_new = []
        count = 0
        if len(string1_list)==N and len(string2_list)==N:
           for i in string1_list:
               string1_list_new.append(int(i))
           for j in string2_list:
               string2_list_new.append(int(j))
           string1_list_new.sort()
           string2_list_new.sort()
           for i in string1_list_new:
               for j in string2_list_new[::-1]:
                   if i-j>0:
                       count+=1
                       string1_list_new.remove(i)
                       string2_list_new[::-1].remove(j)
                       continue
           if count>int(N/2):
               print('YES')
           else:
               print('NO')



















