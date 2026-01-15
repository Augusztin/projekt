a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))
c = int(input("Add meg a harmadik számot: "))

a_paros = (a % 2 == 0)
b_paros = (b % 2 == 0)
c_paros = (c % 2 == 0)

if a_paros and b_paros and c_paros:
    print("Mindhárom páros.")
elif not a_paros and not b_paros and not c_paros:
    print("Mindhárom páratlan.")
else:
    print("Kevert.")