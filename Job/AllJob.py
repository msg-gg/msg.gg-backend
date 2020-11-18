import json
# with open("groups.json") as groups:
# 	groups_json = json.load(groups)
#
# 	print(groups_json["group1"])
import time
from collections import OrderedDict

from selenium import webdriver
import pandas
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
from sys import path

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)  # 웹 자원 로드를 위해 3초 기다려줌

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 이미지 크롤링

body = driver.find_element_by_tag_name('body')
from collections import OrderedDict
import json

data = OrderedDict()
world = []
reboot = []
reboot2 = []
aurora = []
red = []
enosis = []
union = []
scania = []
luna = []
zenith = []
croa = []
bera = []
elysium = []
arcane = []
nova = []
driver.get('https://maple.gg/world')
for i in range(1, 45):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    world.append(character)

driver.get('https://maple.gg/world/luna')
for i in range(1, 45):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    luna.append(character)

driver.get('https://maple.gg/world/scania')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    scania.append(character)

driver.get('https://maple.gg/world/elysium')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    elysium.append(character)

driver.get('https://maple.gg/world/reboot')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    reboot.append(character)

driver.get('https://maple.gg/world/croa')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    croa.append(character)

driver.get('https://maple.gg/world/aurora')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    aurora.append(character)

driver.get('https://maple.gg/world/bera')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    bera.append(character)

driver.get('https://maple.gg/world/red')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    red.append(character)

driver.get('https://maple.gg/world/union')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    union.append(character)

driver.get('https://maple.gg/world/zenith')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    zenith.append(character)

driver.get('https://maple.gg/world/enosis')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    enosis.append(character)
driver.get('https://maple.gg/world/reboot2')

for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    reboot2.append(character)

driver.get('https://maple.gg/world/arcane')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    arcane.append(character)

driver.get('https://maple.gg/world/nova')
for i in range(1, 44):
    character = {}
    rank = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[1]').text
    name = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[2]').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/section/div/div/div[1]/div[' + str(i) + ']/div[3]/div/div').text
    character['world'] = rank
    character['name'] = name
    character['people'] = people
    nova.append(character)

data['world'] = world
data['luna'] = luna
data['scania'] = scania
data['elysium'] = elysium
data['reboot'] = reboot
data['croa'] = croa
data['aurora'] = aurora
data['bera'] = bera
data['red'] = red
data['union'] = union
data['zenith'] = zenith
data['enosis'] = enosis
data['reboot2'] = reboot2
data['arcane'] = arcane
data['nova'] = nova

with open('AllJob.json', 'w', encoding="utf-8") as make_file: json.dump(data, make_file, ensure_ascii=False, indent="\t")
