from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class sauce_tests:
    def emptyLogin(self):
     driver = webdriver.Chrome(ChromeDriverManager().install())
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     loginBtn = driver.find_element(By.ID,"login-button")
     sleep(2)
     loginBtn.click()
     errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
     testResult = errorMessage.text == "Epic sadface: Username is required"
     print(f"TEST SONUCU :{testResult}")
     sleep(5)
    def emptyPassword(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.maximize_window()
       driver.get("https://www.saucedemo.com/")
       userName = driver.find_element(By.ID,"user-name")
       userName.send_keys("Mrxa")
       sleep(2)
       
       loginBtn = driver.find_element(By.ID,"login-button")
       sleep(2)
       loginBtn.click()
       errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       testResult = errorMessage.text == "Epic sadface: Password is required"
       print(f"TEST SONUCU :{testResult}")
       sleep(5)
    def locked_user(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.maximize_window()
       driver.get("https://www.saucedemo.com/")
       userName = driver.find_element(By.ID,"user-name")
       userName.send_keys("locked_out_user")
       password = driver.find_element(By.ID,"password")
       password.send_keys("secret_sauce")
       loginBtn = driver.find_element(By.ID,"login-button")
       sleep(3)
       loginBtn.click()
       errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
       print(f"TEST SONUCU: {testResult}")
       sleep(10)
    def errorMessage_close(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.maximize_window()
       driver.get("https://www.saucedemo.com/")
       sleep(2)
       loginBtn = driver.find_element(By.ID,"login-button")
       sleep(3)
       loginBtn.click()
       sleep(3)
       closeButton = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
       sleep(2)
       closeButton.click()
       print("Hata mesajı kapatma butonuna tıklandı")
       sleep(10)
    def standard_user(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.maximize_window()
       driver.get("https://www.saucedemo.com/")
       userName = driver.find_element(By.ID,"user-name")
       userName.send_keys("standard_user")
       password = driver.find_element(By.ID,"password")
       password.send_keys("secret_sauce")
       loginBtn = driver.find_element(By.ID,"login-button")
       sleep(3)
       loginBtn.click()
       sleep(2)
       listOfItems = driver.find_elements(By.CLASS_NAME,"inventory_item")
       print(f"Sitede {len(listOfItems)} Adet ürün var.")
       sleep(10)
       
    


testClass=sauce_tests()
testClass.emptyLogin()
testClass.emptyPassword()
testClass.locked_user()
testClass.errorMessage_close()
testClass.standard_user()