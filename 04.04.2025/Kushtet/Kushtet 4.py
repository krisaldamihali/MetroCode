    
# Shembull 4. (nested if - Kusht brenda kushtit )
nota = int(input("Shkruaj notën e studentit (nga 1 në 10): "))
provime_te_kaluara = int(input("Sa provime ka kaluar studenti? "))

if nota >= 5:
    if provime_te_kaluara >= 3:
        print("Studenti është i kualifikuar për diplomim!")
    else:
        print("Studenti ka kaluar provimin, por duhet të kalojë më shumë provime.")
else:
    print("Studenti ka dështuar në provim. Duhet të përmirësohet.")
    

    
