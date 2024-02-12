#!/usr/bin/env python
# coding: utf-8

# # Amazon Web Scraper

# In[ ]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd


# In[ ]:


def check_amount():
    url='https://www.amazon.in/gp/aw/d/B0CKJ5ZXFK/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=ba07619d5efcc22773d2438719ccfd74&hsa_cr_id=0&qid=1707374044&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_mcd_asin_0_img&pd_rd_w=3fwqa&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_p=df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_r=1684BRD1VDA9HJW4DBWP&pd_rd_wg=3FvES&pd_rd_r=1ba85e15-c818-43f5-ad1d-99eaa4198d28'
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page=requests.get(url,headers=headers)
    s1=BeautifulSoup(page.content,"html.parser")
    s2=BeautifulSoup(s1.prettify(),"html.parser")
    title = s2.find(id='productTitle').get_text()
    amount = s2.find(id='color_name_1_price').get_text()
    title=title.strip()
    amount=amount.strip()[1:]
#     print(title)
#     print(amount)
    today=datetime.date.today()
    h1=['Title','Price','Date']
    data=[title,amount,today]
    with open('Amazon_Web_ScraperDataset.csv','w',newline='',encoding='UTF8') as f:
        writer=csv.writer(f)
        writer.writerow(h1)
        writer.writerow(data)
    df=pd.read_csv(r'C:/Users/nsure/Internship/Amazon Web Scrapping/Amazon_Web_ScraperDataset.csv')
    print(df)
    with open('Amazon_Web_ScraperDataset.csv','a+',newline='',encoding='UTF8')as f:
        writer=csv.writer(f)
        writer.writerow(data)



# In[ ]:


while(True):
    check_amount()
    time.sleep(86400)
df=pd.read_csv(r'C:/Users/nsure/Internship/Amazon Web Scrapping/Amazon_Web_ScraperDataset.csv')
print(df)


# In[ ]:




