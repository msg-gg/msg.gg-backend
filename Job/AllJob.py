import time
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

data = []
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

data.append(world)
data.append(luna)
data.append(scania)
data.append(elysium)
data.append(reboot)
data.append(croa)
data.append(aurora)
data.append(bera)
data.append(red)
data.append(union)
data.append(zenith)
data.append(enosis)
data.append(reboot2)
data.append(arcane)
data.append(nova)
print(data)