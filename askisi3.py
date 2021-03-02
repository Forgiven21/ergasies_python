#Αναγκαια import
import time, datetime, json, urllib.request

#Ημερομηνιες
date_today = datetime.datetime.today().strftime ('%d%m%Y')
day = datetime.datetime.today().strftime ('%d')
month = datetime.datetime.today().strftime ('%m')
year = datetime.datetime.today().strftime ('%Y')
var = datetime.datetime.now()
time_today = var.strftime("%H:%M:%S")
imerominia = int(day)

#Συναρτηση που πηγαινει στο site του opap και αποθηκευει τους αριθμους του κινο
def numbers(nm):
    link = f"https://api.opap.gr/draws/v3.0/1100/{kino[0]}" #Το 0 ειναι η 1η κληρωση της ημερας
    o = urllib.request.urlopen(link)
    p = o.read()
    p = p.decode()
    kin = json.loads(p)
    return kin[nm]["list"]

#Αρχικοποιηση πινακα
x = imerominia*20
table = [0]*x

#Επαναληψεις μεχρι και την σημερινη ημερα
j = 0
for i in range (1, imerominia+1):
    d = f'{year}-{month}-{i:02d}'
    link2 = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{d}/{d}/draw-id" #Link στο site του οπαπ στο κινο
    o1 = urllib.request.urlopen(link2)
    p1 = o1.read()
    p1 = p1.decode()
    kino = json.loads(p1)
    #Αποθηκευση αριθμων στον πινακα
    for y in range (20):
        table[j] = (numbers("winningNumbers")[y])
        j+=1
    print (numbers("winningNumbers"))

#Count ωστε να εμφανιστει το ποσοστο των αριθμων
for i in range (1, 81):
    print (i, "=", table.count(i), "φορα/ες")
