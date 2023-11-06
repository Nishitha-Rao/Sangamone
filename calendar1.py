def cal31():
    import calendar
    f1 = open("cal31.txt","w")
    months31 = [1,3,5,7,8,10,12]
    for i in months31:
        print(calendar.month(2023,i))
        f1.write(calendar.month(2023,i))
    f1.close()
def cal30():
    import calendar
    f1 = open("cal30.txt","w")
    months30 = [4,6,9,11]
    for i in months30:
        print(calendar.month(2023,i))
        f1.write(calendar.month(2023,i))
    f1.close()
def cal28():
    import calendar
    f1 = open("cal28.txt","w")
    months28 = [2]
    for i in months28:
        print(calendar.month(2024,i))
        f1.write(calendar.month(2024,i))
    f1.close()
def caln():
    days = int(input("number of days "))
    if days == 30:
        cal30()
    elif days == 31:
        cal31()
    elif days == 28:
        cal28()
    elif days == 29:
        cal28()
    else:
        print("Invalid input")

