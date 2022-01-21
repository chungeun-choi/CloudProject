from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import string
import pandas as pd




def crollingData(test):

    driver = webdriver.Chrome('/Users/cucuridas/Downloads/chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://www.ncloud.com/guideCenter/glossary?t="+test+"&q=")
    print('연결됬다아앙',test)

    data = {'Eng':[],'Dis':[]}
    df = pd.DataFrame(data=data)

    for count in range(999):
        
        time.sleep(10)
        
        selector_test = driver.find_elements_by_css_selector("li.step")
        
        for STe in selector_test:
            cal1 = STe.find_element_by_css_selector("h4")
            cal2 = STe.find_element_by_css_selector("p")
            data_set = {'Eng':cal1.text,'Dis':cal2.text}
            #print(cal1.text,cal2.text)
            
            df= df.append(data_set, ignore_index=True)
        
        
        

        try: 
            number = str(count + 4)
        
            button = driver.find_element_by_css_selector("#app > article > div.center-wrap > div > div > a:nth-child("+number+")")
            button.click()
        except: 
            print("데이터 수집 완료.")
            print(df)
            df.to_csv("C:\\test\\test"+test+'Data.csv',engin='python',)
            break



Alpha = string.ascii_uppercase    

for num in range (len(Alpha)-1):
    crollingData(Alpha[num])


