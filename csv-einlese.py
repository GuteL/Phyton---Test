import csv
import pandas as pd


df = pd.read_csv('data.csv', delimiter=',', encoding='utf-8')

df.rename(columns={'ProduktID_neu': 'ProduktID'}, inplace=True)

if df['Produktname'].iloc[1] == 'Laptop':
    df['Produktname'] = df['Produktname'].replace('Laptop', 'Notebook')
    df['Preis'] = df['Preis'] * 1.2  
    df['Lagerbestand'] = df['Lagerbestand'] -10
    print("Produktname wurde geändert und Preis angepasst.")
else:
    print("Produktname ist nicht Laptop")
    
df.drop(columns=['Kategorie'], inplace=True)

df.to_csv('data_neu.csv', index=False, encoding='utf-8')

print(df)

# --------------------------------------------------------------------------
# änderungen = []
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',')
#     fieldnames = reader.fieldnames.copy()  
#     for row in reader:
#         if 'ProduktID' in fieldnames:
#             index = fieldnames.index('ProduktID')
#             fieldnames[index] = 'ProduktID_neu'
#         änderungen.append(row)
        
# with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
#     writer.writeheader()
#     writer.writerows(änderungen)
    
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',')
#     for row in reader:
#         print(row)




# -------------------------------------------------------------------------------
# änderungen = []
# with open('data.csv', 'r+') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         if row[0] == 'ProduktID':
#             row[0] = 'ProduktID_neu'
#         änderungen.append(row)

# with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(änderungen)

# with open('data.csv') as csvfile:
#     grint = csv.reader(csvfile, delimiter=',') 
#     for row in grint:
#         print(row)

        
        