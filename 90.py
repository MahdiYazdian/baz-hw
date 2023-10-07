import math

def founction():
    arr = []
    inputn = int(input("Enetr N : "))
    for num in range(inputn):
        number = int(input("Enter number : "))
        arr.append(number)
        
    for pr in arr:
        print(str(pr) + " factorial : "+str(math.factorial(pr)))

founction()