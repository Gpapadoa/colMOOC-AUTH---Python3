print('Άσκηση κώδικα Ενότητας 4:')

#Συνάρτηση:

def squares(*args):

    if len(args)==1 :
        print('Μηδέν')
        return
    else:
        import statistics as st
        mesos = st.mean(args)

        for k in args:
            yield (mesos-k)**2


#Κυρίως Πρόγραμμα:

for i in squares(3,4,5):
    print(i)

input('Τέλος Προγράμματος.')

