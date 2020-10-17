n1=int(input("introduceti nr elevului : "))
n2=int(input("introduceti nr elevului : "))
n3=int(input("introduceti nr elevului : "))
p1=int(input("introduceti punctajul elevului : "))
p2=int(input("introduceti punctajul elevului : "))
p3=int(input("introduceti punctajul elevului : "))
if (p1<p2) and (p1>p3):
    print("Punctaj maxim are elevul cu numarul ",n1)
if (p2>p1) and (p2>p3):
     print("Punctaj maxim are elevul cu numarul ",n2)
if (p3>p1) and (p3>p2):   
     print("Punctaj maxim are elevul cu numarul ",n3)  
if (p1==p2) and (p1>p3) and (p2>p3):  
    print("Elevii cu numarul",n1,"si",n2,"au acelasi punctaj")      
if (p1==p3) and (p1>p2) and (p3>p2):  
    print("Elevii cu numarul",n1,"si",n3,"au acelasi punctaj")
if (p2==p3) and (p2>p1) and (p3>p1):  
    print("Elevii cu numarul",n1,"si",n3,"au acelasi punctaj")   