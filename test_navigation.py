import time
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\HP\\PycharmProjects\\pythonProject\\drivers\\chromedriver.exe")
Username= 'Admin'
Password= 'admin123'
driver.get('https://opensource-demo.orangehrmlive.com/')
print("driver.title")  #return the title of the page
print("driver.current_url")  #return url of the page
user_input = driver.find_element_by_id('txtUsername')
user_input.send_keys( Username )
password_input = driver.find_element_by_id('txtPassword')
password_input.send_keys(Password)
login_button = driver.find_element_by_id('btnLogin')
login_button.click()
driver.get('https://opensource-demo.orangehrmlive.com/index.php/dashboard')
print("driver.title")  #return the title of the page #FR
driver.get('https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave')
time.sleep(5)
print("driver.title")  #return the title of the page #TT
driver.back()
time.sleep(5)
print("driver.title")  #return the title of the page #FR
driver.forward()
time.sleep(5)
print("driver.title")  #return the title of the page #TT
time.sleep(5)
driver.close()

