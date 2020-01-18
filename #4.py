#ohjelma yhdistää listat ottamalla niiden pituuden ja sen jälkeen käymällä pituuden läpi for-loopin rangen avulla
#ja lisäämällä vuorotellen niiden osat uuteen listaan

keksija=["Einstein", "Lovelace", "Kopernikus", "Curie"]
Galilei=["Io", "Europa", "Ganymedes", "Kallisto"]

pimpelipompeli=[]

def listasolmu():
    z=len(keksija)
    for x in range(z):
        pimpelipompeli.append(keksija[x])
        pimpelipompeli.append(Galilei[x])
    print(pimpelipompeli)

listasolmu()