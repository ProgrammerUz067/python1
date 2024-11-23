def t_matn(matn):
    """matin qabul qilib teskariga o'girib beradi"""
    teskarisi=matn[::-1]
    print(teskarisi)
    
t_matn("ramiz")



def kopaytma(x,y):
    """kiritilgan sonlarni ko'paytiradi"""
    natija=x*y
    print(natija)
    
kopaytma(5,5)



def katta(x,y):
    """kiritilgan sonlarni eng kattasini hisoblaydi"""
    if x>y:
        natija=x
    else:
        natija=y
    print(natija)

katta(123,45)


def kichik(x,y):
    """kiritilgan sonlarning eng kichigini hisoblaydi"""
    if x>y:
        natija=y
    else:
        natija=x
    print(natija)
    
kichik(1457,6985)




def k_harf(matn):
    """matn kiritganda uni kichik harflarga aylanadi"""
    kichik=matn.lower()
    print(kichik)
    
k_harf("RaMiZ")
















