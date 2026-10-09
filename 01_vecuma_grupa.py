vecums = int(input("Ievadi savu vecumu: "))

if vecums < 0:
    print("Nepareizs vecums")
elif vecums < 13:
    print("bērns")
elif vecums < 18:
    print("pusaudzis")
elif vecums < 65:
    print("pieaugušais")
else:
    print("seniors")