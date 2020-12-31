#Άσκηση κώδικα Ενότητας 5:

def data_to_float(data_str):
    data_fl=[]
    for i in data_str:
        data_fl.append(float(i))
    return data_fl

    
# Κυρίως Πρόγραμμα:

with open ('inputdata.txt','r') as fin:
    
    idata = fin.readlines() #αρχικά δεδομένα str
    data = data_to_float(idata) # δεδομένα αφού μετατράπηκαν σε float
    
    
    import statistics as st
    average = round(st.mean(data),3) #Μέσος Όρος δεδομένων με στρογγυλοποίηση στο τρίτο δεκαδικό
    standard_deviation = round(st.stdev(data),3) #Τυπική Απόκλιση δεδομένων με στρογγυλοποίηση στο τρίτο δεκαδικό
    
    out = 'Mέσος όρος = ' + str(average) + '\n' + 'Tυπική απόκλιση = ' + str(standard_deviation)
    with open('outputdata.txt','w',encoding="utf-8") as fout:
        fout.write(out)






    
