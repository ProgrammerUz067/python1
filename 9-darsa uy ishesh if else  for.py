son=int(input("son kiriting>>"))
if son>0:
    print("bu musmat son")
else: 
    print("bu manfi son")
    
sonlar=int(input("son kiriting>>"))    
if  sonlar%2==0:
    print("bu yuzgacha son>>")
else:
    print("bu katta son")
    
  
    

x=int(input("nechi karrani xisoblaymiz>>"))
sonlar=list(range(1,11))

for son in sonlar:
    natija=x*son
    print(x,"*",son,"=",natija)
    print(f"{x}*{son}={natija}")
    
    
    
    x=int(input("nechi sonini yig'indisini xisoblaymiz>>"))
    sonlar=list(range(1,11))

    for son in sonlar:
        natija=x+son
    print(x,"+",son,"=",natija)
    print(f"{x}+{son}={natija}")
    
son=int(input("son kiriting>>"))
if son==list(range(2,101,2)):
    print("buni oxiri toq son")
else:
    print("buni oxiri toq son")
    
    
    
    