def best():
    week = int(input("Enter your Week :"))
    if week<=7:
        print("first week")
    elif week>7 and week <=14 :
        print("two week")
    elif week>14 and week <=21 :
        print("three week")
    elif week>21:
        print("four week")

    
best()      
