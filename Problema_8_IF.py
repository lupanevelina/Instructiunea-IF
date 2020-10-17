a=int(input("Itroduceti un numar : "))
b=int(input("Itroduceti un numar : "))
if (a%2==0) and (b%2==0) :
    if a>b :
        print(a)
    else:
        print(b)    
if (a%2==0) and (b%2!=0) :
    print(a)
if (a%2!=0) and (b%2==0) :
    print(b)
if (a%2!=0) and (b%2!=0) :
    print("nu avem numere pare")    