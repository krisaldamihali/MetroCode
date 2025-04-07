
#..................................................
### Një while loop përsëritet derisa një kusht të jetë i vërtetë.
# while kushti:
    # Kodi që do të përsëritet


numri = 1

while numri <= 5:
    print("Numri:", numri)
    numri += 1  # Rrit vlerën e numrit me 1
    
#................................................
    
#Shembull 2: Marrja e një numri pozitiv nga përdoruesi

numri = -1  # Fillimisht vendosim një vlerë të gabuar

while numri < 0:
    numri = int(input("Shkruaj një numër pozitiv: "))

print("Faleminderit! Ju keni shkruar numrin:", numri)

#Shembull 3: Printimi i numrave çift nga 2 deri në 10
i = 2

while i <= 10:
    print(i)
    i = i + 2
    
    
#.................................................. 

#Ushtrim 1
#Shkruaj një program që numëron mbrapsht nga 10 deri në 1 dhe në fund printon "Gati, NISU!" 🚀
number = 10

while number >= 1:
    print(number)
    number = number - 1

print("Gati, NISU!")  # Ky mesazh printohet pasi mbaron numërimi

