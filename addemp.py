from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Test case : 3 (PIM)

class name1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        #Tc: 3

        #username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

        #password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(4)

        #login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

        #PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

        #ADD
        ADD_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD=driver.find_element(By.XPATH,ADD_xpath).click()
        time.sleep(4)

        #First name
        FIRSTNAME_xpath='//input[@placeholder="First Name"]'
        FIRSTNAME=driver.find_element(By.XPATH,FIRSTNAME_xpath).send_keys("Aisha")
        time.sleep(4)

        #Last name
        LASTNAME_xpath='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,LASTNAME_xpath).send_keys("zahra")
        time.sleep(4)

        #Save
        Save_xpath='//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        Save=driver.find_element(By.XPATH,Save_xpath).click()
        time.sleep(5)

        #other id
        OtherID_xpath='//label[text()="Other Id"]/following::div[1]/input'
        OtherID=driver.find_element(By.XPATH,OtherID_xpath).send_keys("12345")
        time.sleep(4)

        #xpath for DL
        DL_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        DL=driver.find_element(By.XPATH,DL_xpath).send_keys("89990")
        time.sleep(4)

        #DL date
        DL_date_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        date=driver.find_element(By.XPATH,DL_date_xpath).send_keys("2024-04-20")
        time.sleep(5)

        #SSN number
        SSN_xpath='//label[text()="SSN Number"]/following::div[1]/input'
        SSN=driver.find_element(By.XPATH,SSN_xpath).send_keys("01234")
        time.sleep(5)

        #SIN number
        SIN_xpath='//label[text()="SIN Number"]/following::div[1]/input'
        SIN=driver.find_element(By.XPATH, SIN_xpath).send_keys("5678")
        time.sleep(5)

        #Nationality
        Nationality_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        Nationality=driver.find_element(By.XPATH,Nationality_xpath).send_keys("Indian")
        time.sleep(5)

        #Marital status
        Marital_xpath='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        Marital=driver.find_element(By.XPATH,Marital_xpath).send_keys("Married")
        time.sleep(5)

        #DOB
        DOB_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        DOB=driver.find_element(By.XPATH,DOB_xpath).send_keys("1991-04-20")
        time.sleep(5)

        #Gender
        Gender_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        Gender=driver.find_element(By.XPATH,Gender_xpath).click()
        time.sleep(5)

        #Militaryservice
        Military_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
        MilitaryService=driver.find_element(By.XPATH,Military_xpath).send_keys("Yes")
        time.sleep(5)

        #Smoker
        Smoker_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label'
        Smoker=driver.find_element(By.XPATH,Smoker_xpath).click()
        time.sleep(5)

        #save
        Save_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
        Save=driver.find_element(By.XPATH,Save_xpath).click()
        time.sleep(5)
        print("Employee details has been saved successfully")
a=name1()
a.name_password()
