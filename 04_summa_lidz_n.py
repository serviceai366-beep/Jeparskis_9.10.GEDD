try:
    n = int(input("Ievadi pozitīvu veselu skaitli: "))

    if n <= 0:
        print("Kļūda: skaitlim jābūt lielākam par 0.")
    else:
        summa = 0

        for i in range(1, n + 1):
            summa = summa + i

        print("Summa:", summa)

except ValueError:
    print("Kļūda: ievadi veselu skaitli.")