# # """ While sikli """

# i=1

# while i>5:
#     print(i)
#     i+

savol="Istalgan son kiriting \n"
savol+="toxtatish uchun (exit) :"
ishora=True




while ishora:
    qiymat=input(savol)
    if qiymat=="exit":
        ishora=False
    else:
        qiymat=float(qiymat)
        print(f"{qiymat} ning kvadrati {qiymat**2}")





# 2-yo'li
# while True:
#     qiymat=input(savol)
#     if qiymat=="exit":
#         break
#     else:
#         qiymat=float(qiymat)
#         print(f"{qiymat} ning kvadrati {qiymat**2}")






# uy ishi
runlist=["Mango","Aplle","Orange","Guava"]
matn=input("Siz mevalar ro'yxatini ko'rmoqchimisiz unda (y) kiriting\n . Agar to'xtatishni xoxlasangiz (stop) kiriting :")
ishora=True


while ishora:
    if matn=="stop":
        ishora=False
    elif matn=="y":
        print(runlist)
    else:
        print("Amalingiz xato iltimos boshqatdan urinib ko'ring")





number=[12,45,68,7,45,150,48,500,30,25]

y=[]

for son in number:
    if son%5==0:
        y.append(son)
    else:
        pass

print(y)






str1="Biror matn kiriting"
str1+="Toxtatish uchun (stop) :"
ishora=True



while ishora:
    matn=input(0)
    if matn.isalpha():
        print(matn)
    elif matn.isalnum():
        pass
    elif matn=="stop":
        ishora=False
    else:
        print("Xatolik yuz berdi iltimos boshqatdan urining")




i=1

while i<11:
    print(i)
    i+=1








name={"Teador":19,"Osman":24,"Kril":51}



katta=max(name.keys())
kichik=min(name.keys())


print(katta,kichik)

















