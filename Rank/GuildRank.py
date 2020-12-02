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
rebootRank = []
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
    driver.get('https://maple.gg/rank/guild?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + '&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + '&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        worldRank.append(character)

    #루나
    driver.get('https://maple.gg/rank/guild/luna?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=1&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=1&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        lunaRank.append(character)

    #스카니아
    driver.get('https://maple.gg/rank/guild/scania?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=17&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=7&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        scaniaRank.append(character)

    #엘리시움
    driver.get('https://maple.gg/rank/guild/elysium?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=12&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=12&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        elysiumRank.append(character)

    #리부트
    driver.get('https://maple.gg/rank/guild/reboot?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=2&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=2&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        rebootRank.append(character)

    #크로아
    driver.get('https://maple.gg/rank/guild/croa?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=10&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=10&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        croaRank.append(character)

    #오로라
    driver.get('https://maple.gg/rank/guild/aurora?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=3&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=3&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        auroraRank.append(character)

    #베라
    driver.get('https://maple.gg/rank/guild/bera?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=11&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=11&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        beraRank.append(character)

    #레드
    driver.get('https://maple.gg/rank/guild/red?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=4&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=4&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        redRank.append(character)

    #유니온
    driver.get('https://maple.gg/rank/guild/union?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=6&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=6&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        unionRank.append(character)

    #제니스
    driver.get('https://maple.gg/rank/guild/zenith?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=9&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=9&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        zenithRank.append(character)

    #이노시스
    driver.get('https://maple.gg/rank/guild/enosis?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=5&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=5&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        enosisRank.append(character)

    #리부트2
    driver.get('https://maple.gg/rank/guild/reboot2?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=1&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=1&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        reboot2Rank.append(character)

    #아케인
    driver.get('https://maple.gg/rank/guild/arcane?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=13&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=13&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        arcaneRank.append(character)

    #노바
for j in range(1, 4):
    driver.get('https://maple.gg/rank/guild/nova?page=' + str(j))
    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j - 1) + 'w=14&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    imgURL = []
    imageNum = 0
    for i in soup:
        imgURL.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.com/Ranking/World/Guild?page=' + str(2 * j) + 'w=14&t=1'
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="left")

    for i in soup:
        imgURL.append(i.find("img")["src"])

    for i in range(1, 21):
        character = {}
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        serverImg = imgURL[i * 2 - 1]
        guildName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a').text

        master = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[4]').text

        character['rank'] = rank
        character['serverImg'] = serverImg
        character['guildName'] = guildName
        character['master'] = master
        character['level'] = level
        character['point'] = point
        novaRank.append(character)

data['worldRank'] = worldRank
data['lunaRank'] = lunaRank
data['scaniaRank'] = scaniaRank
data['elysiumRank'] = elysiumRank
data['rebootRank'] = rebootRank
data['croaRank'] = croaRank
data['auroraRank'] = auroraRank
data['beraRank'] = beraRank
data['redRank'] = redRank
data['unionRank'] = unionRank
data['zenithRank'] = zenithRank
data['enosisRank'] = enosisRank
data['reboot2Rank'] = reboot2Rank
data['novaRank'] = novaRank

with open('GuildRank.json', 'w', encoding="utf-8") as make_file:
	json.dump(data, make_file, ensure_ascii=False, indent="\t")
