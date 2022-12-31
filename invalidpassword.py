from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Test case2 Invalid Password

class name1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)
#Tc: 2

#username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

#password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin100")
        time.sleep(4)

#login button
        login_xpath = '//button[@type="submit"]'
        submit = driver.find_element(By.XPATH, login_xpath).click()
        time.sleep(10)

#password error
        error_xpath="//div[@class='oxd-alert oxd-alert--error']"
        error=driver.find_element(By.XPATH,error_xpath)
        print(error.text)


a=name1()
a.name_password()
