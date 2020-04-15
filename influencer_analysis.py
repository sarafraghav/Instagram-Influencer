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

influencer = open('influencers.txt','r').readlines()
influencers = {}
final = open('Influencer_engagement.csv','w')
repl_dict = {'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9', }
DEBUG = True

def price(follower):
  if follower<50000:
    return 15
  elif follower<150000:
    return 25
  elif follower<300000:
    return 45
  elif follower<500000:
    return 70
  else:
    return 1000        




#CODE_SETUP
options = Options()
options.headless = True
if DEBUG:
  driver = webdriver.Firefox(executable_path='geckodriver.exe')
else:
  driver = webdriver.Firefox(firefox_options=options,  executable_path='geckodriver.exe')

#INITIATOR
driver.get('https://kicksta.co/instagram-engagement-calculator')
try:
 WebDriverWait(driver, 50).until( expect.presence_of_element_located((By.XPATH, '//*[@id="inlineFormInputGroup"]')))  
 elem = driver.find_element_by_xpath('//*[@id="inlineFormInputGroup"]').send_keys('saraf.raghav')  
 elem = driver.find_element_by_xpath('//*[@id="calculateBtn"]').click() 
 elem = driver.find_element_by_xpath(' //*[@id="calculatorOptin"]').send_keys('sraghav@tisb.ac.in')  
 elem = driver.find_element_by_xpath('//*[@id="emailBtn"]').click() 
 print('Initialised Succesfully')
 driver.get('https://kicksta.co/instagram-engagement-calculator')
except:
  print("Initiaising Failed") 
final.write('Username , Engagement , Followers , Reach , Price Per User \n')  
for user in influencer: 
  try:
   elem = driver.find_element_by_xpath('//*[@id="inlineFormInputGroup"]').send_keys(user)  
   elem = driver.find_element_by_xpath('//*[@id="calculateBtn"]').click()
   WebDriverWait(driver, 50).until( expect.presence_of_element_located((By.XPATH, '//*[@id="instagramEngagementRate"]')))
   time.sleep(2.5)
   engagement = float(driver.find_element_by_xpath('//*[@id="instagramEngagementRate"]').text[0:4])/100
   followers = int(driver.find_element_by_xpath('//*[@id="instagramFollowers"]').text.replace('K','000').replace('M','000000'))
   influencers[user.strip()] = [engagement,followers]
   pric = price(followers)
   reach = followers*engagement
   price_per_user = pric / reach
   print(('{} : {}  : {} : {} : {}').format(user.strip(),str(engagement) , str(followers) , str(reach) , str(price_per_user)))
   final.write(('{} , {}  , {} , {} , {} \n').format(user.strip(),str(engagement) ,str(followers) , str(reach) , str(price_per_user)))
   driver.get('https://kicksta.co/instagram-engagement-calculator')
  except:
    print('Skipped')
    driver.get('https://kicksta.co/instagram-engagement-calculator')
    continue

        
