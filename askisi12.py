
file = input("give an ascii file ") #Ζηταει απο τον χρηστη ενα file
for i in range(len(file)):
    let = file[len(file)-i -1] #Διαβαζει απο το τελος τους χαρακτηρες
    num = ord(let) # μετατροπη σε αριθμους
    num2 = 128 - num # κατοπτρικο τους
    ascii = chr(num2) # Τον μετατρεπω σε χαρακτηρα
    print(ascii , end ="")
