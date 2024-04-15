
#LE GRAND TOME DES PROJETS PARA-ANGLAIS
# 
# #Ex 3.1
# 
# h=input("Heures: ")
# m=input("Minutes: ")
# s=input("Secondes: ")
# 
# hs=3600
# ms=60
# 
# print("est égal à "+str((int(h)*hs+int(m)*ms+int(s)))+" secondes.")

#Ex 3.2

s=input("Secondes: ")

hs=3600
h=int(s)//hs

ms=60

m=int(s)%hs

s=hs%ms


print("est égal à "+str(h)+" heures, "+str(m)+" minutes,"+str(s)+" secondes.")


# +str(round(m))



