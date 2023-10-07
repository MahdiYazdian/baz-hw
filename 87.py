def function():
    arr = []
    numfor = int(input("enter : "))
    for n in range(numfor):
        num = int(input("Enter number :"))
        arr.append(num)
    
    arr.sort(reverse=True)
    for a in arr :
        print(a)

function()