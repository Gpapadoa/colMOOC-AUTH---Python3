print('Άσκηση κώδικα Ενότητας 2')

year = int(input('Δώσε έτος για έλεγχο και πάτα enter, Έτος: '))   

if year%100==0 and year%400==0:
    disekto = True
elif year%100!=0 and year%4==0:
    disekto = True
else:
    disekto = False

print('Το έτος',year,'είναι δίσεκτο; Απάντηση:',disekto)

input('Τέλος προγράμματος')
