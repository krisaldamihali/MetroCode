''' Ushtrim 
Kërkesa:
Shkruani një program në Python që kërkon nga përdoruesi të fusë notën e tij (0-100) dhe
më pas të tregojë në cilën shkallë vlerësimi bie. 
Nëse nota është 90 ose më shumë, shfaqni mesazhin "Nota juaj është A"
Nëse është midis 80 dhe 89, shfaqni "Nota juaj është B"
Nëse është midis 70 dhe 79, shfaqni "Nota juaj është C"
Nëse është midis 60 dhe 69, shfaqni "Nota juaj është D"
Nëse është më pak se 60, kontrolloni nëse nota është më e vogël se 40, 
dhe në atë rast tregoni "Ju keni dështuar rëndë!", përndryshe shfaqni "Nota juaj është F" '''


nota = int(input("Shkruani notën tuaj (0-100): "))

if nota >= 90:
    print("Nota juaj është A.")
elif nota >= 80:
    print("Nota juaj është B.")
elif nota >= 70:
    print("Nota juaj është C.")
elif nota >= 60:
    print("Nota juaj është D.")
else:
    if nota < 40:
        print("Ju keni dështuar rëndë!")
    else:
        print("Nota juaj është F.")