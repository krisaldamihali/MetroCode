# Le te printojme mesazhin tone te pare "Hello World"
print("Hello World")
# Vini re se duke qene se po printojme nje te dhene te tipit string, i kemi vendosur fjalet ne thonjeza


# Le te shohim si mund te printojme vleren e nje variable te quajtur konstantja
konstantja = 10
print(konstantja)

# Le te printojme nje variabel qe permban si vlere nje te dhene string
objekti = "roboti" # Emri i varjables eshte "objekti" dhe vlera e variables eshte "roboti"


print("Me poshte po printojme vleren e variables objekti: ")
# Per te printuar variablen e mesiperme mjafton t'i referohemi emrit te saj
print(objekti)


# Per te printuar se bashku nje string dhe nje vlere, i ndajme me nje presje
print("Kjo eshte vlera e konstantes:", konstantja)


# Nese duam te perdorim operatorin +(mbledhje) per te bashkuar nje fjale dhe nje numer, duhet qe ta konvertojme numrin ne fjale nepermjet funksionit "str()"
# Kjo sepse nuk mund te mbledhim nje fjale me nje numer
# Pra, vlera e variables "konstantja" si fjale, do te ishte str(konstantja) e cila do te jepte rezultatin "10" (si string, jo si numer)
# Vetem kur te dy tipet e te dhenave jane te njejte mund t'i mbledhim vlerat e tyre
print("Konstantja: "  + str(konstantja))