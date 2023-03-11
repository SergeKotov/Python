# Source code from the session

import sys
import os

current = os.getcwd()
folder_name = 'PythonHW'

# Format: XML
import xml.etree.ElementTree as ET

file_name = '2_4_newsafr.xml'
file_path = os.path.join(current, folder_name, file_name)
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(file_path, parser)

# root = tree.getroot()
# print('\nFile format exercises\nXML')
# print(type(root))
# print(root.attrib)
# news_list = root.findall("channel/item")
# print(f"Всего в этом файле {len(news_list)} новостей")

# titles_list = root.findall("channel/item/title")
# for title in titles_list:
# 	print(title.text)

# tree.write("files/newsafr2.xml")

# Format: JSON
import json

file_name = '2_4_newsafr.json'
file_path = os.path.join(current, folder_name, file_name)
with open(file_path) as f:
	json_data = json.load(f)

# print('\nFile format exercises\nJSON')
# print(type(json_data))
# news_list = json_data["rss"]["channel"]["items"]
# print(f"Всего в этом файле {len(news_list)} новостей")

# for news in news_list:
# 	print(news["title"])

# json_string = json.dumps(json_data)
# print(json_string)

# with open(file_path, "w") as f:
# 	json.dump(json_data, f, ensure_ascii=False, indent=4)

# Format: CSV
import csv

file_name = '2_4_newsafr.csv'
file_path = os.path.join(current, folder_name, file_name)

print('\nFile format exercises\nCSV')
with open(file_path) as f:
	reader = csv.reader(f)
	counter = -1
	for row in reader:
		print(row)
		counter += 1
print(f"Всего в этом файле {counter} новостей")

# with open(file_path) as f:
# 	reader = csv.reader(f)
# 	news_list = list(reader)

# print(type(news_list))
# print(news_list[:2])
# header = news_list.pop(0)
# for row in news_list:
# 	print(row[-1])

# csv.register_dialect("customcsv_noquote", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
# csv.register_dialect("customcsv_semicolon", delimiter=";")

# with open(file_path, "w") as f:
# 	writer = csv.writer(f, "customcsv_noquote")
# 	writer.writerow(header)
# 	writer.writerows(news_list[:4])
	# for row in news_list[:4]:
	# 	writer.writerow(row)

print()
sys.exit()

# with open(file_path) as f:
# 	reader = csv.DictReader(f)
# 	counter = 0
# 	for row in reader:
# 		print(row["title"])
# 		counter += 1
# print(f"Всего в этом файле {counter} новостей")

# ================================
# ДОПОЛНИТЕЛЬНЫЙ БЛОК
# ================================
# как преобразовать dict в xml
# читаем json. при помощи dicttoxml преобразуем в xml - получаем ТЕКСТ
# дальше этот текст нужно превратить в дерево при помощи функции ET.fromstring()
# зато у нас сразу получается root
# https://pypi.org/project/dicttoxml/ pip install dicttoxml
# from dicttoxml import dicttoxml
# import json

# with open("files/newsafr.json") as f:
# 	json_data = json.load(f)
# print("Преобразуем наш json в xml при помощи dicttoxml")
# xml = dicttoxml(json_data)
# print(type(xml)) # результат - двоичная строка (byte-string). нужно преобразовать ее в обычную 
# root = ET.fromstring(xml.decode("utf-8"))
# # проверяем, что все хорошо с нашим xml (выводим заголовки новостей так же, как делали раньше)
# titles_list = tree.findall("channel/item/title")
# for title in titles_list:
# 	print(title.text)


# # чтобы сохранить xml в более читаемом виде, его придется сначала отформатировать. штатных способов в старых версиях питона (до 3.9) нет, через minidom (как в лекции) - теперь появляются лишние строки, поэтому проще установить и подключить модуль xmlformatter
# # в параметрах Formatter'а указывается тип отступа (пробел, табулятор) и количество отступов
# # в качестве входного значения даем XML, сериализованный в строку
# import xmlformatter
# formatter = xmlformatter.Formatter(indent="2", indent_char=" ")
# prettyxml = formatter.format_string(ET.tostring(root)).decode("utf-8")

# with open("files/newsafr3.xml", "w") as f:
# 	f.write(prettyxml)

# # как превратить XML в словарь
# # самый удобный способ - подключить defaultdict из модуля collections
# # и написать собственную функцию конверсии https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
# from collections import defaultdict

# def etree_to_dict(t):
#     d = {t.tag: {} if t.attrib else None}
#     children = list(t)
#     if children:
#         dd = defaultdict(list)
#         for dc in map(etree_to_dict, children):
#             for k, v in dc.items():
#                 dd[k].append(v)
#         d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
#     if t.attrib:
#         d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
#     if t.text:
#         text = t.text.strip()
#         if children or t.attrib:
#             if text:
#               d[t.tag]['#text'] = text
#         else:
#             d[t.tag] = text
#     return d

# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.parse("files/newsafr.xml", parser)
# root = tree.getroot()
# json_data = etree_to_dict(root)
# with open("files/newsafr3.json", "w") as f:
# 	json.dump(json_data, f, ensure_ascii=False, indent=2)

# ================================
# КОНЕЦ ДОПОЛНИТЕЛЬНОГО БЛОКА
# ================================