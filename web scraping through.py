import requests
from bs4 import BeautifulSoup
import re

# *****getting table
r = requests.get('https://www.mastersportal.com/disciplines/24/computer-science-it.html')
soup = BeautifulSoup(r.text, 'lxml')
getTable = soup.find_all('table', {'id': 'RankingDisciplineTable'})

# *****regexing info
university = re.findall('href="(.*?)"', str(getTable[0].find_all('td', {'data-title': 'Universities'})))

location = re.findall('<span> (.*?) <\/span>', str(getTable[0].find_all('td', {'data-title': 'Location'})))

TimesHigherEducationRanking = re.findall('<span> (.*?) <\/span>', str(
    getTable[0].find_all('td', {'data-title': 'Times Higher Education Ranking (2018)'})))

ShanghaiJiaoTongUniversityRanking = re.findall('<span> (.*?) <\/span>', str(
    getTable[0].find_all('td', {'data-title': 'Shanghai Jiao Tong University Ranking (2017)'})))

TopUniversitiesRanking = re.findall('<span> (.*?) <\/span>',
                                    str(getTable[0].find_all('td', {'data-title': 'TopUniversities Ranking (2018)'})))

USNewsWorldReportRanking = re.findall('<span> (.*?) <\/span>', str(
    getTable[0].find_all('td', {'data-title': 'U.S. News & World Report Ranking (2018)'})))

# ***********printing out
print('university | ', 'location | ', 'TimesHigherEducationRanking | ', 'ShanghaiJiaoTongUniversityRanking | ',
      'TopUniversitiesRanking | ', 'USNewsWorldReportRanking')

for i in range(len(university)):
    print(university[i], ' | ', location[i], ' | ', TimesHigherEducationRanking[i], ' | ',
          ShanghaiJiaoTongUniversityRanking[i], ' | ', end='')
    print(TopUniversitiesRanking[i], ' | ', USNewsWorldReportRanking[i])
