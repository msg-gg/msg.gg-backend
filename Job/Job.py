# import json
# with open("groups.json") as groups:
# 	groups_json = json.load(groups)
#
# 	print(groups_json["group1"])


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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		nightlord.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		nightwalker.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		darkknight.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		demonslayer.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		demonavenger.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		dualblader.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		luminous.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		mercedes.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		mechanic.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		mihile.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		viper.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		battlemage.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		bowmaster.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		blaster.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		bishop.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		shadower.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		soulmaster.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		striker.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		marks.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		adele.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		aran.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		ark.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		arkmagefp.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		arkmagetc.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		evan.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		angelicbuster.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		wildhunter.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		windbreaker.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		shade.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		illium.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		xenon.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		zero.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		cadena.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		kaiser.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		cannonmaster.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		captain.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		kinesis.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		paladin.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		pathfinder.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		phantom.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		flamewizard.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		hoyoung.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
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
	dete = driver.find_element_by_xpath(
		'//*[@id="app"]/div[2]/div[4]/div[1]/div/div[' + str(j) + ']/section/div/div[3]/span').text
	if j != 3:
		top['title'] = title
		top['topRecode'] = topRecode
		top['topTime'] = topTime
		top['nameLevel'] = nameLevel
		top['ranking'] = ranking
		top['dete'] = dete
		hero.append(top)
	else:
		top['title'] = title
		top['ranking'] = topRecode
		top['jobCount'] = topTime
		top['people'] = nameLevel
		top['ratio'] = ranking
		top['dete'] = dete
		hero.append(top)

data['nightlord'] = nightlord
data['nightwalker'] = nightwalker
data['darkknight']=darkknight
data['demonslayer']=demonslayer
data['demonavenger']=demonavenger
data['dualblader']=dualblader
data['luminous']=luminous
data['mercedes']=mercedes
data['mechanic']=mechanic
data['mihile']=mihile
data['viper']=viper
data['battlemage']=battlemage
data['bowmaster']=bowmaster
data['blaster']=blaster
data['bishop']=bishop
data['shadower']=shadower
data['soulmaster']=soulmaster
data['striker']=striker
data['marks']=marks
data['adele']=adele
data['aran']=aran
data['ark']=ark
data['arkmagefp']=arkmagefp
data['arkmagetc']=arkmagetc
data['evan']=evan
data['angelicbuster']=angelicbuster
data['wildhunter']=wildhunter
data['windbreaker']=windbreaker
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
data['flamewizard']=flamewizard
data['hoyoung']=hoyoung
data['hero']=hero

with open('Job.json', 'w', encoding="utf-8") as make_file:
	json.dump(data, make_file, ensure_ascii=False, indent="\t")