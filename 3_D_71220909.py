import math
def helikopter():
    i = 0
    while i == 0 :
        jAwal = int(input("Masukan jarak awal >>> "))
        
        if jAwal > 1 :
            e1 = int(input("Masukan sudut elevasi pada menit ke-5 (dalam derajat) : "))
            e2 = int(input("Masukan sudut elevasi pada menit ke-6 (dalam derajat) : "))
            TinggiAwal = jAwal * math.tan(math.radians(e1))
            print(round(TinggiAwal, 2),"meter")
            jAkhir = jAwal * math.tan(math.radians(e2)) - math.tan(math.radians(e1))
            SelisihKetinggian = jAkhir * math.tan(math.radians(e2))
            print(round(SelisihKetinggian, 2),"meter")
            i = 0
        elif jAwal == 0 :
            print("program dihentikan")
            i = 1


helikopter()

