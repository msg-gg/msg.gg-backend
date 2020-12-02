# pip install selenium
# pip install webdriver-manager
import urllib

import driver as driver
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
worldRank = []
auroraRank = []
redRank = []
enosisRank = []
unionRank = []
scaniaRank = []
lunaRank = []
zenithRank = []
croaRank = []
beraRank = []
elysiumRank = []
arcaneRank = []
novaRank = []
reboot1Rank = []
reboot2Rank = []

for j in range(1, 6):
    driver.get('https://maple.gg/rank/achievement/luna?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/luna?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        if j == 1 and i == 1:
            ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img04.png'
            rating = '골드'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        lunaRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        lunaRank.append(character)

    driver.get('https://maple.gg/rank/achievement/scania?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/scania?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        scaniaRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        scaniaRank.append(character)

    driver.get('https://maple.gg/rank/achievement/elysium?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/elysium?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        elysiumRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        elysiumRank.append(character)

    driver.get('https://maple.gg/rank/achievement/reboot?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/reboot?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        reboot1Rank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        reboot1Rank.append(character)

    driver.get('https://maple.gg/rank/achievement/croa?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/croa?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        croaRank.append(character)

    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        croaRank.append(character)

    driver.get('https://maple.gg/rank/achievement/aurora?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/aurora?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        auroraRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        auroraRank.append(character)

    driver.get('https://maple.gg/rank/achievement/bera?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/bera?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        beraRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        beraRank.append(character)

    driver.get('https://maple.gg/rank/achievement/red?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/red?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        redRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        redRank.append(character)

    driver.get('https://maple.gg/rank/achievement/union?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/union?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
            imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
            imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        unionRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        unionRank.append(character)

    driver.get('https://maple.gg/rank/achievement/zenith?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/zenith?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
            imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
            imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        zenithRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        zenithRank.append(character)

    driver.get('https://maple.gg/rank/achievement/enosis?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/enosis?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        enosisRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        enosisRank.append(character)

    driver.get('https://maple.gg/rank/achievement/reboot2?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/reboot2?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        reboot2Rank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        reboot2Rank.append(character)

    driver.get('https://maple.gg/rank/achievement/arcane?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/arcane?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
            imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
            imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        arcaneRank.append(character)
    for i in range(11, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[+ i - 1]
        serverImg = imgURL_1[+ i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        arcaneRank.append(character)

for j in range(1, 4):
    driver.get('https://maple.gg/rank/achievement/nova?page=' + str(j))
    url = 'https://maple.gg/rank/achievement/nova?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        serverImg = imgURL_1[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
        rating = '실버'
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        guild = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
        if guild == '':
            guild = '(없음)'

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['rating'] = rating
        character['point'] = point
        character['guild'] = guild
        novaRank.append(character)
    if j == 3:
        for i in range(11, 19):
            character = {}
            rank = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
            img = imgURL[+ i - 1]
            serverImg = imgURL_1[+ i - 1]
            charName = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
            level = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
            job = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
            ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
            rating = '실버'
            point = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
            guild = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
            if guild == '':
                guild = '(없음)'

            character['rank'] = rank
            character['img'] = img
            character['serverImg'] = serverImg
            character['name'] = charName
            character['level'] = level
            character['job'] = job
            character['ratingImg'] = ratingImg
            character['rating'] = rating
            character['point'] = point
            character['guild'] = guild
    else:
        for i in range(11, 21):
            character = {}
            rank = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
            img = imgURL[+ i - 1]
            serverImg = imgURL_1[+ i - 1]
            charName = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
            level = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
            job = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
            ratingImg = 'https://ssl.nx.com/s2/game/maplestory/renewal/common/result_img05.png'
            rating = '실버'
            point = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
            guild = driver.find_element_by_xpath(
                '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text
            if guild == '':
                guild = '(없음)'

            character['rank'] = rank
            character['img'] = img
            character['serverImg'] = serverImg
            character['name'] = charName
            character['level'] = level
            character['job'] = job
            character['ratingImg'] = ratingImg
            character['rating'] = rating
            character['point'] = point
            character['guild'] = guild
        novaRank.append(character)

data['auroraRank'] = auroraRank
data['redRank'] = redRank
data['enosisRank'] = enosisRank
data['unionRank'] = unionRank
data['scaniaRank'] = scaniaRank
data['lunaRank'] = lunaRank
data['zenithRank'] = zenithRank
data['croaRank'] = croaRank
data['beraRank'] = beraRank
data['elysiumRank'] = elysiumRank
data['arcaneRank'] = arcaneRank
data['novaRank'] = novaRank
data['reboot2Rank'] = reboot2Rank
data['reboot1Rank'] = reboot1Rank

with open('Achievement.json', 'w', encoding="utf-8") as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent="\t")
