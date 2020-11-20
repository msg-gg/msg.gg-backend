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
unionRank = []
reboot1UnionRank = []
reboot2UnionRank = []
auroraUnionRank = []
redUnionRank = []
enosisUnionRank = []
unionUnionRank = []
scaniaUnionRank = []
lunaUnionRank = []
zenithUnionRank = []
croaUnionRank = []
beraUnionRank = []
elysiumUnionRank = []
arcaneUnionRank = []
novaUnionRank = []
for j in range(1, 6):
    # 전체월드 랭킹
    driver.get('https://maple.gg/rank/union?page=' + str(j))
    url = 'https://maple.gg/rank/union?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        unionRank.append(character)

    # 리부트2 랭킹
    driver.get('https://maple.gg/rank/union/reboot2?page=' + str(j))
    url = 'https://maple.gg/rank/union/reboot2?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        reboot2UnionRank.append(character)

    # 리부트1 랭킹
    driver.get('https://maple.gg/rank/union/reboot?page=' + str(j))
    url = 'https://maple.gg/rank/union/reboot?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        reboot1UnionRank.append(character)

    # 오로라 랭킹
    driver.get('https://maple.gg/rank/union/aurora?page=' + str(j))
    url = 'https://maple.gg/rank/union/aurora?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        auroraUnionRank.append(character)

    # 레드 랭킹
    driver.get('https://maple.gg/rank/union/red?page=' + str(j))
    url = 'https://maple.gg/rank/union/red?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 2):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        redUnionRank.append(character)

    # 이노시스 랭킹
    driver.get('https://maple.gg/rank/union/enosis?page=' + str(j))
    url = 'https://maple.gg/rank/union/enosis?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        enosisUnionRank.append(character)

    # 유니온 랭킹
    driver.get('https://maple.gg/rank/union?page=' + str(j))
    url = 'https://maple.gg/rank/union/union?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        unionUnionRank.append(character)

    # 스카니아 랭킹
    driver.get('https://maple.gg/rank/union/scania?page=' + str(j))
    url = 'https://maple.gg/rank/union/scania?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        scaniaUnionRank.append(character)

    # 루나 랭킹
    driver.get('https://maple.gg/rank/union/luna?page=' + str(j))
    url = 'https://maple.gg/rank/union/luna?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        lunaUnionRank.append(character)

    # 제니스 랭킹
    driver.get('https://maple.gg/rank/union/zenith?page=' + str(j))
    url = 'https://maple.gg/rank/union/zenith?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        zenithUnionRank.append(character)

    # 크로아 랭킹
    driver.get('https://maple.gg/rank/union/croa?page=' + str(j))
    url = 'https://maple.gg/rank/union/croa?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        croaUnionRank.append(character)

# 베라 랭킹
    driver.get('https://maple.gg/rank/union/bera?page=' + str(j))
    url = 'https://maple.gg/rank/union/bera?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        beraUnionRank.append(character)

    # 엘리시움 랭킹
    driver.get('https://maple.gg/rank/union/elysium?page=' + str(j))
    url = 'https://maple.gg/rank/union/elysium?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        elysiumUnionRank.append(character)

    # 아케인 랭킹
    driver.get('https://maple.gg/rank/union/arcane?page=' + str(j))
    url = 'https://maple.gg/rank/union/arcane?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        arcaneUnionRank.append(character)
driver.get('https://maple.gg/rank/union/nova')
people = driver.find_element_by_xpath(
    '//*[@id="app"]/section[4]/section/header/b').text
people = re.findall("\d+", people)
num = people[0]
num = int(num) / 20
    for j in range(1, int(num + 1)):
    # 노바 랭킹
    driver.get('https://maple.gg/rank/union/nova?page=' + str(j))
    url = 'https://maple.gg/rank/union/nova?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("div", class_="d-inline-block mr-2 align-middle")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        unionLevel = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/span').text
        power = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        character['rank'] = rank
        character['img'] = img
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['unionLevel'] = unionLevel
        character['recode'] = power
        novaUnionRank.append(character)

data['unionRank'] = unionRank
data['reboot2UnionRank'] = reboot2UnionRank
data['reboot1UnionRank'] = reboot1UnionRank
data['auroraUnionRank'] = auroraUnionRank
data['redUnionRank'] = redUnionRank
data['enosisUnionRank'] = enosisUnionRank
data['unionUnionRank'] = unionUnionRank
data['scaniaUnionRank'] = scaniaUnionRank
data['lunaUnionRank'] = lunaUnionRank
data['zenithUnionRank'] = zenithUnionRank
data['croaUnionRank'] = croaUnionRank
data['beraUnionRank'] = beraUnionRank
data['elysiumUnionRank'] = elysiumUnionRank
data['arcaneUnionRank'] = arcaneUnionRank
data['novaUnionRank'] = novaUnionRank

with open('Union.json', 'w', encoding="utf-8") as make_file:
	json.dump(data, make_file, ensure_ascii=False, indent="\t")
