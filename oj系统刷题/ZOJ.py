while True:
    x=input()
    if x=="E":
        break
    else:
        z=[]
        o=[]
        j=[]
        str1=""
        num_z=0
        num_o=0
        num_j=0
        x_str=" ".join(x)
        x_list=x_str.split()
        for i in range(len(x_list)):
            if x_list[i]=="Z":
                num_z+=1
                z.append(x_list[i])
            elif x_list[i]=="O":
                num_o+=1
                o.append(x_list[i])
            elif x_list[i]=="J":
                num_j+=1
                j.append(x_list[i])
        num_max=max(num_z,num_o,num_j)
        for num1 in range(num_max-num_z):
            z.append(" ")
        for num2 in range(num_max-num_o):
            o.append(" ")
        for num3 in range(num_max-num_j):
            j.append(" ")
        for a,b,c in zip(z,o,j):
            str1+=a
            str1+=b
            str1+=c
        str2=str1.replace(" ","")
        print(str2)










