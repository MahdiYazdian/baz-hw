
arr =[]
def function():
    
    for n in range(10):
        inp = int(input("Enter Number "+str(n+1)+" : "))
        arr.append(inp)
        
    for av in arr:
        
        for a in range(2,av):
            Isavval  = True  
            if av%a==0 :
                print(av)
                break  
function()