xa=int(input("Introduceti numarul de bile albe mici : "))
xr=int(input("Introduceti numarul de bile rosii mici : "))
xv=int(input("Introduceti numarul de bile verzi mici : "))
ya=int(input("Introduceti numarul de bile albe mari : "))
yr=int(input("Introduceti numarul de bile rosii mari : "))
yv=int(input("Introduceti numarul de bile verzi mari : "))
xt=xa+xr+xv
yt=ya+yr+yv
print("Totalul bilelor : ",xt+yt)
if (xt>yt) :
    print("Mici : ",xt)
if (xt<yt) :
    print("Mari : ",yt)    
else:
    print("numar egal de bile")    
if (xa+ya>xr+yr) and (xa+ya>xv+yv) : 
    print("Albe : ",xa+ya,"bile")
if (xr+yr>xa+ya) and (xr+yr>xv+yv) : 
    print("Rosii : ",xr+yr,"bile")
if (xv+yv>xa+ya) and (xv+yv>xr+yr) : 
    print("Verzi : ",xv+yv,"bile")
if (xa+ya==xr+yr)and (xa+ya>xv+yv) :
    print("Albe si rosii :  ",xa+ya,"bile")    
if (xa+ya==xr+yr)and (xa+ya<xv+yv) :
    print("Verzi : ",xv+yv,"bile")        
if (xa+ya==xv+yv)and (xa+ya>xr+yr) :
    print("Albe si verzi : ",xa+ya,"bile")        
if (xa+ya==xv+yv)and (xa+ya<xr+yr) :
    print("Rosii :  ",xr+yr,"bile") 
if (xr+yr==xv+yv)and (xr+yr>xa+ya) :
    print("Rosii si verzi : ",xr+yr,"bile") 
if (xr+yr==xv+yv)and (xr+yr<xa+ya) :
    print("Albe :",xa+ya,"bile") 