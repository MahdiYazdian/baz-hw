arr= []

def founction():
   
    inputn = int(input("Enetr N : "))
    for num in range(inputn):
        number = int(input("Enter number : "))
        arr.append(number)

    arr.sort(reverse=True)
    return arr

def prin(arr =[]):
    for n in arr :
        print(n)
arr = founction()
prin(arr)