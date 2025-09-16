def ex1():
    print ("    Ex 1: Calculul unei expresii matematice \n")
    print ("Calculam urmatoarea expresie matematica: ((3+7)/(2*3))^2 + (1/(5+6^2))")
    result = ((3+7)/(2*3))**2 + (1/(5+6**2))
    return result

def ex2():
    print ("    Ex 2: Calculul vitezei medii (m/s) \n")
    distance_km = input("Introdu distanta parcursa in kilometri: ")
    time_hours = input("Introdu timpul in care distanta a fost parcursa: ")
    distance_km = float(distance_km) * 1000
    time_hours = float(time_hours) * 3600
    avg_speed = distance_km / time_hours
    result = (round(avg_speed, 4))
    return result
    
def ex3():
    print ("    Ex 3: Calculul ariei si perimetrului unui triunghi \n")
    a = float(input("Introduceti lungimea laturii a: "))
    b = float(input("Introduceti lungimea laturii b: "))    
    c = float(input("Introduceti lungimea laturii c: "))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    perimeter = a + b + c
    print("\nRezultatul exercitiului trei este:")
    print("Aria triunghiului este: ", round(area, 4))
    print("Perimetrul triunghiului este: ", round(perimeter, 4))   
    
def main():    
    value = ex1()
    print("\nRezultatul exercitiului unu este: ", round(value,4), "\n")

    value = ex2()
    print("\nRezultatul exercitiului doi:\nViteza medie este: ", value, "m/s\n")

    value = ex3()

if __name__ == "__main__":
    main()