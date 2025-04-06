#Printimi i nje variable 
name = "Alice Smith"
print(name)  

print("\n-----------------------------------------------------------------\n")  
# Shenim: Nese doni te lini nje hapsire midis dy printimeve mund te perdorni \n ose print()

# User input
name = input("Enter your name: ")
print("Welcome, " + name + "!")  #concatenation
print("\n-----------------------------------------------------------------\n")  

power_level = int(input("On a scale of 1-100, how strong are your powers? "))
print("Your power level is " + str(power_level) + "!") #Kujdes! Duhet ta konvertoni ne string sepse nuk mund ta bashkoni nje string me nje integer.  
