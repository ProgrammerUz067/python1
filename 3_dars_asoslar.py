# 3-dars python asoslari


#1
son=int(input("Iltimos son kiriting <>"))
if son%3==0:
    print("Tabiklaymiz bu to'gri javob")
elif son%5==0:
    print("Amal to'gri bajarildi !")
elif son%7==0:
    print("Siz to'gri topdingiz")
else:
    print("Afsuski siz xatoga yo'l qo'ydingiz")



#2
num1=int(input("Xoxlagan soningizni kiriting :"))
if num1<10:
    print("Bu 1 xonali son")
elif num1<100:
    print("Bu 2 xonali son")
elif num1<1000:
    print("bu 3 xonali son")
else:
    print("Iltimos amallarni yana bir bor tekshirib ko'ring")



#3
soz=input("Biror bir so'z kiriting >")
matn=soz[::-1]
if soz==matn:
    print("Bu palidrom so'z ")
else:
    print("bu palidrom so'z emas")
















