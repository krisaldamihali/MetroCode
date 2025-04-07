 
#Shembull me loops
numbers = [1, 2, 3, 4]

for num in numbers:
    print(num * 2)


#Ushtrim 1 
#Printo numrat nga 1 deri në 10:
for i in range(1, 11):
    print(i)

#Ushtrim 2
#Printo "Hello!" 5 herë:
for i in range(5):
    print("Hello!")

#Ushtrim 3
#Shto të gjitha numrat nga 1 deri në 5:
total = 0
for i in range(1, 6):
    total = total + i

print("Shuma është:", total)


#..................................................
## for variabel in range(nr_fillimi, nr_mbarimi, hapi):
    # Kodi që do të përsëritet
    
for i in range(1, 6):  
    print("Numri:", i)

for i in range(2, 11, 2):
    print("Numri çift:", i)


#..................................................
####Shembull i zgjeruar

# Krijo një listë bosh
numbers = []

# Shto 5 numra në listë
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)

# Printo listën
print("Vektori është:", numbers)

# Llogarit shumën e të gjithë numrave
total = 0
for num in numbers:
    total = total + num

# Printo rezultatin
print("Shuma e numrave në vektor është:", total)



