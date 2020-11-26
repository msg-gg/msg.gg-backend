# pip install selenium
# pip install webdriver-manager
import re
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

driver.get('https://maple.gg/job/nightlord')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        nightlord.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        nightlord.append(top)

driver.get('https://maple.gg/job/nightwalker')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        nightwalker.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        nightwalker.append(top)

driver.get('https://maple.gg/job/darkknight')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        darkknight.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        darkknight.append(top)

driver.get('https://maple.gg/job/demonslayer')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        demonslayer.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        demonslayer.append(top)

driver.get('https://maple.gg/job/demonavenger')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        demonavenger.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        demonavenger.append(top)

driver.get('https://maple.gg/job/dualblader')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        dualblader.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        dualblader.append(top)

driver.get('https://maple.gg/job/luminous')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        luminous.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        luminous.append(top)

driver.get('https://maple.gg/job/mercedes')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        mercedes.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        mercedes.append(top)

driver.get('https://maple.gg/job/mechanic')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        mechanic.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        mechanic.append(top)

driver.get('https://maple.gg/job/mihile')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        mihile.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        mihile.append(top)

driver.get('https://maple.gg/job/viper')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        viper.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        viper.append(top)

driver.get('https://maple.gg/job/battlemage')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        battlemage.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        battlemage.append(top)

driver.get('https://maple.gg/job/bowmaster')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        bowmaster.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        bowmaster.append(top)

driver.get('https://maple.gg/job/blaster')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        blaster.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        blaster.append(top)

driver.get('https://maple.gg/job/bishop')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        bishop.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        bishop.append(top)

driver.get('https://maple.gg/job/shadower')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        shadower.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        shadower.append(top)

driver.get('https://maple.gg/job/soulmaster')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        soulmaster.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        soulmaster.append(top)

driver.get('https://maple.gg/job/striker')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        striker.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        striker.append(top)

driver.get('https://maple.gg/job/marks')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        marks.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        marks.append(top)

driver.get('https://maple.gg/job/adele')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        adele.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        adele.append(top)

driver.get('https://maple.gg/job/aran')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        aran.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        aran.append(top)

driver.get('https://maple.gg/job/ark')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        ark.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        ark.append(top)
driver.get('https://maple.gg/job/arkmagefp')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        arkmagefp.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        arkmagefp.append(top)
driver.get('https://maple.gg/job/arkmagetc')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        arkmagetc.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        arkmagetc.append(top)
driver.get('https://maple.gg/job/evan')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        evan.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        evan.append(top)
driver.get('https://maple.gg/job/angelicbuster')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        angelicbuster.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        angelicbuster.append(top)
driver.get('https://maple.gg/job/wildhunter')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        wildhunter.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        wildhunter.append(top)
driver.get('https://maple.gg/job/windbreaker')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        windbreaker.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        windbreaker.append(top)
driver.get('https://maple.gg/job/shade')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        shade.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        shade.append(top)
driver.get('https://maple.gg/job/illium')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        illium.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        illium.append(top)
driver.get('https://maple.gg/job/xenon')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        xenon.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        xenon.append(top)
driver.get('https://maple.gg/job/zero')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        zero.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        zero.append(top)
driver.get('https://maple.gg/job/cadena')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        cadena.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        cadena.append(top)
driver.get('https://maple.gg/job/kaiser')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        kaiser.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        kaiser.append(top)
driver.get('https://maple.gg/job/cannonmaster')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        cannonmaster.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        cannonmaster.append(top)
driver.get('https://maple.gg/job/captain')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        captain.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        captain.append(top)
driver.get('https://maple.gg/job/kinesis')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        kinesis.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        kinesis.append(top)
driver.get('https://maple.gg/job/paladin')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        paladin.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        paladin.append(top)
driver.get('https://maple.gg/job/pathfinder')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        pathfinder.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        pathfinder.append(top)
driver.get('https://maple.gg/job/phantom')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        phantom.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        phantom.append(top)
driver.get('https://maple.gg/job/flamewizard')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        flamewizard.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        flamewizard.append(top)
driver.get('https://maple.gg/job/hoyoung')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        hoyoung.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        hoyoung.append(top)
driver.get('https://maple.gg/job/hero')
for j in range(1, 4):
    top = {}
    title = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/header').text
    topRecode = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/h1').text
    topTime = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/small').text
    nameLevel = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[1]/span').text
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[2]/span').text
    date = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
    if j != 3:
        top['title'] = title
        top['topRecode'] = topRecode
        top['topTime'] = topTime
        top['nameLevel'] = nameLevel
        top['ranking'] = ranking
        top['date'] = date
        hero.append(top)
    else:
        top['title'] = title
        top['ranking'] = topRecode
        top['jobCount'] = topTime
        top['people'] = nameLevel
        top['ratio'] = ranking
        top['date'] = date
        hero.append(top)

data['nightlord'] = nightlord
data['nightWalker'] = nightwalker
data['darkknight']=darkknight
data['demonslayer']=demonslayer
data['demonavenger']=demonavenger
data['dualblader']=dualblader
data['luminous']=luminous
data['mercedes']=mercedes
data['mecanic']=mechanic
data['mikhail']=mihile
data['viper']=viper
data['battleMage']=battlemage
data['bowmaster']=bowmaster
data['blaster']=blaster
data['bishop']=bishop
data['shadower']=shadower
data['soulMaster']=soulmaster
data['striker']=striker
data['marks']=marks
data['adele']=adele
data['aran']=aran
data['ark']=ark
data['arkmagefp']=arkmagefp
data['arkmagetc']=arkmagetc
data['evan']=evan
data['angelicbuster']=angelicbuster
data['wildHunter']=wildhunter
data['windBreaker']=windbreaker
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
data['flameWizard']=flamewizard
data['hoyoung']=hoyoung
data['hero']=hero

with open('Job.json', 'w', encoding="utf-8") as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent="\t")
