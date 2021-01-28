import re
from bs4 import BeautifulSoup
import requests
# from gt import links
import csv

# url = 'https://www.sanfoundry.com/'
# p = requests.get(url)
# s = BeautifulSoup(p.text, 'html.parser') 
# table = s.find('div',{'class':'grid-33 tablet-grid-33 mobile-grid-100 second-column'})
# for l in table.find_all('ul')[0:1]:
#     d = {m.find('a').text:m.find('a')['href'] for m in l.find_all('li') if 'MCQ' in m.find('a').text}
d = {'1000 Wireless & Mobile MCQs': 'https://www.sanfoundry.com/1000-wireless-mobile-communications-questions-answers/', '1000 VHDL MCQs': 'https://www.sanfoundry.com/1000-vhdl-questions-answers/', '1000 MATLAB MCQs': 'https://www.sanfoundry.com/1000-matlab-questions-answers/', '1000 Mechatronics MCQs': 'https://www.sanfoundry.com/1000-mechatronics-questions-answers/', '1000 Renewable Energy MCQs': 'https://www.sanfoundry.com/1000-renewable-energy-questions-answers/', '1000 Antennas MCQs': 'https://www.sanfoundry.com/1000-antennas-questions-answers/', '1000 Cognitive Radio MCQs': 'https://www.sanfoundry.com/1000-cognitive-radio-questions-answers/', '1000 Total Quality Management MCQs': 'https://www.sanfoundry.com/1000-total-quality-management-questions-answers/', '1000 Arduino MCQs': 'https://www.sanfoundry.com/1000-arduino-questions-answers/'}
for  topicTitle, topicLink in d.items():
    print(topicTitle)
    p = requests.get(topicLink)
    s = BeautifulSoup(p.text, 'html.parser') 
    try:
        aLink = s.find('div',{'class':'entry-content'})
        links = {bLink.text:bLink['href'] for bLink in aLink.find_all('a')}
        for a,b in links.items():
            print(f'{topicTitle}::{a}')
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
                    # print(expl)
                    with open(f'csv/{topicTitle}.csv', 'a', encoding='utf-8') as csvfile:
                        # print([que, choices, ans, expl, a, b])
                        writer = csv.writer(csvfile)
                        writer.writerow([que, choices, ans, expl, a, b])
                except AttributeError: continue
                except IndexError: continue
    except KeyError: continue