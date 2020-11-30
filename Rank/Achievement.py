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

for j in range(1, 6):
    # 랭킹
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

    url = 'https://maplestory.nexon.game.naver.com/Ranking/Achievement?page=' + str(j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="ach_img")

    imgURL_2 = []
    imageNum = 0
    for i in soup:
        imgURL_2.append(i.find("img")["src"])

    url = 'https://maplestory.nexon.game.naver.com/Ranking/Achievement?page=' + str(5 + j)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("td", class_="ach_img")

    imageNum = 0
    for i in soup:
        imgURL_2.append(i.find("img")["src"])

    for i in range(1, 11):
        character = {}
        driver.get('https://maple.gg/rank/achievement?page=' + str(j))
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
        ratingImg = imgURL_2[i - 1]
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text

        driver.get('https://maplestory.nexon.game.naver.com/Ranking/Achievement?page=' + str(2 * j - 1))
        rating = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]/span').text
        character['rating'] = rating
        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['point'] = point
        worldRank.append(character)
    for i in range(11, 21):
        character = {}
        driver.get('https://maple.gg/rank/achievement?page=' + str(j))
        rank = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/th').text
        img = imgURL[ + i - 1]
        serverImg = imgURL_1[ + i - 1]
        charName = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/span/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[1]').text
        job = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/div[2]/div[1]/span[3]').text
        ratingImg = imgURL_2[i - 1]
        point = driver.find_element_by_xpath(
            '//*[@id="app"]/section[4]/section/div/table/tbody/tr[' + str(i) + ']/td[3]').text
        character['rank'] = rank
        character['img'] = img
        character['serverImg'] = serverImg
        character['name'] = charName
        character['level'] = level
        character['job'] = job
        character['ratingImg'] = ratingImg
        character['point'] = point

        driver.get('https://maplestory.nexon.game.naver.com/Ranking/Achievement?page=' + str(2 * j))
        rating = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i - 10) + ']/td[3]/span').text
        character['rating'] = rating
        worldRank.append(character)

data['worldRank'] = worldRank

with open('Achievement.json', 'w', encoding="utf-8") as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent="\t")
