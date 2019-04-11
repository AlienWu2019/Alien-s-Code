S=input()
len_S=len(S)
content=[]
A=[]
for i in range(len_S+1):
    content.append(i)
for i in range(len_S):
    if S[i] == "I":
        A.append(content[0])
        content.remove(content[0])
    elif S[i] == "D":
        A.append(content[-1])
        content.remove(content[-1])
A.append(content[0])
print(A)


