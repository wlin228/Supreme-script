import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

checkoutDelay = 5000
monitorDelay = 2000;

buyerName = 'Supreme Buyer'
buyerMail = 'myadfg@nospace.com'
buyerTele = '1234567890'
buyerAdress = 'Area 31'
buyerCity = 'London'
buyerZIP = 'XXXXXX'
buyerCountry = 'CANADA'
buyerCardType = 'Mastercard'
buyerCardNumber = '1111 1111 1111 1111'
buyerCardExpMonth = '01'
buyerCardExpYear = '2024'
buyerCardCvv = '169'


excutable_path = r'chromedriver.exe'
driver = webdriver.Chrome(excutable_path)
driver.get('https://www.supremenewyork.com/shop/all/sweatshirts')
driver.find_element_by_class_name()

while True:
    try:
        driver.find_element_by_partial_link_text('Thermal Zip')
        break
    except NoSuchElementException:
        time.sleep(monitorDelay / 1000)
        driver.refresh()

print("Product Found!")
driver.find_element_by_partial_link_text('Thermal Zip').click()
wait = WebDriverWait(driver, 10)
something = wait.until(EC.presence_of_element_located((By.ID, 's')))
wait.until(EC.presence_of_element_located((By.CLASS_NAME,'public-DraftStyleDefault-block public-DraftStyleDefault-ltr')))
Select(driver.find_element_by_id('s')).select_by_visible_text('Medium')
driver.find_element_by_name('commit').click()
print("added!")

time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

print('Filling contact information')
ord_billing_name = driver.find_element_by_id('order_billing_name')

ord_billing_name.send_keys(buyerName)
ord_email = driver.find_element_by_id('order_email')
ord_email.send_keys(buyerMail)
ord_tele = driver.find_element_by_id('order_tel')
ord_tele.send_keys(buyerTele)
ord_adress = driver.find_element_by_id('bo')
ord_adress.send_keys(buyerAdress)
ord_billing_city = driver.find_element_by_id('order_billing_city')
ord_billing_city.send_keys(buyerCity)
ord_zip = driver.find_element_by_id('order_billing_zip')
ord_zip.send_keys(buyerZIP)
Select(driver.find_element_by_id('order_billing_country')).select_by_visible_text(buyerCountry)
Select(driver.find_element_by_id('order_billing_state')).select_by_visible_text('ON')
ord_cnb = driver.find_element_by_id("rnsnckrn")
ord_cnb.send_keys(buyerCardNumber)
Select(driver.find_element_by_id('credit_card_month')).select_by_visible_text(buyerCardExpMonth)
Select(driver.find_element_by_id('credit_card_year')).select_by_visible_text(buyerCardExpYear)
ord_cnb = driver.find_element_by_id("orcer")
ord_cnb.send_keys(buyerCardCvv)
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
print("Checking out delay")
time.sleep(5)
driver.find_element_by_name('commit').click()
print("Please solve the Recaptcha!")
