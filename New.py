import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Chetak_Booking():
    def test_payment(self):
        driver=webdriver.Chrome()
        driver.get("https://uat-ecom.excellonconnect.com/login")
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Login using Password'])[1]"))).click()
        driver.find_element(By.NAME, "mobileNo").send_keys("7391008538")
        driver.find_element(By.NAME, "password").send_keys("Aakash@123")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Login using Password'])[1]"))).click()
        wait.until(EC.url_to_be("https://uat-ecom.excellonconnect.com/?Brand=Chetak"))

        Expected_URL = "https://uat-ecom.excellonconnect.com/?Brand=Chetak"
        assert Expected_URL == driver.current_url, f"Expected_URL:{Expected_URL}, but got {driver.current_url}"
        wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[contains(@class,'MuiButton-label')][normalize-space()='BOOK VEHICLE'])[1]"))).click()

        wait.until(EC.url_to_be("https://uat-ecom.excellonconnect.com/products/00GL69D5/Chetak-Blue-2901-Cyber-White"))
        Expected_url = "https://uat-ecom.excellonconnect.com/products/00GL69D5/Chetak-Blue-2901-Cyber-White"
        wait.until(EC.url_to_be(Expected_url))
        assert Expected_url == driver.current_url, f"Expected_url:{Expected_url},but got:{driver.current_url}"

        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='demo-customized-select']"))).click()
        driver.find_element(By.XPATH,"//li[normalize-space()='Maharashtra']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//div[@id='demo-simple-select-filled'])[2]").click()
        driver.find_element(By.XPATH,"(//li[@role='option'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[@class='MuiButton-label']").click()

        wait.until(EC.url_to_be("https://uat-ecom.excellonconnect.com/products/00GL69D5/bookingreview/Chetak-Blue-2901-Cyber-White/Chetak-@-Wakdewadi/Maharashtra/Pune"))
        Expected_URL1="https://uat-ecom.excellonconnect.com/products/00GL69D5/bookingreview/Chetak-Blue-2901-Cyber-White/Chetak-@-Wakdewadi/Maharashtra/Pune"
        assert Expected_URL1==driver.current_url, f"Expected_URL1: {Expected_URL1}, but got: {driver.current_url}"

        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@value='true']").click()

        Chechbox_List= [
            "(// input[@ aria-label='primary checkbox'])[1]",
            "(// input[@ aria-label='primary checkbox'])[2]",
            "(// input[@ aria-label='primary checkbox'])[3]"
        ]
        for xpath in Chechbox_List:
            driver.find_element(By.XPATH,xpath).click()
        driver.find_element(By.XPATH,"//span[normalize-space()='CONFIRM AND MAKE PAYMENT']").click()
        time.sleep(5)
        driver.quit()

runpayment = Chetak_Booking()
runpayment.test_payment()