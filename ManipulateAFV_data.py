import numpy as np
import csv
import pandas as pd 
from sortedcontainers import SortedDict

#Reading in data source and cleaning from missing values in certain columns. 
data = pd.read_csv("/Users/alexanderlindell/Documents/Programmering /Python/Afv_data.csv",delimiter=';')
temp = data[data['Utveckling(%)'] == '-'].index
data.drop(temp,inplace=True)
temp = data[data['Utv forsta dagen'] == '-'].index
data.drop(temp,inplace=True)

#Making dict of flags to be able to sort and calculate mean of utv corresponing to a certain flag. 
flagsdatautv = {}
for i in range(len(data)): 
    flagsdatautv[int(data.iloc[i].loc['Flaggor(st)'])] = []
for i in range(len(data)):     
    flagsdatautv[int(data.iloc[i].loc['Flaggor(st)'])].append(int(data.iloc[i].loc['Utveckling(%)']))
sortedflagsdatautv = SortedDict(flagsdatautv)  


flagsdatautvfirst = {}
for i in range(len(data)): 
    flagsdatautvfirst[int(data.iloc[i].loc['Flaggor(st)'])] = []
for i in range(len(data)):     
    flagsdatautvfirst[int(data.iloc[i].loc['Flaggor(st)'])].append(float(data.iloc[i].loc['Utv forsta dagen']))    
sortedflagsdatautvfirst = SortedDict(flagsdatautvfirst) 

#Writing the new csvfile with information about flags.
calcflagsfile = "Flags.csv"  
flagscolumns = ['Flaggor', 'Utv', 'AndelPos', 'firstDay','AndelPosFD']
try: 
    with open(calcflagsfile,'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=flagscolumns)
        writer.writeheader()
        for element in range(len(sortedflagsdatautv)):
            writer.writerow({'Flaggor':element,
                            'Utv':round(np.mean(sortedflagsdatautv[element])/100,2),
                            'AndelPos':round((np.array(sortedflagsdatautv[element])>0).sum()/len(sortedflagsdatautv[element]),2),
                            'firstDay':round(np.mean(sortedflagsdatautvfirst[element])/100,2),
                            'AndelPosFD':round((np.array(sortedflagsdatautvfirst[element])>0).sum()/len(sortedflagsdatautv[element]),2)}) 
except IOError:
    print("I/O error")


#Writing new csvfile with information about "Andel Emission"
calcAndelEmission = "AndelEmission.csv"
AndelEmissionscolumns = ['Company', 'Emission', 'Utv', 'Utv first day']
try: 
    with open(calcAndelEmission,'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=AndelEmissionscolumns)
        writer.writeheader()
        for row in range(len(data)):
            writer.writerow({'Company':data.iloc[row].loc['Bolag'],
                            'Emission':round(data.iloc[row].loc['Andel nyemission(%)']/100,2),
                            'Utv':round(int(data.iloc[row].loc['Utveckling(%)'])/100,2),
                            'Utv first day':round(float(data.iloc[row].loc['Utv forsta dagen'])/100,2)}) 
except IOError:
    print("I/O error")

#Writing new csvfile with information about "Andel Säkrad"
calcAndelSakrad = "AndelSakrad.csv"
AndelSakradcolumns = ['Company', 'Andel sakrad', 'Utv', 'Utv first day']
try: 
    with open(calcAndelSakrad,'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=AndelSakradcolumns)
        writer.writeheader()
        for row in range(len(data)):
            writer.writerow({'Company':data.iloc[row].loc['Bolag'],
                            'Andel sakrad':round(data.iloc[row].loc['Andel sakrad(%)']/100,2),
                            'Utv':round(int(data.iloc[row].loc['Utveckling(%)'])/100,2),
                            'Utv first day':round(float(data.iloc[row].loc['Utv forsta dagen'])/100,2)}) 
except IOError:
    print("I/O error")

#Writing new csvfile with information about "Nyckelpersons ägande"
calcNyckelpersonsAgande = "NyckelpersonsAgande.csv"
NyckelpersonsAgandecolumns = ['Company', 'Nyckelpersons Agande', 'Utv', 'Utv first day']
try: 
    with open(calcNyckelpersonsAgande,'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=NyckelpersonsAgandecolumns)
        writer.writeheader()
        for row in range(len(data)):
            if data.iloc[row].loc['Nyckelpersons agande'] != 'Uppgiftsaknas':
                writer.writerow({'Company':data.iloc[row].loc['Bolag'],
                                'Nyckelpersons Agande':round(float(data.iloc[row].loc['Nyckelpersons agande'])/100,2),
                                'Utv':round(int(data.iloc[row].loc['Utveckling(%)'])/100,2),
                                'Utv first day':round(float(data.iloc[row].loc['Utv forsta dagen'])/100,2)})

except IOError:
    print("I/O error")    


