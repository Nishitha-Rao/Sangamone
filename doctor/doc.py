def doc(text,html):
    f1 = open(text,"r")
    list1 = f1.readlines()
    f2 = open(html,'r')
    info1 = f2.read()
    for element in list1:
        with open(f"{element.rstrip()}.html","w") as file:
            file.write(info1.replace("DOCTOR",element))
        #print(info1.replace("DOCTOR",element))
doc("Doctors.txt","1.html")
