#Uppgift m05u12

#Tom lista
l_tal = []
filnamn = 'm02u12_output.txt'

#Funktioner
def summa():
    summa = 0
    for t in l_tal:
        summa += t
    return summa

def högsta():
    högsta = l_tal[0]
    for t in l_tal:
        if t > högsta:
            högsta = t
        return högsta

    def lägsta():
        lägsta = l_tal[0]
        for t in l_tal:
            if t < lägsta:
                lägsta = t
            return lägsta

f = open(filnamn, 'w')
f.close()


with open(filnamn, 'a') as f:    
    while True:
        inmatning = int(input("Ange ett heltal (0 avbryter): "))
        if inmatning == 0:
            f.write("Inmatat tal: 0, programmet avbryts.")
            break
        l_tal.append(inmatning)
        f.write(f"Inmatat tal: {inmatning}, min: {lägsta()}, max: {högsta()}, summa: {summa()}.\n")

    f.write(f"Hela lista: {l_tal}, min: {lägsta()}, max: {högsta()}, summa: {summa()}."

with open(filnamn) as f:
    print(f.read())
