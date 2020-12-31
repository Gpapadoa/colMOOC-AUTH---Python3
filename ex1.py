# Άσκηση κώδικα Ενότητας 1 

import math #Βιβλιοθήκη math

print('Δώσε τις καρτεσιανές συντεταγμένες (a1,a2,b1,b2) των διανυσμάτων a και b ώστε να υπολογιστεί η μεταξύ τους γωνία θ καθώς και το συνημίτονο αυτής.')

a1=float(input('a1='))
a2=float(input('a2='))
b1=float(input('b1='))
b2=float(input('b2='))

a_b = a1*b1 + a2*b2 # a.b : εσωτερικό γινόμενο

a = math.sqrt(a1**2 + a2**2) # |a| 

b = math.sqrt(b1**2 + b2**2) # |b|

ab = a*b # |a| * |b|

costh = a_b/ab # συνημίτονο γωνίας θ

goniath = math.degrees( math.acos(costh) ) # γωνία θ σε μοίρες

print('Για τα δεδομένα που έδωσες το συνημίτονο της μεταξύς τους γωνίας θ ειναι:')
print('costh =',costh)
print('Και η γωνία θ σε μοίρες είναι:')
print('goniath =',goniath)

input()






