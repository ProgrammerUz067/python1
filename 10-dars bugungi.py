# sonlar=list(range(1,11))x=1
# 
# for son in sonlar:
#    x=x*son
# print(x)


#malumotlar={"ism":"Ramizjon","yosh":14}
# print(malumotlar["manzili"])
# print(malumotlar["ism"])
#ism=malumotlar["ism"]
#yosh=malumotlar["yosh"]
#print("sizning ismingiz",malumotlar["ism"],"sizning yoshingiz",malumotlar["yosh"])
#print(f"sizning ismingiz {ism} sining yoshingiz {yosh} da")




#lug'at
dostlar={"alisher":12,"doston":13,"oybek":16,"jo'rabek":12,"azizbek":15}
#lug'atni o'zgartirish
# dostlar["alisher"]=14
#
# #lug'atdan o'chirish
# del dostlar["doston"]
# #lug'attni tozalash
# dostlar.clear()
for kalit,qiymat in dostlar.items():
    print(f"sizning ismingiz {kalit} yoshingiz {qiymat} da")

davlatlar={"amerika":"vashington","o'zbekiston":"toshkent","italia":"rim","turkiya":"istanbul","unit kingdom":"longon"}
# amer=davlatlar["amerika"]
# uzb=davlatlar["o'zbekiston"]
# ital=davlatlar["italia"]
# turk=davlatlar["turkiya"]
# uk=davlatlar["unit kingdom"]
# print(f"o'zbekistonning poytaxti {uzb}")
# print(f"italiyaning poytaxti {ital}")
# print(f"turkiyaning poytaxti {turk}")
# print(f"unit kingdomning poytaxti {uk}")

#chiqarishni oson yo'li
for kalit,qiymat in davlatlar.items():
    print(f"{kalit} ning poytaxti {qiymat}")






