luku =int(input("luku:\n"))

if luku > 0:
    print("luku on positiivinen")
    if luku > 10:
        print("luku on suurempi kuin kymmenen")
elif luku < 0:
    print("luku on negatiivinen")
    if luku < -10:
        print("luku on piinempi kuin -10")
else:
    print("luku = 0")
print("ohjelman suoritus päätyy")
    
    

    