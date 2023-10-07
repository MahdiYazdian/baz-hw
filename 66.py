_input =[]
_fibo=[]
printbool = False

def inp():
    for num in range(100):
        x = int(input("Enter number :"))
        _input.append(x)

def fibo():
    x=0
    s=1
    _fibo.append(x)
   
    for a in range(50):
        t = x
        x +=s
        s=t
        _fibo.append(x)
    
def setnumber(_input =[],_fibo=[]):
    for num in _input:
        if num%2!=0 :
            for n in _fibo:
                if n == num:
                    printbool =True
                    print(num)
                    break


inp()
fibo()
setnumber(_input,_fibo)

