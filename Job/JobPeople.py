# pip install selenium
# pip install webdriver-manager
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

data = []
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
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightlord.append(character)

driver.get('https://maple.gg/job/nightwalker')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightwalker.append(character)

driver.get('https://maple.gg/job/darkknight')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    darkknight.append(character)

driver.get('https://maple.gg/job/demonslayer')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    demonslayer.append(character)

driver.get('https://maple.gg/job/dualblader')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    dualblader.append(character)

driver.get('https://maple.gg/job/luminous')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    luminous.append(character)

driver.get('https://maple.gg/job/mercedes')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    mercedes.append(character)

driver.get('https://maple.gg/job/mechanic')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    mechanic.append(character)

driver.get('https://maple.gg/job/mihile')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    mihile.append(character)

driver.get('https://maple.gg/job/viper')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    viper.append(character)

driver.get('https://maple.gg/job/battlemage')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    battlemage.append(character)

driver.get('https://maple.gg/job/bowmaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    bowmaster.append(character)

driver.get('https://maple.gg/job/blaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    blaster.append(character)

driver.get('https://maple.gg/job/bishop')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    bishop.append(character)

driver.get('https://maple.gg/job/shadower')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    shadower.append(character)

driver.get('https://maple.gg/job/soulmaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    soulmaster.append(character)

driver.get('https://maple.gg/job/striker')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    striker.append(character)

driver.get('https://maple.gg/job/marks')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    marks.append(character)

driver.get('https://maple.gg/job/adele')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    adele.append(character)

driver.get('https://maple.gg/job/aran')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    aran.append(character)

driver.get('https://maple.gg/job/ark')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    ark.append(character)

driver.get('https://maple.gg/job/arkmagefp')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    arkmagefp.append(character)

driver.get('https://maple.gg/job/arkmagetc')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    arkmagetc.append(character)

driver.get('https://maple.gg/job/evan')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    evan.append(character)

driver.get('https://maple.gg/job/angelicbuster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    angelicbuster.append(character)

driver.get('https://maple.gg/job/wildhunter')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    wildhunter.append(character)

driver.get('https://maple.gg/job/windbreaker')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    windbreaker.append(character)

driver.get('https://maple.gg/job/shade')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    shade.append(character)

driver.get('https://maple.gg/job/illium')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    illium.append(character)

driver.get('https://maple.gg/job/xenon')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightlord.append(character)

driver.get('https://maple.gg/job/xenon')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    nightlord.append(character)

driver.get('https://maple.gg/job/zero')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    zero.append(character)

driver.get('https://maple.gg/job/cadena')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    cadena.append(character)

driver.get('https://maple.gg/job/kaiser')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    kaiser.append(character)

driver.get('https://maple.gg/job/cannonmaster')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    cannonmaster.append(character)

driver.get('https://maple.gg/job/captain')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    captain.append(character)

driver.get('https://maple.gg/job/kinesis')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    kinesis.append(character)

driver.get('https://maple.gg/job/paladin')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    paladin.append(character)

driver.get('https://maple.gg/job/pathfinder')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    pathfinder.append(character)

driver.get('https://maple.gg/job/phantom')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    phantom.append(character)

driver.get('https://maple.gg/job/flamewizard')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    flamewizard.append(character)

driver.get('https://maple.gg/job/hoyoung')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    hoyoung.append(character)

driver.get('https://maple.gg/job/hero')
for j in range(1, 15):
    character = {}
    ranking = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[2]/section/div/table/tbody/tr[' + str(j) + ']/td[1]').text
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
    character['world'] = world
    character['ratio'] = ratio
    character['recode'] = recode
    character['recodeTime'] = recodeTime
    character['seedRecode'] = seedRecode
    character['seedRecodeTime'] = seedRecodeTime
    hero.append(character)
data.append(nightlord)
data.append(nightwalker)
data.append(darkknight)
data.append(demonslayer)
data.append(demonavenger)
data.append(dualblader)
data.append(luminous)
data.append(mercedes)
data.append(mechanic)
data.append(mihile)
data.append(viper)
data.append(battlemage)
data.append(bowmaster)
data.append(blaster)
data.append(bishop)
data.append(shadower)
data.append(soulmaster)
data.append(striker)
data.append(marks)
data.append(adele)
data.append(aran)
data.append(ark)
data.append(arkmagefp)
data.append(arkmagetc)
data.append(evan)
data.append(angelicbuster)
data.append(wildhunter)
data.append(windbreaker)
data.append(shade)
data.append(illium)
data.append(xenon)
data.append(zero)
data.append(cadena)
data.append(kaiser)
data.append(cannonmaster)
data.append(captain)
data.append(kinesis)
data.append(paladin)
data.append(pathfinder)
data.append(phantom)
data.append(flamewizard)
data.append(hoyoung)
data.append(hero)
print(data)