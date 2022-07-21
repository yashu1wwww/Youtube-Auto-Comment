import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'vk18@gmail.com\n'   
password = 'vk18rat\n'          

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

url = 'https://youtu.be/OKBMCL-frPU'
driver.get(url)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
time.sleep(7)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element_by_css_selector("#contenteditable-root").send_keys("one of the best trailer ever seen")
time.sleep(3)
driver.find_element_by_css_selector("#contenteditable-root").send_keys("amazing one")
time.sleep(2)
driver.find_element_by_css_selector("#contenteditable-root").send_keys("great one")
time.sleep(2)
driver.find_element_by_css_selector("#contenteditable-root").send_keys("wonderful")
time.sleep(2)
driver.find_element_by_css_selector("#contenteditable-root").send_keys("fantastic")
time.sleep(2)
driver.find_element_by_css_selector("#button").click()
time.sleep(30)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
#driver.find_element_by_css_selector("#button").click()
#comment= driver.find_element_by_id("contenteditable-root")
#comment.send_keys("game")
#comment = driver.find_element_by_id("text").click()
#from selenium.common.exceptions import NoSuchElementException
#try:
    #user_name = driver.find_element_by_name("userName")
    #user_name.send_keys("mercury")
#except NoSuchElementException:
    #print("exception handled")
    
    #comment= driver.find_element_by_id("contenteditable-root")
#comment.send_keys("game")
#comment = driver.find_element_by_id("text").click()
    
    






            


