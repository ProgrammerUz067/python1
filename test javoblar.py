#1.b
#2.c
#3 def teskari_son(x):
#     teskarisi=x[::-1]
#     print(teskarisi)

# teskari_son("134")



#5 birinchi=lambda matn:matn[0]
# print(birinchi("Ramiz"))



#6 first_harf=lambda matn:matn[-1]
# print(first_harf("Ramiz"))




#8 def daraja(x,n):
#     natija=x**n
#     print(natija)

# daraja(10, 2)





#9 for a in list(range(1,11)):
#            print(a)


#10 def matn_uzun(matn):
#     uzunlik=len(matn)
#     print(uzunlik)

# matn_uzun("Raniz")




#11 def malumot_info(ism,familiya):
#     info={
#         "ism":ism,
#         "familiya":familiya
#         }
#     return info

# print(malumot_info("ramizjon","ziyodullayev"))




#13 def taxi(km,vaqt):
#     if km>3 and vaqt>10:
#         print("sizga taxi kerak")
#     else:
#         print("sizga taxi kerakmas")







# yosh=int(input("yoshingizni kiriting:"))
# ism=input("ismingizni kiriting:")
# ema=input("emailingizni kiriting:")
# if yosh<18 or ema not in "@":
#     print("sayitga xush kelibsiz")
# else:
#     print("sayitga kirish taqiqlanadi xatolik bor")







#15 son=int(input("son kiriting:"))
# if son%2==0:
#     print("juft son")
# else:
#     print("toq son")









# def revers(num:int)->None:
#     result=0
#     ishora=1 if num>=0 else -1
#     while num!=0:
#         result=result*10+num%10
#         num//=10
#     return result*ishora

# print(revers(548))



# def print_digt(num:int)->None:
#     while num!=0:
#         digit=num%10
#         print(digit)
#         num//=10
# print(print_digt(1485))





# def two(list1,list2):
#     result=[]
#     for number in list1:
#         if number in list2:
#             result.append(number)
#     return result







































