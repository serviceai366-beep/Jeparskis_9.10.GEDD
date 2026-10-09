daudzums = int(input("Cik skaitļus ievadīsi? "))

if daudzums <= 0:
    print("Kļūda: skaitļu skaitam jābūt lielākam par 0.")
else:
    skaitlis = int(input("Ievadi skaitli: "))
    mazakais = skaitlis
    lielakais = skaitlis

    for i in range(daudzums - 1):
        skaitlis = int(input("Ievadi skaitli: "))

        if skaitlis < mazakais:
            mazakais = skaitlis

        if skaitlis > lielakais:
            lielakais = skaitlis

    print("Mazakais:", mazakais)
    print("Lielakais:", lielakais)