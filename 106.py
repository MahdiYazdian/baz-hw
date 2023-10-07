def fountion():
    zooj = 0
    for num in range(5):
        number = int(input("Enter number : "))
        if number%2==0:
            zooj+=1
    return zooj

print(fountion())