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

for j in range(1, 6):
    # 오로라 랭킹
    driver.get('https://maple.gg/rank/total/aurora?page' + str(j))
    url = 'https://maple.gg/rank/total/aurora?page=' + str(j)
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

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")


    for i in range(1, 11):
        driver.get('https://maple.gg/rank/total/aurora?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=3')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        auroraRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/aurora?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=3')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        auroraRank.append(character)

    # 레드 랭킹
    driver.get('https://maple.gg/rank/total/red?page=' + str(j))
    url = 'https://maple.gg/rank/total/red?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/red?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=4')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        redRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/red?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=4')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        redRank.append(character)

    # 이노시스 랭킹
    driver.get('https://maple.gg/rank/total/enosis?page=' + str(j))
    url = 'https://maple.gg/rank/total/enosis?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/enosis?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=5')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        enosisRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/enosis?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=5')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        enosisRank.append(character)

    # 유니온 랭킹
    driver.get('https://maple.gg/rank/total/union?page=' + str(j))
    url = 'https://maple.gg/rank/total/union?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/union?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=6')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        unionRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/union?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=6')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        unionRank.append(character)

    # 스카니아 랭킹
    driver.get('https://maple.gg/rank/total/scania?page=' + str(j))
    url = 'https://maple.gg/rank/total/scania?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/scania?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=7')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        scaniaRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/scania?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=7')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        scaniaRank.append(character)

    # 루나 랭킹
    driver.get('https://maple.gg/rank/total/luna?page=' + str(j))
    url = 'https://maple.gg/rank/total/luna?page=' + str(j)
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

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block align-middle")

    imgURL_1 = []
    imageNum = 0
    for i in soup:
        imgURL_1.append(i.find("img")["src"])

    for i in range(1, 11):
        driver.get('https://maple.gg/rank/total/luna?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=8')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        lunaRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/luna?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=8')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        lunaRank.append(character)

    # 제니스 랭킹
    driver.get('https://maple.gg/rank/total/zenith?page=' + str(j))
    url = 'https://maple.gg/rank/total/zenith?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/zenith?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=9')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        zenithRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/zenith?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=9')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        zenithRank.append(character)

    # 크로아 랭킹
    driver.get('https://maple.gg/rank/total/croa?page=' + str(j))
    url = 'https://maple.gg/rank/total/croa?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/croa?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=10')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        croaRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/croa?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=10')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        croaRank.append(character)

# 베라 랭킹
    driver.get('https://maple.gg/rank/total/bera?page=' + str(j))
    url = 'https://maple.gg/rank/total/bera?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/bera?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=11')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        beraRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/bera?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=11')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        beraRank.append(character)

    # 엘리시움 랭킹
    driver.get('https://maple.gg/rank/total/elysium?page=' + str(j))
    url = 'https://maple.gg/rank/total/elysium?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/elysium?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=12')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        elysiumRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/elysium?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=12')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        elysiumRank.append(character)

    # 아케인 랭킹
    driver.get('https://maple.gg/rank/total/arcane?page=' + str(j))
    url = 'https://maple.gg/rank/total/arcane?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/arcane?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=13')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        arcaneRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/arcane?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=13')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        arcaneRank.append(character)

    # 노바 랭킹
    driver.get('https://maple.gg/rank/total/nova?page=' + str(j))
    url = 'https://maple.gg/rank/total/nova?page=' + str(j)
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
        driver.get('https://maple.gg/rank/total/nova?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j - 1) + '&w=14')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
        character['guild'] = guild
        novaRank.append(character)

    for i in range(11, 21):
        driver.get('https://maple.gg/rank/total/nova?page=' + str(j))
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
        popularity = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]').text

        driver.get('https://maplestory.nexon.com/Ranking/World/Total?page=' + str(2 * j) + '&w=14')
        guild = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[6]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['popularity'] = popularity
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

with open('Rank.json', 'w', encoding="utf-8") as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent="\t")
