# Vecuma robežas:
# 0–12: bērns
# 13–17: pusaudzis
# 18–64: pieaugušais
# 65 un vairāk: seniors

try:
    vecums = int(input("Ievadi savu vecumu: "))

    if vecums < 0:
        print("Kļūda: vecums nevar būt negatīvs.")
    elif vecums < 13:
        print("bērns")
    elif vecums < 18:
        print("pusaudzis")
    elif vecums < 65:
        print("pieaugušais")
    else:
        print("seniors")

except ValueError:
    print("Kļūda: ievadi veselu skaitli.")