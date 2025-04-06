#Shkruani një program që llogarit perimetrin dhe sipërfaqen e një drejtkëndëshi duke përdorur gjatësinë dhe gjerësinë e dhënë nga përdoruesi.
gjatesia = int(input("Shkruani gjatësinë e drejtkëndëshit: "))
gjersia = int(input("Shkruani gjerësinë e drejtkëndëshit: "))

# Llogaritim perimetrin dhe sipërfaqen
perimetri = 2 * (gjatesia + gjersia)
siperfaqja = gjatesia * gjersia

# Shfaqim rezultatet
print("Perimetri i drejtkëndëshit është:", perimetri)
print("Sipërfaqja e drejtkëndëshit është:", siperfaqja)