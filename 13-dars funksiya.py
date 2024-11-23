#funksiya

# def hellow():
#     """inglischada salom berauvchi funksiya"""
#     print("hellow")
#
# hellow()

#birinchi misolimiz





# def tanishtir(ism,familya):
#     """
#     bu funksiya insonga o'zining ismini familiyasini
#     yoshini olib unga salom beradi
#     """
#
#     print(f"Asalomu aleykum {ism.title()} {familya.title()}")
#
# tanishtir("ramizjon","ziyodullayev")




# def yosh_hisobla(joriy_yil,t_yil):
#     """
#     bu funksiya insonning yoshini
#      xisoblab beradi
#     """
#     yosh=joriy_yil-t_yil
#     print(f"sizning yoshingiz {yosh} da")
#
# yosh_hisobla(2023,2009)





# def yigindi(x,y):
#     """iki sonning yig'indisini hisoblab beruvchi funksiya"""
#     natija=x+y
#     print(natija)
#
# yigindi(120,23)





def ayirma(x,y):
    """iki soning ayirmasini hisoblab beradi"""
    natija=x-y
    print(natija)

ayirma(13,3)




def kopaytma(x,y):
    """iki soning ko'paytmasini hisoblab beradi"""
    natija=x*y
    print(natija)

kopaytma(2,2)






def bolinma(x,y):
    """iki soning bo'linmasini hisoblab beradi"""
    natija=x/y
    print(natija)

bolinma(10,5)







def kattani_hisob(x,y):
    """iki soning qaysi biri kataligini hisoblab beradi"""
    print(max(x,y))

kattani_hisob(2000,100)






def kichik_hisob(x,y):
    """iki soning qaysi biri kichikligini hisoblab beradi"""
    if x>y:
        natija=x
    else:
        natija=y
    print(natija)
kichik_hisob(1000,234)




def darajani_h(x,y):
    """iki soning kvadratini  hisoblab beruvchi funksiya"""
    natija=x**y
    print(natija)

darajani_h(100,2)




def teskari_matn(matn):
    """nima matin kiritsak shuni teskarisini hisoblab beradi"""
    teskarisi=matn[::-1]
    if matn !=teskarisi:
        natija="siz kiritgan so'zning teskarisi yo'q"
    else:
        print(matn[::-1])
    print(teskarisi)

teskari_matn("ikki")





