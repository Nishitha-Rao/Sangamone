import datetime as dt
wordlist1 = [['apple', 'area', 'ant', 'away'], ['ball', 'bad','bat', 'bag', 'bounce'], ['cat', 'camel', 'carrot', 'cabbage'], ['donkey', 'driver', 'drink', 'decimal'], ['eagle', 'elephant', 'enter', 'egg'], ['flag', 'flutter', 'fume', 'funny'], ['gang', 'grapes', 'gender', 'garden'], ['hospital', 'holiday', 'hunger', 'hostel'], ['ink', 'injection', 'injury', 'icecream'], ['juice', 'jewel', 'jump', 'judge'], ['kitten', 'kite', 'kick', 'knowledge'], ['lemon', 'light', 'length', 'laugh'], ['mentor', 'manager', 'macro', 'mouth'], ['net', 'nest', 'nothing', 'north'], ['orange', 'omit', 'original', 'owner'], ['principle', 'prince', 'provide', 'print'], ['queen', 'quiz', 'quit', 'question'], ['rest', 'roller', 'ring', 'republic'], ['state', 'strategy', 'steel', 'sound', 'symbol', 'sarcastic', 'surround', 'seven'], ['towel', 'tap', 'ten', 'ticket'], ['umbrella', 'unable', 'ugly', 'umpire'], ['verb', 'vendor', 'violin'], ['whistle', 'west', 'wood', 'wonder', 'warning'], ['xerox', 'xylophones', 'xylose', 'xyster'], ['yellow', 'young', 'yeast', 'yeah'], ['zoo', 'zoom', 'zone', 'zebra']]
#wordlist2 list will be used by the computer
wordlist2 = wordlist1
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,10,1):
    #to determine the time before entering the input
    today1 = dt.datetime.now()
    print(today1)
    #to determine the time after entering the input
    input1 = input("enter word: ")
    today2 = dt.datetime.now()
    print(today2)
    diff1 = (today2 - today1).seconds
    print(diff1)
    #to check if the user has entered the word within 5 seconds
    if diff1 > 5:
        print("WARNING! you have exceeded the time limit")
    #to find the length of the word
    len1 = len(input1) 
    firstchar = input1[0:1]
    #after finding the first character, find its index position in the wordlist
    indexfirst = alpha.index(firstchar)
    #in the currentlist add the elements beginning from the charecter firstchar
    currentlist = wordlist2[indexfirst]
    #after getting the input from the user remove that element from the currentlist
    if input1 in currentlist:
        currentlist.remove(input1)
    
    #find the last character of the input1 which was entered by the user
    lastchar1 = input1[len1-1:len1]
    # find the position of the last char in the alpha list
    position1 = alpha.index(lastchar1)
    # templist1 contains the list of words beginning from the letter lastchar
    templist1 = wordlist2[position1]
    #input2 will have the first element of the templist 
    input2 = templist1[0]
    firstchar = input2[0:1]
    indexfirst = alpha.index(firstchar)
    currentlist = wordlist2[indexfirst]
    #after getting the input from the computer remove that element from the currentlist
    if input2 in currentlist:
        currentlist.remove(input2)
    #print both user's as well as computer's word
    print(input1,input2)

