_fibo=[]


def fibo():
    x=0
    s=1
    count = 0
    _fibo.append(x)
   
    for a in range(5):
        t = x
        x +=s
        s=t
        _fibo.append(x)
    _input = int(input("Enter : ")) 
    for f in range(1,len(_fibo)):
      
        if _input%f==0:
            count+=1
            print(f)
    print(_fibo)
    return count+1

print(fibo())