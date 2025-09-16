import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def ex1_1():
    clear()
    a = float(input("Introduceti primul numar real: "))
    b = float(input("Introduceti al doilea numar real: "))
    suma = a + b
    produs = a * b
    maxim = max(a, b)
    print("Suma celor doua numere este:", suma)
    print("Produsul celor doua numere este:", produs)
    print("Maximul dintre cele doua numere este:", maxim)
    
    match int(input("\n1 - Returnare la pagina exercitiului | 0 - Meniu principal: ")):
        case 1: ex1()
        case 0: main()
        case _: print("Optiune invalida.")

def ex1_2():
    clear()
    
    numar = int(input("Introduceti un numar intreg: "))
    if numar % 2 == 0:
        print("Numarul", numar, "este par.")
    else:
        print("Numarul", numar, "este impar.")
        
    match int(input("\n1 - Returnare la pagina exercitiului | 0 - Meniu principal: ")):
        case 1: ex1()
        case 0: main()
        case _: print("Optiune invalida.")
    
def ex1_3():
    clear()
    n = int(input("Introduceti un numar intreg pozitiv n: "))
    print("Numerele de la 1 la", n, "sunt:")
    for i in range(1, n + 1):
        print(i, end=' ')
    
    match int(input("\n1 - Returnare la pagina exercitiului | 0 - Meniu principal: ")):
        case 1: ex1()
        case 0: main()
        case _: print("Optiune invalida.")

def ex1_4():
    clear()
    n = int(input("Introduceti un numar intreg pozitiv n: "))
    suma = 0
    i = 1
    while i <= n:
        suma += i
        i += 1
    print("Suma numerelor de la 1 la", n, "este:", suma)
    
    match int(input("\n1 - Returnare la pagina exercitiului | 0 - Meniu principal: ")):
        case 1: ex1()
        case 0: main()
        case _: print("Optiune invalida.")

def ex1():
    clear()
    print ("    Ex 1: Operatii aritmetice: \n")
    print ("1.1 Citirea a doua numere reale si efectuarea urmatoarelor operatii aritmetice: \n")
    print ("    (Suma lor; Produsul lor; Maximul dintre ele;)\n")
    print ("1.2 Citirea unui numar si verifiica daca este par sau impar;\n")
    print ("1.3 Aisarea tuturor numerelor de la 1 la n utilizand bucla 'for'")
    print ("1.4 Calculeaza suma numerelor de la 1 la n folosind while\n")
    match int(input("Alege exercitiul (1-4) | 0 - Return: ")):
        case 1: ex1_1()
        case 2: ex1_2()
        case 3: ex1_3()
        case 4: ex1_4()
        case 0: main()
        case _: print("Exercitiu invalid. Te rog alege un numar intre 1 si 4.")
    


def ex2_1():
    clear()
    a = float(input("Introduceti valoarea lui a: "))
    b = float(input("Introduceti valoarea lui b: "))
    if a == 0:
        if b == 0:
            print("Ecuatia are o infinitate de solutii.")
        else:
            print("Ecuatia nu are solutii.")
    else:
        x = -b / a
        print("Solutia ecuatiei este: x =", x)
        
    match int(input("\n1 - Returnare la pagina exercitiului | 0 - Meniu principal: ")):
        case 1: ex2()
        case 0: main()
        case _: print("Optiune invalida.")
        
def ex2_2():
    clear()
    a = float(input("Introduceti valoarea lui a: "))
    b = float(input("Introduceti valoarea lui b: "))
    c = float(input("Introduceti valoarea lui c: "))
    
    if a == 0:
        if b == 0:
            if c == 0:
                print("Ecuatia are o infinitate de solutii.")
            else:
                print("Ecuatia nu are solutii.")
        else:
            x = -c / b
            print("Ecuatia este de gradul I. Solutia este: x =", x)
    else:
        D = b**2 - 4*a*c
        print("Discriminantul D =", D)
        if D < 0:
            print("Ecuatia nu are solutii reale.")
        elif D == 0:
            x = -b / (2*a)
            print("Ecuatia are o solutie dubla: x =", x)
        else:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            print("Ecuatia are doua solutii reale distincte: x1 =", x1, "si x2 =", x2)
    match int(input("\n1 - Returnare la pagina exercitiului | 0 - Meniu principal: ")):
        case 1: ex2()
        case 0: main()
        case _: print("Optiune invalida.")

def ex2():
    clear()
    print("    Ex 2: Algoritmi si programe pentru ecuatii: \n")
    print("2.1. Ecuatia de gradul I: ax+b=0\n Implementarea programului care:\n")
    print(" - Citeste valorile lui a si b de la tastatura, trateaza separat cazurile: a=0 si a!=0\n")
    print("2.2. Ecuatia de gradul II: ax^2+bx+c=0\n Implementarea programului care:\n")
    print(" - Citeste valorile lui a, b si c de la tastatura, verifica daca ecuatia este de gradul 1 (cazul a = 0),\ncalculeaza si afiseaza discriminantul D=b^2-4ac,\nDetermina solutiile in dependenta de valoarealui D(<0, =0, >0)\n")
    match int(input("Alege exercitiul (1-2) | 0 - Return: ")):
        case 1: ex2_1()
        case 2: ex2_2()
        case 0: main()
        case _: print("Exercitiu invalid. Te rog alege un numar intre 1 si 2.")

def ex3_1():
    clear()
    while True:
        print("Meniu Ecuatii:")
        print("1. Ecuatia de gradul I: ax + b = 0")
        print("2. Ecuatia de gradul II: ax^2 + bx + c = 0")
        print("0. Returnare la pagina exercitiului")
        optiune = int(input("Alege optiunea (0-2): "))
        
        if optiune == 1:
            a = float(input("Introduceti valoarea lui a: "))
            b = float(input("Introduceti valoarea lui b: "))
            if a == 0:
                if b == 0:
                    print("Ecuatia are o infinitate de solutii.")
                else:
                    print("Ecuatia nu are solutii.")
            else:
                x = -b / a
                print("Solutia ecuatiei este: x =", x)
        
        elif optiune == 2:
            a = float(input("Introduceti valoarea lui a: "))
            b = float(input("Introduceti valoarea lui b: "))
            c = float(input("Introduceti valoarea lui c: "))
            
            if a == 0:
                if b == 0:
                    if c == 0:
                        print("Ecuatia are o infinitate de solutii.")
                    else:
                        print("Ecuatia nu are solutii.")
                else:
                    x = -c / b
                    print("Ecuatia este de gradul I. Solutia este: x =", x)
            else:
                D = b**2 - 4*a*c
                print("Discriminantul D =", D)
                if D < 0:
                    print("Ecuatia nu are solutii reale.")
                elif D == 0:
                    x = -b / (2*a)
                    print("Ecuatia are o solutie dubla: x =", x)
                else:
                    x1 = (-b + D**0.5) / (2*a)
                    x2 = (-b - D**0.5) / (2*a)
                    print("Ecuatia are doua solutii reale distincte: x1 =", x1, "si x2 =", x2)
        
        elif optiune == 0:
            ex3()
        else:
            print ("Optiune invalida. Te rog alege un numar intre 0 si 2.")

def ex3():
    clear()
    print("    Ex 3: Exercitiu de sinteza: \n")
    print(" - Alegerea tipului de ecuatie (gradul I sau gradul II) prin meniu if/elif\n")
    print(" - Rezolva exercitiile implementand logica anumita\n")
    print(" - Repeta meniul pana cand utilizatorul alege optiunea de iesire (while)\n")
    match int(input("1 - Incepe exercitiul | 0 - Return: ")):
        case 1: ex3_1()
        case 0: main()
        case _: print("Optiune invalida.")
    
    
def main():     
    clear()
    print("Laborator Nr.2 - Tehnici de Programare")
    match int(input("Alege exrcitiul de laborator (1-3): ")):
        case 1: ex1()
        case 2: ex2()
        case 3: ex3()
        case _: print("Exercitiu invalid. Te rog alege un numar intre 1 si 3.")
    

if __name__ == "__main__":
    main()