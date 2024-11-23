davlatlar={"amerika":"vashington","o'zbekiston":"toshkent","italia":"rim","turkiya":"istanbul","unit kingdom":"longon"}
matn=input("shu ro'yxatdan biron bir davlatni kiriting<<")
print("siz tanlagan davlatning poytaxti",davlatlar[matn])



menyu={"zarhal":"menyusi 15t","istiqlol":"menyusi 23","sarob":"menyusi 28","salomat ota":"menyusi 34","italiano":"menyusi 49"}
print(menyu)
tanla=input("shu ro'yxatga asosan biror bir restoranni tanglang>>")
print("siz tanlagan restoran",menyu[tanla])



yosh=int(input("yoshingizni kiriting>>"))
ism=input("ismingizni kiriting>>")
telefon=int(input("Telefon raqamingizni kiriting>>"))



if yosh>0:
    ishora="yosh"
else:
    print("iltimos yoshni boshqatdan kiriting:")

if ism==ism: 
    ism=ism
else:
    print("iltimos ismingizni boshqatdan kiriting:")


if telefon>0:
    nomer=telefon
else:
    print("iltimos telefon raqamni boshqatdan kiriting:")


malumot_foydalanuvchiniki={
    "yosh":yosh,
    "ism":ism,
    "telefon_raqami":nomer
     }
print(malumot_foydalanuvchiniki)







