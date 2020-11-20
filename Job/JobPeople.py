# pip install selenium
# pip install webdriver-manager
import urllib

import soup as soup
import time
from selenium import webdriver
import pandas
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)  # 웹 자원 로드를 위해 3초 기다려줌

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 이미지 크롤링

body = driver.find_element_by_tag_name('body')

# 인기순/작성순 선택할 수 있는 영역 클릭
# driver.find_element_by_xpath('//paper-button[@class="dropdown-trigger style-scope yt-dropdown-menu"]').click()
# 인기순 카테고리 클릭
# driver.find_element_by_xpath('//paper-listbox[@class="dropdown-content style-scope yt-dropdown-menu"]/a[1]').click()


page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

# comments=soup.find_all('yt-formatted-string',attrs={'class':'style-scope ytd-comment-renderer'})

cmmt_box = soup.find_all(attrs={'id': 'wrap'})
# real=soup.find('video')
# real=real.get('src')

# print(real)
# //*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[2]/dl/dt/a/text()
# //*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[3]

# //*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/dl/dt/a/text()
from collections import OrderedDict
import json

data = OrderedDict()
nightlord = []
nightwalker = []
darkknight = []
demonslayer = []
demonavenger = []
dualblader = []
luminous = []
mercedes = []
mechanic = []
mihile = []
viper = []
battlemage = []
bowmaster = []
blaster = []
bishop = []
shadower = []
soulmaster = []
striker = []
marks = []
adele = []
aran = []
ark = []
arkmagefp = []
arkmagetc = []
evan = []
angelicbuster = []
wildhunter = []
windbreaker = []
shade = []
illium = []
xenon = []
zero = []
cadena = []
kaiser = []
cannonmaster = []
captain = []
kinesis = []
paladin = []
pathfinder = []
phantom = []
flamewizard = []
hoyoung = []
hero = []

url = 'https://maple.gg/job/nightlord'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/nightlord')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightlord.append(character)

url = 'https://maple.gg/job/nightwalker'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/nightwalker')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightwalker.append(character)

url = 'https://maple.gg/job/darkknight'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/darkknight')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    darkknight.append(character)

url = 'https://maple.gg/job/demonslayer'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/demonslayer')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    demonslayer.append(character)

url = 'https://maple.gg/job/demonavenger'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/demonavenger')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    demonavenger.append(character)

url = 'https://maple.gg/job/dualblader'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/dualblader')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    dualblader.append(character)

url = 'https://maple.gg/job/luminous'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/luminous')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    luminous.append(character)

url = 'https://maple.gg/job/mercedes'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/mercedes')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    mercedes.append(character)

url = 'https://maple.gg/job/mechanic'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/mechanic')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    mechanic.append(character)

url = 'https://maple.gg/job/mihile'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/mihile')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    mihile.append(character)

url = 'https://maple.gg/job/viper'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/viper')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    viper.append(character)

url = 'https://maple.gg/job/battlemage'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/battlemage')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    battlemage.append(character)

url = 'https://maple.gg/job/bowmaster'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/bowmaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    bowmaster.append(character)

url = 'https://maple.gg/job/blaster'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/blaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    blaster.append(character)

url = 'https://maple.gg/job/bishop'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/bishop')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    bishop.append(character)

url = 'https://maple.gg/job/shadower'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/shadower')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    shadower.append(character)

url = 'https://maple.gg/job/soulmaster'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/soulmaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    soulmaster.append(character)

url = 'https://maple.gg/job/striker'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/striker')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    striker.append(character)

url = 'https://maple.gg/job/marks'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/marks')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    marks.append(character)

url = 'https://maple.gg/job/adele'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/adele')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    adele.append(character)

url = 'https://maple.gg/job/aran'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/aran')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    aran.append(character)

url = 'https://maple.gg/job/ark'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/ark')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    ark.append(character)

url = 'https://maple.gg/job/arkmagefp'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/arkmagefp')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    arkmagefp.append(character)

url = 'https://maple.gg/job/arkmagetc'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/arkmagetc')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    arkmagetc.append(character)

url = 'https://maple.gg/job/evan'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/evan')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    evan.append(character)

url = 'https://maple.gg/job/angelicbuster'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/angelicbuster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    angelicbuster.append(character)

url = 'https://maple.gg/job/wildhunter'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/wildhunter')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    wildhunter.append(character)

url = 'https://maple.gg/job/windbreaker'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/windbreaker')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    windbreaker.append(character)

url = 'https://maple.gg/job/shade'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/shade')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    shade.append(character)

url = 'https://maple.gg/job/illium'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/illium')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    illium.append(character)

url = 'https://maple.gg/job/xenon'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/xenon')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightlord.append(character)

url = 'https://maple.gg/job/zero'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/zero')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    zero.append(character)

url = 'https://maple.gg/job/cadena'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/cadena')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    cadena.append(character)

url = 'https://maple.gg/job/kaiser'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/kaiser')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    kaiser.append(character)

url = 'https://maple.gg/job/cannonmaster'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/cannonmaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    cannonmaster.append(character)

url = 'https://maple.gg/job/captain'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/captain')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    captain.append(character)

url = 'https://maple.gg/job/kinesis'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/kinesis')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    kinesis.append(character)

url = 'https://maple.gg/job/paladin'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/paladin')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    paladin.append(character)

url = 'https://maple.gg/job/pathfinder'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/pathfinder')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    pathfinder.append(character)

url = 'https://maple.gg/job/phantom'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/phantom')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    phantom.append(character)

url = 'https://maple.gg/job/flamewizard'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/flamewizard')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    flamewizard.append(character)

url = 'https://maple.gg/job/hoyoung'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/hoyoung')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    hoyoung.append(character)

url = 'https://maple.gg/job/hero'
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()
imgURL = []

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="bg-light-yellow")

for i in soup:
    imgURL.append(i.find("img")["src"])

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("tr", class_="")
for i in soup:
    imgURL.append(i.find("img")["src"])

driver.get('https://maple.gg/job/hero')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
    worldImg = imgURL[j - 1]
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[2]/b/a').text
    ratio = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[3]/div/div').text
    recode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/b').text
    recodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[4]/span').text
    seedRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/b').text
    seedRecodeTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[5]/span').text
    character['ranking'] = ranking
    character['worldImg'] = worldImg
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    hero.append(character)

data['nightlord'] = nightlord
data['nightwalker'] = nightwalker
data['darkknight']=darkknight
data['demonslayer']=demonslayer
data['demonavenger']=demonavenger
data['dualblader']=dualblader
data['luminous']=luminous
data['mercedes']=mercedes
data['mechanic']=mechanic
data['mihile']=mihile
data['viper']=viper
data['battlemage']=battlemage
data['bowmaster']=bowmaster
data['blaster']=blaster
data['bishop']=bishop
data['shadower']=shadower
data['soulmaster']=soulmaster
data['striker']=striker
data['marks']=marks
data['adele']=adele
data['aran']=aran
data['ark']=ark
data['arkmagefp']=arkmagefp
data['arkmagetc']=arkmagetc
data['evan']=evan
data['angelicbuster']=angelicbuster
data['wildhunter']=wildhunter
data['windbreaker']=windbreaker
data['shade']=shade
data['illium']=illium
data['xenon']=xenon
data['zero']=zero
data['cadena']=cadena
data['kaiser']=kaiser
data['cannonmaster']=cannonmaster
data['captain']=captain
data['kinesis']=kinesis
data['paladin']=paladin
data['pathfinder']=pathfinder
data['phantom']=phantom
data['flamewizard']=flamewizard
data['hoyoung']=hoyoung
data['hero']=hero

with open('JobPeople.json', 'w', encoding="utf-8") as make_file:
	json.dump(data, make_file, ensure_ascii=False, indent="\t")