import math

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a * a

def pole_kola(r):
    return math.pi * r * r

print("Witaj w kalkulatorze pól figur geometrycznych!")

while True:
    print("\nWybierz figurę, dla której chcesz obliczyć pole:")
    print("1. Trójkąt")
    print("2. Prostokąt")
    print("3. Kwadrat")
    print("4. Koło")
    print("5. Wyjdź")

    wybor = input("Twój wybór (wpisz odpowiednią liczbę): ")

    if wybor == '1':
        a = float(input("Podaj długość podstawy trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        print("Pole trójkąta wynosi:", pole_trojkata(a, h))
    elif wybor == '2':
        a = float(input("Podaj długość pierwszego boku prostokąta: "))
        b = float(input("Podaj długość drugiego boku prostokąta: "))
        print("Pole prostokąta wynosi:", pole_prostokata(a, b))
    elif wybor == '3':
        a = float(input("Podaj długość boku kwadratu: "))
        print("Pole kwadratu wynosi:", pole_kwadratu(a))
    elif wybor == '4':
        r = float(input("Podaj promień koła: "))
        print("Pole koła wynosi:", pole_kola(r))
    elif wybor == '5':
        print("Do widzenia!")
        break
    else:
        print("Niepoprawny wybór. Wybierz liczbę od 1 do 5.")
