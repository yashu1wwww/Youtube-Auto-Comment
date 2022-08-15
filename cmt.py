import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'dotnknow@gmail.com\n'   #change to your mail id
password = 'pass1@#$\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

#upto the above the codes credits goes to https://github.com/xtekky these man

url = 'https://youtu.be/NbnsqGI0Yj4' #change to your required url
driver.get(url)
time.sleep(3) #if video contains ads means change 3 into 10 or 12

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

#time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")  #these line code copied from internet source to match the codes and run the program 


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer"))) #these line code copied from internet source to match the codes and run the program 

#the below codes was made my me

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("Amazing") #change cmt to your required 

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("wonderful")  #change cmt to your required 

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("awesome")  #change cmt to your required 

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

driver.close()

#i putted 3 cmts to post cmt automatically if you want more then copy line 54 to 64 and dont forgot to change cmt text if you want more cmts repeat these code paste again and again



    






            


