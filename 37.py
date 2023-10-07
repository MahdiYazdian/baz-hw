
arr=[]


def best():
    for num in range(3):
      number = int(input("Enter your number :"))
      arr.append(number)
    arr.sort(reverse=True)
    for num in arr:
       print(num)

best()      

 