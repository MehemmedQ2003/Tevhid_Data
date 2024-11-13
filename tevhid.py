import json
import csv

with open('tevhid.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open('tevhid.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'suraNo','suraName', 'aya', 'arabic_text', 'translation', 'footnotes']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for item in data:
        for result in item['result']:
            writer.writerow(result)

print("Məlumatlar JSON-dan CSV-ə uğurla yazıldı. ✅✅✅")
