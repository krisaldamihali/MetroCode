# Bëni një makinë llogaritëse që mbledh numra derisa t'i thuash pusho

numri = 0
while True:
    numri += input()
    if str(numri) == "pusho":
        print(numri)
        break
    print(numri)
