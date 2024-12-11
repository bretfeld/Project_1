# Vytvoří list zamestnanci, který obsahuje hodnoty:

zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
print (zamestnanci)

# Ulož poslední index ze zadaného listu zamestnanci do proměnné posledni_index


print (zamestnanci[7])
posledni_index = (len(zamestnanci))
print (posledni_index)

# Uloží hodnotu "Lukáš", do proměnné jmeno
jmeno = "Lukas"
print (jmeno)

# uloží hodnotu "Dvořák", do proměnné prijmeni
prijmeni = "Dvorak"
print (prijmeni)

# vytvoří proměnnou cele_jmeno, do které spojíš hodnoty v proměnných jmeno a prijmeni oddělené mezerou
cele_jmeno = jmeno + " " + prijmeni
print ("Cele jneno:", cele_jmeno)

# vytvoří proměnnou delka_jmena, která bude obsahovat délku hodnoty v proměnné cele_jmeno (započítej i přidanou mezeru)
delka_jmena = len(jmeno + " " + prijmeni)
print ("Delka jmena:", delka_jmena)

# vypíše proměnnou cele_jmeno, která bude shora i zespoda ohraničená řadami rovnítek
print ("=" *12)
print (cele_jmeno)
print ("=" *12)