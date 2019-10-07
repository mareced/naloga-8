nr1 = int(input("Vpišite prvo številko: "))
nr2 = int(input("Vpišite drugo številko: "))
operation = input("Vpišite znak za množenje*, znak za deljenje/, znak za seštevanje+ ali znak za odštevanje- : ")

if operation == "+":
    print("Rezultat je: " + str(nr1 + nr2))
elif operation == "-":
    print("Rezultat je: " + str(nr1 - nr2))
elif operation == "*":
    print("Rezultat je: " + str(nr1 * nr2))
elif operation == "/":
    print("Rezultat je: " + str(nr1 / nr2))
else:
    print ("Žal ne poznam ukaza, poskusite znova")

