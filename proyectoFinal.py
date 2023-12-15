from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
waitScreen= 2

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Funcion para maximizar la pantalla y esperar 5 segundos
driver.maximize_window()
time.sleep(waitScreen)

#Login en el sistema
userID= driver.find_element(By.XPATH, "//input[contains(@name,'username')]").send_keys("Admin")
userPass= driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
userLogin= driver.find_element(By.XPATH, "//button[@type='submit']").click()


#Crear usuario y rol
adminPanel= driver.find_element(By.XPATH, "//a[contains(.,'Admin')]").click()
addUser= driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
time.sleep(4)
#Formulario de creacion de usuarios
userRole= driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]").click()
adminRole= driver.find_element(By.XPATH, "//div[@role='option'][contains(.,'Admin')]").click()
time.sleep(2)
userStatus= driver.find_element(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active'][contains(.,'-- Select --')]").click()
enabledStatus= driver.find_element(By.XPATH, "//div[@role='option'][contains(.,'Enabled')]").click()
#employed= driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
#userName= driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
#password= driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()

time.sleep(60)
driver.close()