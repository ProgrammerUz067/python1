# class Book:
#     def __init__(self,nomi,muallifi,narxi,janri):
#         self.nomi=nomi
#         self.muallifi=muallifi
#         self.narxi=narxi
#         self.janri=janri
#
#
#     def get_nomi(self):
#         return self.nomi
#
#     def get_narxi(self):
#         return self.narxi
#
#
# book1=Book("sariq devni minib","Xudoyiberdi toxtaboyev",34000,"badiy")
# book2=Book("stiv jobs","stiv jobs",55000,"hayotiy")
# book3=Book("qaylardasan bolaligim","Xudoyiberdi toxtaboyev",25000,"badiy")
# book4=Book("oqshomi sarvar","alisher navoiy",47000,"badiy")
#
# print(book1.get_narxi())
#
#
#
#
# class Kutubxona:
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.kitoblar=[]
#         self.kitoblar_soni=0
#
#     def nomi(self):
#         return self.nomi
#
#     def qos(self,kitob):
#         self.kitoblar.append(kitob)
#         self.kitoblar_soni+=1
#
#     def count(self):
#         return self.kitoblar_soni
#
#     def info(self):
#         return [kitob.get_narxi() for kitob in self.kitoblar]
#
#
# kutubxona1=Kutubxona("milliy kutubxona")
# kutubxona2=Kutubxona("Pushkinskiy kutubxonasi")
#
#
# kutubxona1.qos(book1)
# kutubxona1.qos(book2)
# kutubxona1.qos(book3)
#
# print(kutubxona1.info())


#
# class Talaba:
#     def __init__(self,ismi,familiyasi,manzili):
#         self.ismi=ismi
#         self.familiyasi=familiyasi
#         self.manzili=manzili
#
#
#     def get_ismi(self):
#         return self.ismi
#
#     def get_manzili(self):
#         return self.manzili
#
#
# talaba1=Talaba("ali","eshmatov","samarqand")
# talaba2=Talaba("alisher","rahmonov","buxoro")
# talaba3=Talaba("oybek","ulugov","qashqadaryo")
# talaba4=Talaba("Ramiz","Ziyodullayev","samarqand")
#
#
#
#
#
# class Fan:
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.talabalar= []
#         self.talabalar_soni=0
#
#     def nomi(self):
#         return self.nomi
#
#     def qos(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni+=1
#
#     def count(self):
#         return self.talabalar_soni
#
#     def info(self):
#         return [talaba.get_ismi() for talaba in self.talabalar]
#
#
#
# fan1=Fan("Ona tili")
# fan2=Fan("Fizika")
#
# fan1.qos(talaba3)
# fan1.qos(talaba2)
# fan2.qos(talaba4)
#
# print(fan1.info())






#uy ishi 21_dars

class Produkt:
    def __init__(self,nomi,narxi,kategoriyasi):
        self.nomi=nomi
        self.narxi=narxi
        self.kategoriyasi=kategoriyasi

    def get_n(self):
        return self.nomi

    def get_narx(self):
        return self.narxi

    def get_k(self):
        return self.kategoriyasi

    def info(self):
        return f"maxsulot nomi {self.nomi} narxi {self.narxi} kategoriyasi {self.kategoriyasi}"


narsa1=Produkt("banan",25000,"meva")
narsa2=Produkt("fonar",14000,"elektronika")
narsa3=Produkt("notbuk",56000000,"texnika")
print(narsa3.info())






class Book:
    def __init__(self,nomi,muallifi,narxi,janri):
        self.nomi=nomi
        self.muallifi=muallifi
        self.narxi=narxi
        self.janri=janri


    def get_nomi(self):
        return self.nomi

    def get_narxi(self):
        return self.narxi

    def janir(self):
        return self.janri

    def get_info(self):
        return f"kitob nomi {self.nomi} muallifi {self.muallifi} narxi {self.narxi} janri {self.janri}"



book1=Book("sariq devni minib","Xudoyiberdi toxtaboyev",34000,"badiy")
book2=Book("stiv jobs","stiv jobs",55000,"hayotiy")
book3=Book("qaylardasan bolaligim","Xudoyiberdi toxtaboyev",25000,"badiy")
book4=Book("oqshomi sarvar","alisher navoiy",47000,"badiy")
print(book4.get_info())






class BankAccount:
    def __init__(self,hisob_raqam,egasi,balansi,valutasi):
        self.hisob_raqam=hisob_raqam
        self.egasi=egasi
        self.balansi=balansi
        self.valutasi=valutasi


    def raqami(self):
        return self.hisob_raqam


    def egasi(self):
        return self.egasi


    def balans(self):
        return self.balansi

    def valut(self):
        return self.valutasi

    def bank_i(self):
        return f"hisob raqami {self.hisob_raqam} egasi {self.egasi} balansi {self.balansi} valutasi {self.valutasi}"


user1=BankAccount(8979172893,"ergashev ali",516100,"euro")
user2=BankAccount(5654656165,"boltaqulov oybek",100000,"rub")
user3=BankAccount(7979414203,"Ziyodulayev ramiz",32555000,"so'm")
print(user3.bank_i())





class Movie:
    def __init__(self,nomi,rejisori,ovozi):
        self.nomi=nomi
        self.rejisori=rejisori
        self.ovozi=ovozi


    def f_n(self):
        return self.nomi

    def f_r(self):
        return self.rejisori

    def f_o(self):
        return self.ovozi

    def f_i(self):
        return f"film nomi {self.nomi} rejisori {self.rejisori} ovozi {self.ovozi}"

f1=Movie("fast four","jon kevin","o'zbekcha")
f2=Movie("taxi","ludvik kevin","fransuzcha")
f3=Movie("so'ngi qon","len mark","ruscha")
print(f2.f_i())






class Song:
    def __init__(self,nomi,ijrochisi,turkumi):
        self.nomi=nomi
        self.ijrochisi=ijrochisi
        self.turkumi=turkumi


    def nomi(self):
        return self.nomi

    def ij(self):
        return self.ijrochisi

    def tur(self):
        return self.turkumi

    def info(self):
        return f"qoshiq nomi {self.nomi} ijrochisi {self.ijrochisi} turkumi {self.turkumi}"


song1=Song("chaqasan","jahongir otajonov","sho'q")
song2=Song("Waqafa","","nashida")
song3=Song("the best","mark jon","rok")
print(song1.info())




class Shape:
    def __init__(self,formasi,uzunligi,balandligi,rangi):
        self.formasi=formasi
        self.uzunligi = uzunligi
        self.balandligi = balandligi
        self.rangi = rangi

    def uzun(self):
        return self.uzunligi

    def reng(self):
        return self.rangi

    def info(self):
        return f"shakilning formasi {self.formasi} uzunligi {self.uzunligi} rangi {self.rangi}"

sh1=Shape("tortburshak",14,2,"oq")
sh2=Shape("aylana",45,3,"sariq")
sh3=Shape("uchburchak",100,84,"qizil")
print(sh3.info())





















