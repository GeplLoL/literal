from module1 import *
while True:
    v=int(input("1-Otsige pealinna\n2-Leidke riik\n3-Lisa\n4-Parandamine\n5-Test"))
    if v==1:
        laused=Loe_fail("TextFile1.txt")
        x=keyRiik(laused)
        print(x)
        print(laused)
    elif v==2:
        laused=reLoe_fail("TextFile1.txt")
        x=keyPealiin(laused)
        print(x)
        print(laused)
    elif v==3:
        laused=Loe_fail("TextFile1.txt")
        x=lisa_key(laused)
        print(laused)
    elif v==4:
        laused=Loe_fail("TextFile1.txt")
        x=parandamine(laused)
        print(x)
    elif v==5:
        laused=Loe_fail("TextFile1.txt")
        x=test(laused)
        print(x)