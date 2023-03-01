from operator import index
from random import *
def Loe_fail(f):
    riigid=[]
    sonastik = {}
    file=open(f, "r", encoding="utf-8-sig")
    for line in file:
        k, v=line.split("-")
        sonastik[k] = v
        riigid.append(k)
    file.close()
    return sonastik
def reLoe_fail(f):
    sonastik = {}
    file=open(f, "r", encoding="utf-8-sig")
    for line in file:
        k, v=line.split("-")
        sonastik[v] = k
    file.close()
    return sonastik
def keyRiik(f:dict):
    xc=input("Sise riik: ")
    x=f.get(xc)
    return x
def keyPealiin(f:dict):
    xc=input("Sise pealiin: ")
    x=f.get(xc)
    return x
def lisa_key(f):
    xc=input("Sisse riik: ")
    cx=input("Sisse pealinn: ")
    f.update({xc:cx})
    return f
def parandamine(f:dict):
    ds=input("Kirjutage riik, mida parandada: ")
    f.pop(ds)
    xc=input("Sisse riik: ")
    cx=input("Sisse pealinn: ")
    f.update({xc:cx})
    return f

def test(f):
    xc = int(input("Mitu korda sa tahad mängida? "))
    sd = list(f.keys())
    ds = list(f.values()) 
    s = choice(sd)
    print(s)
    ind = sd.index(s) 
    answer = input("Sisse pealinn: ") 
    if answer == ds[ind]: 
        x = "õige"
        return x 
    else:
        x = "vale"
        return x
    
    
