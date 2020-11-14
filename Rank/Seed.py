# pip install selenium
# pip install webdriver-manager
import soup as soup
import time
from selenium import webdriver
import pandas
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)  # 웹 자원 로드를 위해 3초 기다려줌

driver.get('https://maplestory.nexon.com/Ranking/World/Total')  # url 접근

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
SeedRank = []
reboot1SeedRank = []
reboot2SeedRank = []
auroraSeedRank = []
redSeedRank = []
enosisSeedRank = []
unionSeedRank = []
scaniaSeedRank = []
lunaSeedRank = []
zenithSeedRank = []
croaSeedRank = []
veraSeedRank = []
elysiumSeedRank = []
arcaneSeedRank = []
novaSeedRank = []

for j in range(1, 11):

    # 전체월드 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + '&w=0')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        SeedRank.append(character)

    # 리부트2 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=1')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        reboot2SeedRank.append(character)

    # 리부트1 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=2')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        reboot1SeedRank.append(character)

    # 오로라 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=3')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        auroraSeedRank.append(character)

    # 레드 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=4')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        redSeedRank.append(character)

    # 이노시스 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=5')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        enosisSeedRank.append(character)

    # 유니온 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=6')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        unionSeedRank.append(character)

    # 스카니아 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=7')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        scaniaSeedRank.append(character)

    # 루나 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=8')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        lunaSeedRank.append(character)

    # 제니스 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=9')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        zenithSeedRank.append(character)

    # 크로아 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=10')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        croaSeedRank.append(character)

# 베라 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=11')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        veraSeedRank.append(character)

    # 엘리시움 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=12')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        elysiumSeedRank.append(character)

    # 아케인 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=13')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        arcaneSeedRank.append(character)

    # 노바 랭킹
    driver.get('https://maplestory.nexon.game.naver.com/Ranking/World/Seed/ThisWeek?page=' + str(j) + ' &w=14')
    for i in range(1, 11):
        character = {}
        charName = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/dl/dt/a').text
        level = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]').text
        recode = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]').text
        recodeTime = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[5]').text

        character['name'] = charName
        character['level'] = level
        character['recode'] = recode
        character['recodeTime'] = recodeTime
        novaSeedRank.append(character)

data.append(SeedRank)
data.append(reboot2SeedRank)
data.append(reboot1SeedRank)
data.append(auroraSeedRank)
data.append(redSeedRank)
data.append(enosisSeedRank)
data.append(unionSeedRank)
data.append(scaniaSeedRank)
data.append(lunaSeedRank)
data.append(zenithSeedRank)
data.append(croaSeedRank)
data.append(veraSeedRank)
data.append(elysiumSeedRank)
data.append(arcaneSeedRank)
data.append(novaSeedRank)

print(data)
import json

# 첫번째 crawling 방법 : xpath를 통해 crawling하는 방법 <아래 글 참고>
'''
//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[2]/dl/dt/a
//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/dl/dt/a
'''
# driver.find_element_by_xpath('//paper-button[@class="dropdown-trigger style-scope yt-dropdown-menu"]').click()
# driver.find_element_by_xpath('//paper-listbox[@class="dropdown-content style-scope yt-dropdown-menu"]/a[1]').click()