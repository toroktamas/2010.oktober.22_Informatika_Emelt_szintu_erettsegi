#!/usr/bin/python3
# -*- coding:utf-8 -*-

def anagramma(szo1):
    return sorted(list(szo1))


print("1. feladat")
"""Szoveget bekerni es meghatarozni hogy hany kulonbozo elemet tartalmaz az adott szoveg. """
szoveg_bekeres = set(list(input("Adja meg a szoveget: ")))
print("A beirt szoveg {} kulonbozo karaktert tartalmaz".format(len(szoveg_bekeres)))

print("2. feladat")
"""Szavak beolvasasa a szotar.txt--bol es eltarolasa amit en szotarban oldanak meg. Ami a kovetkezo keppen nezne ki:
szotar{
hanyadik szo: {
    "Szo": eszesen,
    "szo karakterekent": [e,s,z,e,s,e,n],
    "anagramma": [e,n,s,z]  # egyedi betuk abc sorrendben
 }
}
"""
szotar = {}
n = 0
with open("szotar.txt", "rt+", encoding="ASCII") as f:
    for s in f:
        n+=1
        sor = s.replace("\n","")
        szotar[n] = {}
        szotar[n]["szo"] = sor
        szotar[n]["anagramma"] = anagramma(sor)
        sortor = []
        for sz in sor:
            sortor.append(sz)
            szotar[n]["szo karakterenkent"] = sortor

#print(szotar)
print("3. feladat")
"""Minden szo karaktereit egyenkent abc sorrendbe kell tenni es ezt ki kell irni a abc.txt alomanyba.(minden sorhoz kell tartoznia egy erteknek) """
with open("abc.txt", "wt", encoding="ASCII") as f:
    for szo in szotar.values():
        f.write(''.join(sorted(szo["szo karakterenkent"]))+"\n")

print("4. feladat")
"""Be kell kerni a felhasznalotol 2 szot es meg kell hataronzi hogy anagramma-e egymasnak a ket szo."""
szobekeres1 = list(input("Kerem adja meg az elso vizsgalt szot: "))
szobekeres2 = list(input("Kerem adja meg a masodik vizsgalt szot: "))
szo1 = anagramma(szobekeres1)
szo2 = anagramma(szobekeres2)
if szo1 == szo2:
    print("Anagramma")
else:
    print("Nem anagramma")


print("5. feladat")
"""Felhasznalotol egy szo bekeres es az allomany szavaibol megkeresni hogy ha van talalat akkor egymas ala kiirni."""   
szokereso = list(input("Kerem irjon be egy szot aminek az anagrammajat megkeresi a szotar alomanyban: "))
n = 0
for a in szotar.values():
    if anagramma(szokereso) == a["anagramma"]:
        print(a["szo"])
        n+=1
if n == 0:
    print("Nincs a szotarban anagramma.")

print("6. feladat")
"""Meg kell hatarozni hogy a szotar allomanyban melyik a leghosszabb szo es ki kell iratni a kepenyore """
szotarleghosszabb = {}
for k,v in szotar.items():
    szotarleghosszabb[k] = len(v["szo"])
for d,f in szotarleghosszabb.items():
    if f == max(szotarleghosszabb.values()):
        print(szotar[d]["szo"])

print("7. feladat")
"""karakter szam szerinti novekvo sorrendbe rendezes, egymas amagramma szavai keruljenek egy sorba szokozzel elvalasztva nem ugyanaz a karaktert \
tartalmazo lista szamvai keruljenek egy sorba kulonboyo hasszusagu szavak egy sor sortoressel keruljenek az alomanyba  """


""" Itt csinalok egy uj szotarat, ahol a kulcs a szo hossza es a belso konyvtar kulcsa az
anagramma osszefuzve egy sztringe:
szavak = {
    4: {
        'akku': ['kuka','akku'],
        'aipp': ['papi', 'pipa']
    },
    5: {
        ...
    }
}"""

# toltsuk fel ezt az uj szotarat a 'szotar' nevu szotarbol
szavak = {}
for k,v in szotar.items():
    hossz = len(v['szo'])
    if hossz not in szavak:
        szavak[hossz] = {}
    anagramma = ''.join(v['anagramma'])
    if anagramma not in szavak[hossz]:
        szavak[hossz][anagramma] = []
    szavak[hossz][anagramma].append(v['szo'])

#print(szavak)

""" most pedig csak kiirom ezt a szotarat """
with open("rendezve.txt","wt", encoding="ASCII") as f:
    elozo_hossz = 0
    for k,v in sorted(szavak.items()):
        if elozo_hossz != 0 and elozo_hossz != k:
            f.write("\n")
        for k2, v2 in v.items():
            f.write(' '.join(v2)+'\n')
        elozo_hossz = k