from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import string
import pandas as pd
import openpyxl

    

def crollingData(turl,test,category,subcateogory):

    op = webdriver.ChromeOptions()
    op.add_argument("headless")
    op.add_argument("no-sandbox")
    op.add_argument('--disable-dev-shm-usage')
    url = turl+str(test)
    driver = webdriver.Chrome('/Users/cucuridas/Downloads/chromedriver')
    driver.implicitly_wait(10)
    driver.get(url)
    
    print('연결됬다아앙',test)

    category = category
    subcateogory = subcateogory

    data = {'category':[],
            'subCategory':[],
            'Question':[],
            'Answer':[]}

    df = pd.DataFrame(data=data)
    time.sleep(5)


    #Depth2 항목 선택 
    for i in range(1,11):
        try:
            button2 = driver.find_element_by_css_selector('#app > article > div:nth-child(7) > div > section > div:nth-child(1) > div:nth-child('+str(i)+') > a')
            button2.click()
            time.sleep(5)
        
            #내용 크롤링
            q = driver.find_element_by_class_name('search_title').text
            a = driver.find_element_by_class_name('tui-editor-contents').text
            print(q+"\n"+a)

            data_set = {'category':category,'subCategory':subcateogory,'Question':q,'Answer':a}

            df= df.append(data_set, ignore_index=True)

            #목록으로 들아가기
            button3 = driver.find_element_by_css_selector('#app > article > div.center-wrap > div > section > div.type-1.mt-20 > a')
            button3.click()
    

        except:
            break;    
    df.to_excel("/Users/cucuridas/Desktop/Ncloud/test"+subcateogory+str(test)+".xlsx",index=False,engine='openpyxl')


ca = ['MIG']



turl = 'https://www.ncloud.com/support/faq/trbl?page='

for i in range(1,2):
    crollingData(turl,i,'장애','장애')