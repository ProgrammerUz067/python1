# Today lesson funksions

# def yegindi(*sonlar):
#     pass


# son1=yegindi(3,4,6)

# print(son1)


#uy ishi

def calc(x,y):
    """ Bu funksiya ikala sonni to'rt xil amalda chiqarib beradi"""
    natija=x+y,x-y,x*y,x/y
    print(natija)

calc(5, 4)




def maxsum(x,y):
    """  Funksiyaga istalgan sonni kiritsa uning ko'paytmasini va o'rtacha arifmetigini chiqarib beradi"""
    natija1=x*y
    natija2=x*y/2
    print(f'sonlarning kopaytmasi {natija1},ortacha arifmetigi {natija2}')
    
    
maxsum(4, 2)




def maxmin(x,y):
    """ This funksion to find max end min numbers """
    katta=max(x,y)
    kichik=min(x,y)
    print(f' Sonlarning eng kattasi {katta} kichigi {kichik} ')

maxmin(457,447)






# def alfa(son):
#     """ Bu funksiya bitta sonni toq yoki juft ekanligini aniqlaydi """
#     if son/2==0:
#         print(f'{son} juft son')
#     elif son/3==0:
#         print(f'{son} toq son')
#     else:
#         print("Iltimos amalingizni boshqatdan tekshiring")


# alfa(2)



def son(x):
    """ Bu funksiya x ning kvadrati va kubini hisoblaydi"""
    kvatrat=x**2
    kub=x**3
    print(f' {x} ning kvadrati {kvatrat}  kubi esa {kub}')


son(2)





def teskari(matn):
    """ Bu funksiyaning vasifasi matnni teskarisini chiqarib beradi"""
    teskarisi=matn[::-1]
    print(teskarisi)
    
    
    
teskari("Ramiz")




