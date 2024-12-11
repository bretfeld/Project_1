# různé operace s datovým typem str a int
# vypočítat cenu za dva Mercedesy, uložit ji do proměnné cena_2_merc 
mercedes = 150_000
print ("2 Mercedesy stoji",2*mercedes )

# vypočítat cenu za Mercedes a Rolls-Royce, uložit ji do proměnné cena_merc_a_rolls
rolls_royce = 400_000
cena_merc_a_rolls = mercedes + rolls_royce
print ("Mercedes a Rolls stoji",cena_merc_a_rolls )

# vypočítat cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich), uložit ji do proměnné cena_2_rolls_s_vybavou
vybava = 50_000
cena_2_rolls_s_vybavou = (2*rolls_royce) + (2*vybava)
print (" Dva Rollsy s vybavou  stoji", cena_2_rolls_s_vybavou)

# vypočítat cenu za Mercedes s příplatkovou výbavou, uložit ji do proměnné
print (" Mercedes s vybavou stoji",vybava + mercedes )

# vypočítat cenu po slevě Mercedesu a uložit ji do proměnné merc_se_slevou
sleva_merc = 5000
merc_se_slevou = mercedes - sleva_merc
print ("cena po slevě Mercedesu", merc_se_slevou ) 