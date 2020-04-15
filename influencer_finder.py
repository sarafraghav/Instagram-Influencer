#IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time
import sys    
import os   

#VARIABLES
influen = []

tag = 'dogsarethefunniest'
account_username = 'rsprivacc'
account_password = 'Raghav@2004'
DEBUG = False

#CODE_SETUP
options = Options()
options.headless = False
if DEBUG:
  driver = webdriver.Firefox(executable_path='geckodriver.exe')
else:
  driver = webdriver.Firefox(firefox_options=options,  executable_path='geckodriver.exe')

#INITIATOR

driver.get('https://www.instagram.com/accounts/login/?next=%2F'+tag)
try:
 WebDriverWait(driver, 50).until( expect.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')))
 print('Login Page Loaded')
except:
  print("Page did not load. Try Again") 
  
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(account_username)
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(account_password)
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
try:
  WebDriverWait(driver, 30).until( expect.presence_of_element_located((By.CLASS_NAME, 'OfoBO ')))
  print("Hashtag Page loaded")
except :
  print("Page did not load. Maybe Wifi is too slow , for further information , try to replicate the error by turning debug = true.") 
        
#COMMENTER
def COMMENTER(elem):
    try: 
      influ = []
      global counter
      elem = driver.find_element_by_class_name('OfoBO').click()
      time.sleep(0.5)
      elem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div[1]/a').click() 
      elems = driver.find_elements_by_class_name('KV-D4')
      res = [elems[i] for i in range(len(elems)) if i % 2 != 0] 
      for elem in res:
        if elem.text not in influen and elem.text != "Verified":
          influen.append(elem.text)
        influ.append(elem.text)
      return influ
    except TimeoutException as ex:
      print("A post took too lost to load and hence skipped")
      solver = driver.find_element_by_class_name('wpO6b ').click()
    except NoSuchElementException:
      try:
       elem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div[1]/a').click() 
       elems = driver.find_elements_by_class_name('KV-D4')
       res = [elems[i] for i in range(len(elems)) if i % 2 != 0] 
       for elem in res:
        if elem.text not in influen and elem.text != "Verified":
          influen.append(elem.text)
        influ.append(elem.text)  
       return influ
      except NoSuchElementException:
        try:
         driver.refresh()
         time.sleep(2)
         elem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div[1]/a').click() 
         elems = driver.find_elements_by_class_name('KV-D4')
         res = [elems[i] for i in range(len(elems)) if i % 2 != 0] 
         for elem in res:
          if elem.text not in influen and elem.text != "Verified":
           influen.append(elem.text)
          influ.append(elem.text)  
         return influ
        except NoSuchElementException:
          print("Error") 
    except IndexError:
      print("Page did not load properly , reloading.")

while True:
    inf = COMMENTER(elem)
    for x in inf:
      driver.get('https://www.instagram.com/accounts/login/?next=%2F'+x)
      infl = COMMENTER(elem)
      
    with open('influencers.txt','w') as influencers:  
     for el in influen:
      influencers.write(el + '\n')

    driver.get('https://www.instagram.com/accounts/login/?next=%2F'+inf[-1])
