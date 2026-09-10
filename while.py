print("=====program genap====")

awal =int(input("ketik nilai awal anda="))
selisih= int(input("ketik nilai selisihnya="))
akhir=int(input("ketik nilai akhir anda="))

while awal <= akhir:
    if awal % 2==0:
        print (awal)
    awal += selisih
