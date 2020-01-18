
#Hanna Hakanen 2018
def Ennuste():

    #import random

    print('Tämä on pieni jouluinen peli, joka ennustaa kuinka monen tunnin päästä pukki saapuu.')
    print('Vastaa kysymyksiin kyllä tai ei, ellei muita vastausvaihtoehtoja anneta. Pidä hauskaa ja hyvää joulua!')

    matka_aika = 3

    aatto = input('Onko jouluaatto?')
    if aatto == 'ei':
        print('Pukki tulee vasta jouluaattona')
    else:
        matka = input('Onko pukki lähtenyt jo matkaan?')
        if matka == 'on':
            matka_aika = matka_aika - 2
        humala = input('Onko pukki ottanut terästettyä glögiä lämmikkeeksi?')
        if humala == 'on':
            huppeli = int(input('Kuinka monta mukillista pukki on ottanut? (vastaa numerolla)'))
            matka_aika = matka_aika + huppeli
        petteri = input('Onko Petteri Punakuonon nenä tarpeeksi punainen, jotta pukki löytää perille?')
        if petteri == 'ei':
            matka_aika = matka_aika + 1
        elif petteri == 'on':
            matka_aika = matka_aika - 1
        lumi = input('Onko ulkona lumimyrsky?')
        if lumi == 'on':
            matka_aika = matka_aika + 5
        pipari = input('Onko pukki saanut tarpeeksi piparia?')
        if pipari == 'on':
            matka_aika = matka_aika - 2
        if pipari == 'ei':
            matka_aika = matka_aika + 1
        tuhma = input('Onko tänä vuonna ollut paljon kilttejä lapsia?')
        if tuhma == 'ei':
            matka_aika = matka_aika - 2
        if tuhma == 'on':
            matka_aika = matka_aika + 2
        tuhma2 = input('Oletko sinä ollut kiltti tänä vuonna? (kyllä/en)')
        if tuhma2 == 'kyllä':
            if matka_aika <= 0:
                print('Pukki on ihan pian perillä!')
            else:
                print('Pukki tulee ', matka_aika, ' tunnin päästä')
        elif tuhma2 == 'en':
            print('Pukki tuo sinulle vain risuja, ja tulee sinun luoksesi vasta aivan viimeisenä')

Ennuste()