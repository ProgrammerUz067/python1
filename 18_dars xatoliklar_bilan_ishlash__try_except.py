# try va except


# try:
#     son=int(input("son kiriting:"))
#     daraja=son**2
#     print(daraja)
# except:
#     print("iltimos son kiritining")



# try:
#     son1=int(input("1-sonni kiring:"))
#     son2=int(input("2-sonni kiring:"))
#     ayirma=son1/son2
#     print(ayirma)
# except ZeroDivisionError:
#     print("sonni nolga bolish mumkin emas")
# except ValueError:
#     print("iltimos faqat son kiriting")



# try:
#     yil=int(input("Joriy yilni kiriting:"))
#     yosh=int(input("yoshingizni kiriting:"))
#     yoshi=yil-yosh
#     print("siz",yoshi,"yilsiz")
# except ValueError:
#     print("iltimos faqat son kiriting:)")



# try:
#     yosh=int(input("Yoshingizni kiriting::"))
#     if yosh<12:
#         print("sizga kirish pepul")
#     elif yosh>12 and yosh<=18:
#         print("sizga kirish 5000so'm")
#     elif yosh>30 and yosh<=40:
#         print("sizga kirish 10000so'm")
#     elif yosh>=60:
#         print("sizga kirish bepul")
# except:
#     print("Faqat son kiriting:)")



# try:
#     mevalar=["olma","anor","uzum","anjir","bexi"]
#     print(mevalar[5])
# except IndexError:
#     print("bunday indeeksdagi ma'lumot yoq")



# try:
#     natija="Salom men Ramiz"
#     natija=natija+5
# except TypeError:
#     print("Matinga sonni qo'shib bo'lmaydi")




#uy ishi
# try:
#     hafta=input("hafta kunini kiriting:")
#     harorat=int(input("Havo haroratini kiriting"))
#     if hafta=="shanba" and hafta=="yakshanba" or harorat<=20:
#             print("bugun uyda dam olamiz")
#     elif hafta=="shanba" and hafta=="yakshanba" or harorat>21:
#             print("bugun toqqa dam olish uchun boramiz")
#     else:
#             print("bugun ish kuni")
# except ValueError:
#     print("iltimos haroratni son bilan yozing")






kun=input("hafta kunini kiriitng:")
if kun=="dushanba" and kun=="chorshanba" or kun=="juma":
    print("bugun dasturlash darsi bor kechikmasdan bor")





























