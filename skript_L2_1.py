# Vytvoří list zamestnanci, který obsahuje hodnoty:

zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
print (zamestnanci)

# Ulož poslední index ze zadaného listu zamestnanci do proměnné posledni_index

posledni_index = (len(zamestnanci))

# Vypiš jméno na indexu 2 za string: 'Na indexu 2 je: '

print ('Na indexu 2 je: ', zamestnanci[2])

# Vypiš jméno na posledním indexu za string: 'Na <posledni_index> indexu je:'

print ('Na <posledni_index> indexu je:', posledni_index)

# vypiš jména od indexu 2 do 5 za string: 'V intervalu od 2 do 5 je:'

print ('V intervalu od 2 do 5 je:', zamestnanci[2:6])

# vypiš každý třetí prvek listu zamestnanci počínaje hodnotou 'František' za string: 'Každý třetí člen je:'.

print ('Každý třetí člen je:', zamestnanci[::3])
print ()
print ()

# Rovnice výpočtu BMI: váha / výška2.
# V této úloze vytvoř program, který získá BMI uživatele Martin, který měří 200 centimerů a váží 80 kilogramů:
# Vytvoř proměnné jmeno, vaha, vyska a zadej do nich hodnoty

vaha = int (80)
vyska = int (2)
jmeno = "Martin"
print (jmeno, ('ma'),vaha,('kg'), vyska,('m'))

# vytvoř proměnnou bmi a přiřaď k ní vzorec, pomocí proměnných vaha, vyska a aritmetického operátoru na druhou 
bmi = (vaha)/(vyska**2)
print('BMI',bmi)
if bmi<18.5:
    print ('Ma podvyzivu')
if (bmi>=18.5) and (bmi<25):
    print ('Ma zdravou vahu')
if (bmi>=25) and (bmi<30):
    print('Mírná nadváha')
if (bmi>=30) and (bmi<=40):
    print('	Obezita')
if bmi>40:
    print ('Tezka obezita')
print ()
print ()


# Vytvoř list zamestnanci, který bude obsahovat stringy 'František', 'Anna', 'Jakub', 'Klára'
zamestnanci = ['František','Anna','Jakub','Klára']
# vypiš obsah zamestnanci za větu 'Zaměstnanci na začátku: '
print ('Zaměstnanci na začátku: ',zamestnanci)
# vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_a
zamestnanci_a = zamestnanci
# přidej do listu zamestnanci_a jména 'Bruno' a 'Anežka'
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')
# vypiš obsah listu zamestnanci_a za string 'Nová jména přidána: '
print ('Nová jména přidána: ',zamestnanci_a)
# vytvoř kopii listu zamestnanci a pojmenuj proměnnou 
zamestnanci_b = zamestnanci
# vlož jméno 'Bruno' na index 1
zamestnanci_b.insert(1, "Bruno")
# Výpis seznamu "zamestnanci"
print("Nová jména vložena:", zamestnanci_b)
print ()
print ()


# Tvým úkolem bude ověřit správnost prvního písmene každého dne v týdnu.
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
# vytvoř proměnnou cislo_dne a zapiš do ní hodnotu 3
cislo_dne = 3
# ověř, jestli hodnota v cislo_dne je v listu vstupni_cisla
if cislo_dne in vstupni_cisla:
    print ("Správná vstupní hodnota!")
 # pokud ano, hodnotu uprav a použij jako index
    # u 'tyden' (1 --> 'pondělí', 2 --> 'úterý', ..)
    den_tydne = tyden[cislo_dne - 1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        # pokud jsou shodné
        print("Správné písmeno")
    else:
        # ... pokud jsou různé
        print("Špatné písmeno!")
else:
    # pokud ne, upozorni na chybný vstup
    print("Špatná vstupní hodnota!")