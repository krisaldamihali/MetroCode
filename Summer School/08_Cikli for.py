# Ushtrim 1
# Printo numrat nga 1 deri në 10:
for i in range(1, 11):
    print(i)

# Ushtrim 2
# Printo "Hello!" 5 herë:
for i in range(5):
    print("Hello!")

# Ushtrim 3
# Mblidh të gjitha numrat nga 1 deri në 5:
total = 0
for i in range(1, 6):
    total = total + i

print("Shuma është:", total)


# ..................................................
# for variabel in range(nr_fillimi, nr_mbarimi[ky numer nuk perfshihet], hapi):
# Kodi që do të përsëritet

for i in range(1, 6):
    print("Numri:", i)

for i in range(2, 11, 2):
    print("Numri çift:", i)
