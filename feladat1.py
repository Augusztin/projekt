szam = int(input("Adj meg egy egész számot: "))

if szam > 0:
    if szam % 2 == 0:
        print(f"A {szam} pozitív páros szám")
    else:
        print(f"A {szam} pozitív páratlan szám")

elif szam < 0:
    if szam % 2 == 0:
        print(f"A {szam} negatív páros szám")
    else:
        print(f"A {szam} negatív páratlan szám")

else:
    print("Nullát adtál meg.")