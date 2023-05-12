class dosya():
    def __init__(self):
        with open("C://Users//metec//OneDrive//Masaüstü//Workspace//YAZILIM KODLAMA//Kodlama Egzersizleri 12. Bölüm//metin1.txt","r",encoding = "utf-8") as  file:
            dosyadakiler = file.read()
            # print(dosyadakiler)
            kelimeler = dosyadakiler.split(" ")
            self.sadece_kelime = list()

            for i in kelimeler:
                i = i.replace("\n", "")
                i = i.replace(" ", "")
                i = i.replace(".", "")
                i = i.replace(",", "")
                self.sadece_kelime.append(i)
        
    def bütün_kelimeler(self):
        kelimelerküme = set()

        print("Tüm Kelimeler....")
        for i in self.sadece_kelime:
            kelimelerküme.add(i)


            for i in kelimelerküme:
                print(i)

                # print("*********************************\n*********************************") 
                    
        print("Kelimelerden Kaç adet basıldığına geçiliyor....\n")


    def frekans(self):
        sözlük = dict()

        for i in self.sadece_kelime:
            if (i in sözlük):
                sözlük[i] += 1
            else:
                sözlük[i] = 1 

        for kelime,sayı in sözlük.items():
            print("{} kelimesi {} defa geçiyor".format(kelime,sayı)) 
            print("*********************************************************")
        

dosya = dosya() 
dosya.bütün_kelimeler()        
dosya.frekans()