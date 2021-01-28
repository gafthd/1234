import re
from bs4 import BeautifulSoup
import requests
from gt import links
import csv

for a,b in links.items():
    page = requests.get(b)
    soup = BeautifulSoup(page.text, 'html.parser')
    i = soup.find('div',{'class':'entry-content'})
    for x in i.find_all('p'):
        if re.search('<p>\d.*?</div>', str(x)) is not None:
            y = str(x).replace('\n','')
            question = re.search('^<p>\d.*?</div>', str(y)).group()
            print(question)
            
            print('\n\n')
            question = re.search('^<p>\d.*?<br/>a[)]',question).group()[3:-10]
            choices = re.search('<br/>a[)].*?<br/><span',question).group()[5:-10].split('<br/>')
            ans = re.search('Answer: \w+',question).group()
            expl = re.search('Explanation: .*',question).group()[:-6]
            # print(question)
            # print(choices)
            # print(ans)
            # print(expl)
            # with open('try.csv', 'w', encoding='utf-8') as csvfile:
            #     print([que, choices, ans, expl, a])
            #     writer = csv.writer(csvfile, delimiter=',')
            #     writer.writerow([que, choices, ans, expl, a])
    #     except AttributeError: continue
        else:
            print('no mas')
    
    break
