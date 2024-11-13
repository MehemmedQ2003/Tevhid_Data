import requests
from bs4 import BeautifulSoup
import json

url = "https://tevhidmeali.com/sure/fatiha-suresi"
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
ayetler = soup.find_all('div', class_='row ayetler')

result = []
sura_no = "1"
sura_name = "Fatiha"

for index, ayet in enumerate(ayetler, start=1):
    turkce_text = ayet.find('p', class_='turkce-text')
    arapca_text = ayet.find('p', class_='arapca-text')

    if turkce_text and arapca_text:
        ayet_numarasi = turkce_text.find('strong').text.strip()
        turkce_metin = turkce_text.text.strip()
        arapca_metin = arapca_text.text.strip()
        
        for span in arapca_text.find_all('span'):
            span.extract()

        arapca_metin = arapca_text.text.strip()
        turkce_metin = turkce_metin.replace(f"{ayet_numarasi}. ", "")
        
        ayet_info = {
            "id": str(0 + index),
            "suraNo": sura_no,
            "suraName": sura_name,
            "aya": ayet_numarasi,
            "arabic_text": arapca_metin,
            "translation": turkce_metin,  
            "footnotes": None
        }
        result.append(ayet_info)
        
json_output = {"result": result}

with open('sureler/1.fatiha_suresi.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_output, json_file, ensure_ascii=False, indent=2)

print("fatiha Suresi ayetleri 'fatiha_suresi.json' dosyasına kaydedildi.")