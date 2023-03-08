def hitung_mobil() :
    done = False
    while done == False :
        asal = input('Masukan asal mobil (ketik "done" untuk keluar) : ')
        if asal == "solo" :
            asal1 = asal.lower()
            l = list(asal1)
            solo = asal1.count(asal1)
            solo += l
            done = False
        # elif asal == "jogja" :
        #     asal1 = asal.lower()
            
        #     jogja1 = asal1.count(asal1)
        #     done = False
        elif asal == "done" :
            done = True
            print(solo)
            # print(jogja1)  
       
hitung_mobil()