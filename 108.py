
arr =[]
def function():
    avval =0
    Isavval  = True
    n = int(input("Enetr n :"))
    for n in range(n):
        inp = int(input("Enter Number "+str(n+1)+" : "))
        arr.append(inp)
    for av in arr:
        for a in range(2,av):
               
            if av%a==0:
                Isavval=False
                break
            else:
                Isavval=True
        if Isavval ==True :
            avval+=1
    return avval
            
                

   
print(function())