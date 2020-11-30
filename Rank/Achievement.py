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
reboot1Rank = []
reboot2Rank = []
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
    # 전체
    driver.get('https://maple.gg/rank/achievement?page=' + str(j))
    url = 'https://maple.gg/rank/achievement?page=' + str(j)
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        worldRank.append(character)

    # 리부트2 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        reboot2Rank.append(character)

    # 리부트1 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        reboot1Rank.append(character)

    # 오로라 랭킹
    driver.get('https://maple.gg/rank/achievement/aurora?page' + str(j))
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        auroraRank.append(character)

    # 레드 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        redRank.append(character)

    # 이노시스 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        enosisRank.append(character)

    # 유니온 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        unionRank.append(character)

    # 스카니아 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        scaniaRank.append(character)

    # 루나 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        lunaRank.append(character)

    # 제니스 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        zenithRank.append(character)

    # 크로아 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        croaRank.append(character)

# 베라 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        beraRank.append(character)

    # 엘리시움 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        elysiumRank.append(character)

    # 아케인 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        arcaneRank.append(character)

for j in range(1, 3):
    # 노바 랭킹
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

    for i in range(1, 21):
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
        rating = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['rating'] = rating
        character['point'] = point
        novaRank.append(character)

data['worldRank'] = worldRank
data['reboot2Rank'] = reboot2Rank
data['reboot1Rank'] = reboot1Rank
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

with open('Achievement.json', 'w', encoding="utf-8") as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent="\t")
