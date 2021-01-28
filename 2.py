# meow
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
        try:
            y = str(x).replace('\n','')
            question = re.search('^<p>\d.*?</div>', str(y)).group()
            # print(question)
            que = re.search('^<p>\d.*?<br/>a[)]',question).group()[3:-7]
            l = re.search('<br/>a[)].*?<br/><span',question).group()[5:-10].split('<br/>')
            choices = '<div class = "choices">'+'</div><div class = "choices">'.join(l)+'</div>'
            m = re.search('Answer: \w+',question).group()[-1]
            # print(l)
            if m == 'a': ans = l[0]
            elif m == 'b': ans = l[1]
            elif m == 'c': ans = l[2]
            elif m == 'd': ans = l[3]
            elif m == 'e': ans = l[4]
            expl = re.search('Explanation: .*',question).group()[:-6]
            # print(que)
            # print(len(choices))
            # print(ans)
            print(expl)
            with open('try.csv', 'a', encoding='utf-8') as csvfile:
                print([que, choices, ans, expl, a])
                writer = csv.writer(csvfile)
                writer.writerow([que, choices, ans, expl, a])
        except AttributeError: continue
    break
