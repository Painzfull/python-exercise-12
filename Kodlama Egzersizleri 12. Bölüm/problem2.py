
file = open("C://Users//metec//OneDrive//Masaüstü//Workspace//YAZILIM KODLAMA//Kodlama Egzersizleri 12. Bölüm//mailler.txt","r",encoding ="utf-8")
file2 = open("C://Users//metec//OneDrive//Masaüstü//Workspace//YAZILIM KODLAMA//Kodlama Egzersizleri 12. Bölüm//mailleryeni.txt","w", encoding = "utf-8")

for satır in file:
    satır = satır[:-1]
    if(satır.endswith(".com") and satır.find("@") != -1):
        file2.write(satır + "\n")

file.close()           
file2.close()



