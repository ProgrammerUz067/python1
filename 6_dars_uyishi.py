
# st1="PyNaTive"

# kichik_harflar=[ i for i in st1 if i.islower()]
# katta_harflar=[ i for i in st1 if i.isupper()]



# natija="".join(kichik_harflar+katta_harflar)
# print(natija)



# """ Diction lug'atlar """

# davlatlar={
#     "Italiya":"rim",
#     "Fransiya":"parij",
    
# }



# davlatlar["italiya"]="Rim"

# # lug'atni o'zgartirish update

# davlatlar.update({"Italiya":"Napoli","Ispaniya":"Madrid"})


# # lug'atni o'chirish del


# del davlatlar["Italiya"]
# print(davlatlar)


# # lug'atlarni butunlay o'chirish clear()



# # davlatlar.clear()

# print(davlatlar["Fransiya"])








# # get() method

# print(davlatlar.get("Italiya","bunday kalit so'z yo'q"))



# # for davlat in davlatlar:
# #     print(f" {davlat} ning poytaxti {davlat[davlat]}")




# # items( methodi)

# for davlat,poytaxt in davlatlar.items():
#     print(f"{davlat} ning poytaxti {poytaxt}")



# # keys()
# print(davlatlar.keys())


# # values()


# print(davlatlar.values())



# popitems()

# print(davlatlar.popitems())


# # pop()

# print(davlatlar.pop("italiya"))




""" Quiz game"""

user1=input("1-ishtirokchi ismingizni kiriting >")
user2=input("2-ishtirokchi ismingizni kiriting >")


# oyinchilarning natijasi hisoblash uchun o'zgaruvchi
user1_score=0
user2_score=0



# ishtirokchilar uchun savollar tuzamiz
savollar=[

    
    {
     "savol":"2**3 ?",
     "javoblar":["8","16","24"],
     "t_javob":"8"
     },
    {
     "savol":"Amir Temur qachon tug'ulgan",
     "javoblar":["1336","1226","2345"],
     "t_javob":"1336"
     },
    {
     "savol":"Python dasturlash tili qanday til",
     "javoblar":["dinamik","statik","o'zgarmas"],
     "t_javob":"dinamik"
     },
    {
     "savol":"3**3 ?",
     "javoblar":["85","27","9"],
     "t_javob":"27"
     },



]


# savollarni konsolga chiqaramiz !


for i,savol in enumerate(savollar,start=1):
    print(f"{i}-savol {savol['savol']}")
    for k,j in enumerate(savol['javoblar'],start=1):
        print(f"{k}) {j}")
    
    
    # foydalanuvchidan savollarga javob olamiz
    if i%2==0:
        javob=input(f"{user1} javobingizni kiriting")
    else:
        javob=input(f"{user2} javobingizni kiriting")

    # TO'G'RI JAVOBNI TEKSHIRAMIZ
    if javob==savol['t_javob']:
        print("To'g'ri javob berdingiz ")
        if i%2==0:
            user1_score+=1
        else:
            user2_score+=1
    else:
        print("Noto'g'ri javob berdingiz !!!")



print("O'yin tugadi")
print("------------------------------------")
print(f"{user1} ning natijasi {user1_score} ta tog'ri javob")
print(f"{user2} ning natijasi {user2_score} ta tog'ri javob")





if user1_score>user2_score:
    print(f"Bu o'yining g'olibi {user1}")
elif user1_score==user2_score:
    print("Bu o'yinda do'stlik g'alaba qozondi !")
else:
    print(f"Bu o'yinning g'olibi {user2}")











