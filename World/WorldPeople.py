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
data = []
level210 = []
level240 = []
driver.get('https://maple.gg/world')
for i in range(1, 15):
    character = {}
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[5]/div[1]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a/span').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[5]/div[1]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/div/div').text
    character['world'] = world
    character['people'] = people
    level210.append(character)

for i in range(1, 15):
    character = {}
    world = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[5]/div[2]/section/div/table/tbody/tr[' + str(i) + ']/td[1]/a/span').text
    people = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[5]/div[2]/section/div/table/tbody/tr[' + str(i) + ']/td[2]/div/div').text
    character['world'] = world
    character['people'] = people
    level240.append(character)

data.append(level210)
data.append(level240)
print(data)

