import requests
from bs4 import BeautifulSoup
import csv



symbol = "ADBL"
content = requests.get('https://merolagani.com/CompanyDetail.aspx?symbol='+symbol).text

soup = BeautifulSoup(content,'lxml')

wrapper = soup.find('div',id="divHistory")
rows = wrapper.find('table').find_all('tr')[1:]
for row in rows:
    td = row.find_all('td')
    sno = td[0].text
    date = td[1].text
    ltp = td[2].text
    change = td[3].text
    high = td[4].text
    low = td[5].text
    open_price =td[6].text
    quantity = td[7].text
    turnover = td[8].text
    print(sno,date,ltp,change,high,low,open_price,quantity,turnover)

# for i in range(0,11):
#     page = wrapper.find('div',class_="pagging").div.input['value']
#     print(page)






