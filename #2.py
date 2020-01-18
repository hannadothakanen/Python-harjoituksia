#ohjelma pyytää käyttäjältä kahta lukua (nimen omaan lukuina), jotka se sen jälkeen summaa yhteen ja muuttaa takaisin
#stringiksi. Jos luku on yli sata, ohjelma tulostaa if-toimintoa hyödyntäen kommenttia isoista luvuista, ja jos alle
#sata, ohjelma tulostaa else-toimintoa hyödyntäen kommentin kivoista luvuista sekä niiden yhteenlasketun summan.

num1 = int(input('kerro numero: '))
num2 = int(input('kerro toinen numero: '))

summa = str(num1 + num2)

if num1 + num2 >= 100:
    print('Aika isot luvut annoit!')

else:
    print ('Kivat luvut, ne on yhteenlaskettuna ', (summa))