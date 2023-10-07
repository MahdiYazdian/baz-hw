

arr = []
def function():
    
    numfor = int(input("enter : "))
    for n in range(numfor):
        num = int(input("Enter number :"))
        arr.append(num)
    
    arrcheck = []
    for n in arr:
        arrcheck.append(n)
    arrcheck.sort(reverse =False)
    
    
    for a in range(len(arr)) :
       
        if arr[a]!=arrcheck[a]:
            return False
        else:
            return True
    
        

print(function())