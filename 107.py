def fountion():
    avvrage = 0
    arr =[]
    for num in range(5):
        number = int(input("Enter number : "))
        avvrage+=number
        arr.append(number)
    avvrage = avvrage/5
    for num in arr:
        
        if num - avvrage>=3:
            print(num)


fountion()