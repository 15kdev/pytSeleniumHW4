from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class odev_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        print(errorMessage)
        sleep(2)
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu {testResult}")
        sleep(4)
    def test_invalid_login2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput2 = driver.find_element(By.ID, "user-name")
        passwordInput2 = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput2.send_keys("locked_out_user")
        passwordInput2.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage2 = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        print(errorMessage2)
        sleep(2)
        testResult2 = errorMessage2.text == "Epic sadface: Sorry, this user has been locked out."

        print(f"Test Sonucu {testResult2}")
        sleep(4)
    def test_invalid_login3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput3 = driver.find_element(By.ID, "user-name")
        passwordInput3 = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput3.send_keys("")
        passwordInput3.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(3)
        errorMessage4 = driver.find_element(By.CSS_SELECTOR,'#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path')
        errorMessage4.click()
        sleep(5)
    def test_invalid_login4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput4 = driver.find_element(By.ID, "user-name")
        passwordInput4 = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput4.send_keys("standard_user")
        passwordInput4.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        toplamUrun = driver.find_elements(By.CLASS_NAME, "inventory_item") 
        print(f"Toplam Ürün Sayısı : {len(toplamUrun)}'dır.")

        sleep(100)



testClass = odev_Sauce()

testClass.test_invalid_login()
testClass.test_invalid_login2()
testClass.test_invalid_login3()
testClass.test_invalid_login4()