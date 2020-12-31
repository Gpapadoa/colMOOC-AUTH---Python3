print('Άσκηση κώδικα Ενότητας 3:')

s=input('Δώσε λέξη για έλεγχο: ')

if len(s)==1 :
    print('Μήκος = 1') 
else:
    if s==s[::-1]:
        adict={s:len(s)}
        alist = list(s)
        print(adict,'\n',alist)
    else:
        print('Η λέξη που έδωσες δεν είναι παλίνδρομο.')


input('Τέλος Προγράμματος')
