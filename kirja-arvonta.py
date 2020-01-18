import random



kirjat=[]
ihmiset=["Hanna", "Jukka", "Minna", "Mauno"]

kirjalista=[]

thislist=[]


f = open("demofile.txt", "r")
for x in f:
  kirjat.append(x)

z=len(kirjat)
for x in range(z):
    thislist.append(random.randrange(1, z+1))

def klista():
    z=len(kirjat)
    for x in range(z):
        kirjalista.append(thislist[x])
        kirjalista.append(kirjat[x])
        kirjalista.append(ihmiset[x])
    print(kirjalista)

klista()