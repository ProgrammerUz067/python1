# class Tel():
#     def __init__(self,marka,color,price):
#         self.marka=marka
#         self.color=color
#         self.price=price
        
        
#     def info(self):
#         return self.marka,self.color,self.price
    
#     def get_mar(self):
#         return self.marka
    
    
#     def pric(self):
#         return self.price
        
    
    
# tel1=Tel("samsung","qora",500)
# tel2=Tel("iphone","ko'k",500)
# print(tel2)



class Notbook():
    def __init__(self,protsesor,vidiocarta,marka,narx,rang="oq"):
        self.protsesor=protsesor
        self.vidiocarta=vidiocarta
        self.rang=rang
        self.narx=narx
        self.marka=marka
        
        
    def about(self):
        return self.protsesor,self.vidiocarta,self.rang,self.narx,self.marka
    
    
    def get_notbuk(self):
        return self.marka,self.rang,self.narx
    
    
    
notbook=Notbook("intel coroi i5", "rtx4060", "oq",1700,"mac m2")


not2=Notbook("rayzen","rxt3040", "asus",400,"qora")
print(not2.about())




class User():
    def __init__(self,username,password=0000):
        self.username=username
        self.password=password
        
        
    def get_user(self):
        return self.username
    
    def get_pas(self):
        return self.password
    


user1=User("Vali", "ali456")
print(user1.get_pas())


user2=Notbook("core i9", "rtx4060", "mac m3 pro", 4000)
print(user2.about())
