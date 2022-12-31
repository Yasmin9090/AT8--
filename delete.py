from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Logging in By using user name and Password

class name1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)
        

        #TC1

        #username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

        #password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(6)

        #login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(5)
#TC :5

        #Get inside to the PIM tab
        PIM_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM = driver.find_element(By.XPATH, PIM_xpath).click()
        time.sleep(4)

        # Below xpath to click the account
        Deleteacc_xpath='//button[@class="oxd-icon-button oxd-table-cell-action-space"]'
        Delete=driver.find_element(By.XPATH,Deleteacc_xpath).click()
        time.sleep(4)

        # Below xpath to delete account
        accdel_xpath=driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()
        time.sleep(5)

        print("Account Details has been Successfully Deleted")

a=name1()
a.name_password()
