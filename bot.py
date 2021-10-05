import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(executable_path="_PATH_")  #enter the path of your selenium chrome driver
driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https%3A%2F%2Fmeet.google.com%2Flanding%3Fauthuser%3D1&followup=https%3A%2F%2Fmeet.google.com%2Flanding%3Fauthuser%3D1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
print(driver.title)
ele=driver.find_element_by_xpath("//*[@id='identifierId']")  # username
print(ele.is_displayed())
print(ele.is_enabled())
ele.send_keys(" email ") #enter email id
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
time.sleep(2)
pwd=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")  # password
print(pwd.is_displayed())
print(pwd.is_enabled())
pwd.send_keys(" password ") # enter password
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/c-wiz/c-wiz/div[1]/div[1]/div/div[5]/c-wiz/div/c-wiz[1]/div").click()
time.sleep(5)  # first class
dismiss=driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span")  # dismiss
if dismiss.is_displayed():
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span").click()
else:
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span").click()
action = ActionChains(driver)
action1=ActionChains(driver)
time.sleep(2)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("enter", do_press=True, do_release=True)
time.sleep(2)
time.sleep(2)
action.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
time.sleep(2)
action1.key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
time.sleep(5)
join=driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
i="True"
if join.is_displayed():
       driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
       time.sleep(2)
else:
        time.sleep(5)
time.sleep(30)
driver.close()
