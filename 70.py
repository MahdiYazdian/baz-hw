numbers = []
magh =[]

def num():
    for n in range(56,1984+1):
        for m in range(1,n):
            if n%m==0:
                print(str(n) +"  maghsom : "+str(m))

num()