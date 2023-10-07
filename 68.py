def func():
    count =0
    inp = input("Enter : ")
    for n in inp:
        if n == '0':
            count+=1
    return count

print(func())