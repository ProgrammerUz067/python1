# OOP meros olish va polimorfizm
# 22-dars dunder metodlarga kirish

class Shaxs:
    def __init__(self,ismi,yoshi):
        self.ismi=ismi
        self.yoshi=yoshi


    def get_n(self):
        return self.ismi

    def get_y(self):
        return self.yoshi

    def get_i(self):
        return f"ismi {self.ismi}  yoshi {self.yoshi} da"



class Student(Shaxs):
    def __init__(self,ismi,yoshi,student_id):
        super().__init__(ismi,yoshi)
        self.student_id=student_id

    def get_i(self):
            return f"ismi {self.ismi}  yoshi {self.yoshi} da  id {self.student_id}"

talaba1=Student("ali",23,"mf4630")
talaba2=Student("alisher",14,"fd4251")
print(talaba2.get_i())




class Techer(Shaxs):
    def __init__(self,ismi,yoshi,fan):
        super().__init__(ismi,yoshi)
        self.fan=fan


    def get_i(self):
            return f"ismi {self.ismi}  yoshi {self.yoshi} da fan {self.fan}"


fan1=Techer("oybek",16,"ona tili")
print(fan1.get_i())







class Items:
    def __init__(self,nomi:str,narxi:float,yili:int):

        assert narxi>=0,f"Siz manfiy son kiritingiz 0 dan katta son kiriting"
        assert yili>0,f"Siz manfiy son kiritingiz 0 dan katta son kiriting"

        self.nomi=nomi
        self.narxi=narxi
        self.yili=yili


telefon1=Items("samsung",700,2022)
telefon2=Items("iphone14",1500,2023)
print(telefon1.narxi)
print(telefon2.yili)




class Movie:
    def __init__(self,nomi,rejisori):
        self.nomi=nomi
        self.rejisori=rejisori

    def get_n(self):
        return self.nomi

    def get_r(self):
        return self.rejisori

    def info(self):
        return f"kino nomi {self.nomi} rejisori {self.rejisori}"




class Films(Movie):
    def __init__(self,nomi,rejisori,janri):
        super().__init__(nomi,rejisori)
        self.janri=janri


    def info(self):
        return f"kino nomi {self.nomi} rejisori {self.rejisori} janri {self.janri}"


film1=Films("taxi","ludvik pan","jangari")
film2=Films("fast and four","jon evin","jangari")
print(film1.info())
print(film2.get_n())




class Multipanorama(Movie):
    def __init__(self,nomi,rejisori,janri):
        super().__init__(nomi,rejisori)
        self.janri=janri

    def info(self):
        return f"kino nomi {self.nomi} rejisori {self.rejisori} janri {self.janri}"


multik1=Multipanorama("buratino","ahmad aliyev","komedik")
print(multik1.info())


class Fantastik(Movie):
    def __init__(self,nomi,rejisori,janri):
        super().__init__(nomi,rejisori)
        self.janri=janri

    def info(self):
        return f"kino nomi {self.nomi} rejisori {self.rejisori} janri {self.janri}"


fant1=Fantastik("oy","silver rose","sarguzasht")
print(fant1.get_r())

jiuihy











# uy ishi
class Shaxs:
    def __init__(self,ism,yosh):
        self.ism=ism
        self.yosh=yosh


    def get_i(self):
        return self.ism

    def get_y(self):
        return self.yosh


    def info(self):
        return f"ismi {self.ism} yoshi {self.yosh}"




# class Admin(Shaxs):
#     def __init__(self, ism, yosh, manzil):
#         super().__init__(ism,yosh)
#         self.manzil=manzil
#
#
#     def info(self):
#         return f"ismi {self.ism} yoshi {self.yosh} manzili {self.manzil}"
#
# admin1=Admin("oybek",17,"buxoro")
# admin2=Admin("afruz",12,"qashqadaryo")
# admin3=Admin("ramiz",14,"samarqand")
#
#
# class Foydalanuvchi(Shaxs):
#     def __init__(self,ism,yosh,ban_kimga):
#         super().__init__(ism,yosh)
#         self.ban_kimga=ban_kimga
#
#
#
#     def ban_user(self):
#         return "foydalanuvchi bloklandi"
#
#
# f1=Foydalanuvchi("Muhammadjon",3,"ali")
# f2=Foydalanuvchi("yusuf",35,"ahmad")
# f3=Foydalanuvchi("ali",21,"oybek")
# print(f1.get_y())
# print(f3.ban_user())



















