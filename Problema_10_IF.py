ng=int(input("Introduceti numarul de gaini : "))
nb=int(input("Introduceti numarul de boabe : "))
nbg=nb//ng
nbc=nb-(ng*nbg)
if (nbg>nbc) :
    print("Gaina mai mult cu : ",nbg-nbc,"boabe")
if (nbc>nbg) :
    print("Curcanul mai mult cu : ",nbc-nbg,"boabe")    
else :
    print("Primesc acelasi numar de boabe")