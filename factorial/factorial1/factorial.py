def find_factorial():
    def fact(n):
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    factorial =[]    
    for i in range(1,6,1):    
        factorial.append(fact(i))
    return factorial