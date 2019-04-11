from dns import resolver

domain = input()

A = resolver.query(domain,"A")

for i in A.response.answer:
    for j in i.items:
        print(j)