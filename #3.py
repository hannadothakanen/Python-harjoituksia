#ohjelma looppaa kerran listan läpi, tulostaen jokaisen sen jäsenen vuorotellen ja lopettaa viimeiseen jäseneen

thislist= ["*","**","***","****","*****","******"]
for x in thislist:
    print(x)
    if x == "******":
        break