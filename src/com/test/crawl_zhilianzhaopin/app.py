
import requests
from bs4 import BeautifulSoup
import sys


def write_to_html(text):
    with open("E:/project_sync_repository/learn_spider/src/com/test/crawl_zhilianzhaopin/1.html", "wb") as fileObj:
        fileObj.write(text)


url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&sm=0&p=1'
r = requests.get(url)
html = r.text.replace(u'\xa9', u'').replace(u'\xa0', u'')
soup = BeautifulSoup(html, 'html.parser')

tableList = soup.select('#newlist_list_content_table .newlist')[1:]
print(tableList[0])
for table in tableList:
    position = table.a.text
    company = table.select('.gsmc')[0].a.text
    spans = table.li.find_all('span')
    address = spans[0].text.split("：")[1]
    experience = spans[3].text.split("：")[1]
    salary = spans[-1].text.split("：")[1]
    print(position+"\t"+company+"\t"+address+"\t"+experience+"\t"+salary)