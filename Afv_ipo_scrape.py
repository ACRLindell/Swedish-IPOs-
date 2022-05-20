import requests
import csv
import numpy as np
from bs4 import BeautifulSoup
# Imports data from AFV IPO hemsida and store it as dict in companies.
page = requests.get("https://www.affarsvarlden.se/ipo-guiden/screener")

companies = []
soup = BeautifulSoup(page.content, 'html.parser')

for row in soup.find_all('tr', {"class": "table-row"}):
    col = row.find_all('td')
    if len(col) > 0:
        bolag = col[0].get_text().replace('\n', '').replace('\xa0', '').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        date = col[1].get_text().replace(' ','')
        lista = col[2].get_text().replace(' ','')
        radgivare = col[3].get_text().replace('\t', '').replace('\n', '').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        borsvarde = col[4].get_text().replace('\t','').replace('\n','').replace('Mkr','').replace(' ','')
        flaggor = col[5].get_text().replace('\t','').replace('\n','').replace('st','').replace(' ','')
        teckningskurs = col[6].get_text().replace('\t','').replace('\n','').replace('kr','').replace('.',',').replace(' ','')
        erbjudande = col[7].get_text().replace('\t','').replace('\n','').replace('Mkr','').replace(' ','')
        andel_nyemission = col[8].get_text().replace('\t','').replace('\n','').replace('%','').replace(' ','')
        teckningsatagare = col[9].get_text().replace('\t','').replace('\n','').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        garantiatagare = col[10].get_text().replace('\n','').replace(' ','')
        andel_sakrad = col[11].get_text().replace('\t','').replace('\n','').replace('%','').replace(' ','')
        vd = col[12].get_text().replace('\t','').replace('\n','').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        ordforande = col[13].get_text().replace('\t','').replace('\n','').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        nyckelpersons_agande = col[14].get_text().replace('\t','').replace('\n','').replace('%','').replace(' ','')
        storagare = col[15].get_text().replace('\t','').replace('\n','').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        saljandestoragare = col[16].get_text().replace('\n','').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        storleksklass = col[17].get_text().replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        #affarsvarldens_analys = col[18].get_text().replace('\t','').replace('\n','')
        uttnyttjad_overtilldelning = col[19].get_text().replace('\t','').replace('\n','').replace(' ','')
        utveckling = col[20].get_text().replace('\t','').replace('\n','').replace('%','').replace(' ','')
        utveckling_forsta_dag = col[21].get_text().replace('\t','').replace('\n','').replace('%','').replace(' ','')
        hemsida = col[22].get_text().replace('\n','').replace(' ','')
        ovriga_radgivare = col[23].get_text().replace('\t','').replace('\n','').replace('å', 'a').replace('ö','o').replace('ä','a').replace(' ','')
        #print(utveckling)

        companies.append(
            dict({"Bolag": bolag,
                "Datum": date,
                "Lista": lista,
                "Radgivare": radgivare,
                "Flaggor(st)":flaggor,
                "Erbjudande(Mkr)":erbjudande, 
                "Utveckling(%)":utveckling, 
                "Borsvarde(Mkr)":borsvarde, 
                "Teckningskurs(kr)":teckningskurs, 
                "Andel nyemission(%)":andel_nyemission, 
                "Teckningsatagare":teckningsatagare, 
                "Garantiatagare":garantiatagare,
                "Andel sakrad(%)":andel_sakrad,
                "VD":vd, 
                "Ordforande":ordforande, 
                "Nyckelpersons agande":nyckelpersons_agande, 
                "Storagare":storagare, 
                "Saljande storägare":saljandestoragare, 
                "Storleksklass":storleksklass, 
                #"Afv analys":affarsvarldens_analys, 
                "Uttnyttjad overtilldelning":uttnyttjad_overtilldelning, 
                "Utv forsta dagen":utveckling_forsta_dag, 
                "Hemsida":hemsida, 
                "Ovriga radgivare":ovriga_radgivare})) 

# Writes the data in companies to csv file. 
csv_file = "Afv_data.csv"

csv_columns = []

for keys in companies[0].keys():
    csv_columns.append(keys)
#print(csv_columns)
try: 
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
        writer.writeheader()
        for data in companies:
            writer.writerow(data)
except IOError:
    print("I/O error")

#Extracts "Teckningsåtagare" from companies and stores in csv
teckningsatagare_list = []

for row in range(len(companies)):
    str = companies[row].get("Teckningsatagare")
    temp_list = str.split(",")
    for item in temp_list:
        if item not in teckningsatagare_list and item != "": 
            teckningsatagare_list.append(item)

csv_file2 = "Afv_teckningsatagare.csv"

try: 
    with open(csv_file2, 'w') as csvfile2:
        writer = csv.writer(csvfile2, delimiter=';')
        writer.writerow(["Teckningsatagare"])
        for item in teckningsatagare_list:
            writer.writerow([item])
except IOError:
    print("I/O error")

#Sortering av utveckling per flagga 
    # Filtrera fram en lista per antal flaggor med utv tillhörande
""" for row in range(len(companies)):
    str = companies[row].get("Flaggor(st)","Utveckling(%)","Utv forsta dagen")
    print(str)
 utveckling_per_flaggor = []
for index in range(1,10):
    utveckling_per_flaggor.append([])
for row in range(len(companies)): 
    if companies[row].get("Flaggor(st)") == '0': 
        utveckling_per_flaggor[0].append(companies[row].get("Utveckling(%)"))
    elif companies[row].get("Flaggor(st)") == '1': 
        utveckling_per_flaggor[1].append(companies[row].get("Utveckling(%)"))  """
#print(utveckling_per_flaggor)

#Selenium function
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options

    # DRIVER_PATH = './chromedriver'
    # # driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    # options = Options()
    # options.headless = True
    # options.add_argument("--window-size=1920,1200")

    # driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    # driver.get('https://www.affarsvarlden.se/ipo-guiden/screener')
    # try:
    #     try:
    #         driver.find_element_by_xpath(
    #             '/html/body/div[5]/div/div/div/button').click()
    #     except:
    #         print('adds')
    #         driver.find_element_by_xpath(
    #             '/html/body/div[8]/div/div/div/button').click()
    #     lista = driver.find_element_by_xpath('//*[@id="column-lista"]').click()
    #     radgivare = driver.find_element_by_xpath(
    #         '//*[@id="column-radgivare"]').click()
    #     teckningskurs = driver.find_element_by_xpath(
    #         '//*[@id="column-teckningskurs"]').click()
    #     teckningsatagare = driver.find_element_by_xpath(
    #         '//*[@id="column-teckningsatagare"]').click()
    #     sakrad = driver.find_element_by_xpath(
    #         '//*[@id="column-andel-sakrad"]').click()
    #     sakrad = driver.find_element_by_xpath(
    #         '//*[@id="column-utveckling-forsta-handelsdag"]').click()
    #     driver.save_screenshot('screenshot.png')
    #     print('done')
    #     driver.quit()
    # except:
    #     print('some error')
    #     driver.quit()
