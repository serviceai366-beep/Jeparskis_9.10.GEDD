parole = "123"
meginajumi = 3
print ("ievadi paroli")
while meginajumi >0:
    x= input()
    if(x== parole):
        print("krasava!!!")
        break
    else:
        meginajumi-= 1
        print("palika meginajumu", str (meginajumi))
if meginajumi== 0:
    print("idi po plach")
