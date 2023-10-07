arr = []


for i in range(3):
    x=input("Enter your number :")
    arr.append(x)

def best(x=[]):
    bes = x[0]
    for n in x:
        if n>bes:
            bes=n
    return bes

print(best(arr))

