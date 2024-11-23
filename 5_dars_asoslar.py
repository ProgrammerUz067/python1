# royxat=[1,'acd',4,5,'asw',7.2,-5,-12.22]


# butun_son=[]



# 1-yo'l
# for son in royxat:
#     if type(son)==int:
#         butun_son.append(son)
# print(len(butun_son))




# 2-yo'l
# butunsonlar=len([qiymat for qiymat in royxat if isinstance(qiymat,int)])
# print(butunsonlar)










# 1-yo'l
# roy=[]

# for son in royxat:
#     roy.append(son)


# list comprehensions

# new_list=[son for son in royxat]



# new_list3=[3,4,5,5,6]




# sa=[son**2 for son in new_list3]
# print(sa)


# sonlar=[2,4,5,8,7,8,8,8,6,3,1,2,4,6,7,1,3,2,7,1,8]

# max_takror=0
# max_son=None

# for son in sonlar:
#     takror_son=sonlar.count(son)
#     if takror_son>max_takror:
#         max_takror==takror_son
#         max_son=son
# print(max_son)



# takrorson=max(set(sonlar))






# royxat=[14,5248,745,621,45,7,8631,7,744,1,2334,87,458]

# max_son=max(royxat)
# min_son=min(royxat)


# max_index=[]
# min_index=[]

# for index,qiymat in enumerate(royxat):
#     if max_son==qiymat:
#         max_index.append(index)
#     elif min_son==qiymat:
#         min_index.append(index)
        
# print(f"Maksimal son {max_son} uning indexsi {max_index}")
# print(f"Minimal son {min_son} uning indexsi {min_index}")



# uy ishi
# royxat=[[],'kok',2,4,5,'sariq',[]]

# for qiymat in royxat:
#     if qiymat==list:
#         royxat.remove(qiymat)
# print(royxat)




#2

# royxat1=[qiymat for qiymat in royxat if qiymat]
# print(royxat1)



# royxat=['s','w','f','q','c','s','f']
# son='f'
# list1=[]
# for index,h in enumerate(royxat):
#     if son in royxat:
#         if son==h:
#             list1.append(index)


# print(list1[-1])




# matn=input("Emailingizni kiriting >")
# i=''

# for harf in matn:
#     if harf=="@":
#         break
#     else:
#         i+=harf
              
# print(i)
    



# satr='Python3 web dasturlash tili'
# satr2='Python2.7 web dasturlash tili'
# b=''

# for h in satr:
#     if h in satr2:
#         b+=h

# print(b)






soz=input("So'z kiriting >")
if len(soz)>3:
    if soz.endswith('ing'):
        soz+='ly'
    else:
        soz+='ing'
else:
    print(soz)

print(soz)


# 611-555-01-26








