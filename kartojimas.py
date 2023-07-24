
# 1 SALYGINIAI SAKINIAI
# A uzduotis
# ivestis = int(input("iveskite skaicius : "))
#     if ivestis > 0:
#         print ("Teigiamas skaičius")
#     elif ivestis < 0:
#         print ("Neigiamas skaičius")
#     else:
#         print ("Nulis")
#
#
#B uzduotis
# amzius = int(input("iveskite amziu : "))
#     if amzius > 18:
#         print ("pilnametis")
#     else:
#         print ("nepilnametis")

#CIKLAI
# A uzduotis
# ciklas = 0
# suma = 0
# sk = int(input("iveskite skaiciu: "))
# while sk != ciklas:
#     ciklas += 1
#     suma += ciklas
#     print(ciklas)
#     # B uzduotis
#     if ciklas % 2 == 0:
#         suma += ciklas
#
# print (suma)

# FUNKCIJOS
# A uzduotis

# def apskaiciuoti_vidurki(skaiciu_sarasas):
#     suma = sum(skaiciu_sarasas)
#     vid = suma / len(skaiciu_sarasas)
#     return vid
#
# list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
#
# print(apskaiciuoti_vidurki(list1))
#
# def palyginti_du_skaičius(skaičius1, skaičius2):
#     if skaičius1 > skaičius2:
#         return skaičius1
#     else:
#         return skaičius2
#
# # KLASES
# # A uzduotis
#
# class staciakampis ():
#     def __init__ (self,plotis, aukstis):
#         self.plotis = plotis
#         self.aukstis = aukstis
#
#         def apskaiciuoti_plota(self):
#             return self.plotis * self.aukstis
#
# staciakampis1 = staciakampis(5,10)
# staciakampis2 = staciakampis(3,7)
#
# print(staciakampis1.apskaiciuoti_plota())
# print(staciakampis2.apskaiciuoti_plota())


# class Darbuotojas:
#     def __init__(self, vardas, pavardė, atlyginimas):
#         self.vardas = vardas
#         self.pavardė = pavardė
#         self.atlyginimas = atlyginimas
#
#     def pakeisti_atlyginima(self, naujas_atlyginimas):
#         self.atlyginimas = naujas_atlyginimas
#
# # Sukuriame objektą ir pakeičiame atlyginimą
# darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 2500)
# print("Dabartinis atlyginimas:", darbuotojas1.atlyginimas)
#
# darbuotojas1.pakeisti_atlyginima(3000)
# print("Naujas atlyginimas:", darbuotojas1.atlyginimas)