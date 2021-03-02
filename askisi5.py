#Αναγκαιο import για κανει randomize τον πινακα
import random

x = int(input("Αξονας x : "))
y = int(input("Αξονας y : "))

c = 0
#100 επαναληψεις για 100 ορθογωνια
for times in range (100):
    #Ορισμος Πινακα με αρχικη τιμη το κενο ("")
    sos = [["" for i in range(x)]for j in range (y)]

    #Γεμιζει πινακα με "Ο" και "S"
    for i in range (y):
        if (i%2==0):
            for j in range (x):
                if (j%2==0):
                    sos[i][j] = "O"
                else:
                    sos[i][j] = "S"
        else:
            for j in range (x):
                if (j%2==0):
                    sos[i][j] = "S"
                else:
                    sos[i][j] = "O"
    #Κανει randomize τον πινακα
    random.shuffle(sos)

    for i in range (y):
        #Κανει print μονο την 1η γραμμη ωστε ολες να ειναι η μια κατω απο την αλλη
        print (sos[i])

    #Εξεταζει αν υπαρχουν SOS καθετα
    kath = 0
    w=0
    for i in range (x):
        #Μονο αν τo y ειναι μεγαλυτερο ή ισο με το 3 μπορουν να υπαρχουν καθετα sos
        if (y>=3):
            for j in range (y-2):
                if (sos[j][w]=="S"):
                    if (sos[j+1][w]=="O"):
                        if (sos[j+2][w]=="S"):
                            kath+=1
            w+=1
    #Εξεταζει αν υπαρχουν SOS οριζοντια
    oriz = 0
    for i in range (y):
        #Μονο αν τo x ειναι μεγαλυτερο ή ισο με το 3 μπορουν να υπαρχουν οριζοντια sos
        if (x>=3):
            for j in range (x-2):
                if (sos[i][j]=="S"):
                    if (sos[i][j+1]=="O"):
                        if (sos[i][j+2]=="S"):
                            oriz+=1
    #Εξεταζει αν υπαρχουν SOS διαγωνια
    diag = 0
    #Μονο αν τo x και το y ειναι μεγαλυτερα ή ισα με το 3 μπορουν να υπαρχουν διαγωνια sos
    if (x>=3 and y>=3):
        for i in range (y-2):
            for j in range (x-2):
                if (sos[i][j]=="S"):
                    if (sos[i+1][j+1]=="O"):
                        if (sos[i+2][j+2]=="S"):
                            diag+=1

        print ("ΚΑΘΕΤΑ")
        print (kath)
        print ("ΟΡΙΖΟΝΤΙΑ")
        print (oriz)
        print ("ΔΙΑΓΩΝΙΑ")
        print (diag)
        print ("\n")
    #Προσθετει στην μεταβλητη c καθε φορα ποσα sos βρηκε στο ορθογωνιο
    c = c + (oriz + kath + diag)
#Μεσος Ορος
q = c/100
print ("ΜΕΣΟΣ ΟΡΟΣ :",q)
