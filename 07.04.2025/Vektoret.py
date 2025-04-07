#Krijimi i listave ne python
colors = ["red", "blue", "green"]
print(colors)

#Aksesimi i elementeve 
print(colors[0])  # red
print(colors[1])  # blue
print(colors[2])  # green

#colors = [ "red" , "blue" , "green" ]
#             0       1         2

#Ndryshimi i elementeve 
colors[1] = "purple"
print(colors)


#Shtimi i elementeve 
colors.append("yellow")
print(colors)

#Fshija e elementeve 
colors.remove("red")
print(colors)

#Fshirja nepermjet pozicionit
del colors[0]
print(colors)

#Kontrolli i gjatesise se listes
print(len(colors))

#Si te merrni vetem nje pjese te listes
colors = ["red", "blue", "green", "yellow"]
print(colors[1:3])  # From index 1 to 2 (blue, green)


#loop ne nje list
for color in colors:
    print(color)
    