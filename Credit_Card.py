def odd_even2(file1):
    def odd_even1(s1):
        cc1 = s1
        len1 = len(cc1)
        odd = ""
        even = ""
        for i in range(0,len1//2,1):
            odd = odd + cc1[2*i]
        for i in range(0,len1//2,1):
            even = even + cc1[1+2*i]
        return (odd,even)

    f1 = open('city1.txt','a')
    f2 = open('city2.txt','a')
    f3 = open(file1,'r')
    for i in range(0,20,1):
        info1 = f3.readline()
        result = odd_even1(info1)
        cc_city1 = result[0]
        cc_city2 = result[1]
        print(cc_city1)
        f1.write(cc_city1)
        f1.write('\n')
        print(cc_city2)
        f2.write(cc_city2)
        f2.write('\n')

    f1.close()
    f2.close()

odd_even2('in5.txt')
odd_even2('in6.txt')
