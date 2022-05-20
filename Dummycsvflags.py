import requests
import csv

""" csv_file = "Flags.csv"
csv_columns = ["Flaggor","Utv","Andel pos","Utv first day", "Andel pos"]
#data =  

try: 
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
        
        writer.writeheader(csv_columns)
        
        writer.writerow(0,0.7,0.9,0.3,0.9)
        writer.writerow(1,0.5,0.7,0.2,0.8)
except IOError:
    print("I/O error")


    import csv """

# csv header
fieldnames = ['Flaggor', 'Utv', 'Andel pos', 'Utv first day','Andel pos']

# csv data
rows = [
    {'Flaggor': '0',
    'Utv': '0,7',
    'Andel pos': '0,9',
    'Utv first day': '0,2',
    'Andel pos': '0,8'},
    {'Flaggor': '1',
    'Utv': '0,5',
    'Andel pos': '0,8',
    'Utv first day': '0,7',
    'Andel pos': '0,7'},
    {'Flaggor': '2',
    'Utv': '0,5',
    'Andel pos': '0,4',
    'Utv first day': '0,3',
    'Andel pos': '0,5'},
    {'Flaggor': '3',
    'Utv': '0,4',
    'Andel pos': '0,2',
    'Utv first day': '0,1',
    'Andel pos': '0,1'}
   
]

with open('Flags.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


fieldnames = ['Company', 'Emission', 'Utv', 'Utv first day']

# csv data
rows = [
    {'Company': 'Company1',
    'Emission':'0.7',
    'Utv': '0.7',
    'Utv first day': '0.2'},
    {'Company': 'Company2',
    'Emission':'0.6',
    'Utv': '0.5',
    'Utv first day': '0.7'},
    {'Company': 'Company2',
    'Emission':'0.4',
    'Utv': '0.5',
    'Utv first day': '0.3'},
    {'Company': 'Company3',
    'Utv': '0.4',
    'Andel pos': '0.2',
    'Utv first day': '0.1'}
   
]

with open('AndelEmission.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)    