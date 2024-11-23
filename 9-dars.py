# son=int(input("son kiriting>>"))
# if son%2==0:
#     print("juft son")
# else:
#     print("toq son")
#
# son1=int(input("birinchi sonni kiriting>>"))
# son2=int(input("ikinchi sonni kiriting>>"))
# son3=int(input("uchinchi sonni kiriting>>"))
# if son1>son2 and son1>son3:
#     print(son1,"eng katta")
# elif son2>son1 and son2>son3:
#     print(son2,"eng katta")
# else:
#     print(son3,"eng katta")
#
# son=int(input("son kiritin>>"))
# sonlar=list(range(1,101))
# if son in sonlar:
#     print("bu son ro'yxatta bor")
# else:
#     print("siz kiritgan son ro'yxatta yo'q")



# taomlar=["osh","manti","somsa","lag'mon","shashlik"]
# buyurtma=input("nima buyurtma qilasiz<<")
# if buyurtma.lower() in taomlar:
#     print("buyurtma qabul qilindi")
# else:
#     print("bu ovqat ro'yxatta y

# sonlar=list(range(1,200))
# juft_sonlar=[]
# toq_sonlar=[]
# for son in sonlar:
#     if son%2==0:
#         juft_sonlar.append(son)
#     else:
#         toq_sonlar.append(son)
# print(juft_sonlar)
# print(toq_sonlar)



# print("***karra jadvali***")
# x=int(input("nechi karrani xisoblaymiz>>"))
# sonlar=list(range(1,11))
#
# for son in sonlar:
#     natija=x*son
#     #print(x,"*",son,"=",natija)
#     print(f"{x}*{son}={natija}")

sonlar=[1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    if son==5:
        continue
    print(son)

sonlar=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for son in sonlar:
        if son==5:
            break
        print(son)


