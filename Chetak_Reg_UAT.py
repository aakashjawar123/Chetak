import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_Nav_to_Registration(setup):
    try:
        setup.get("https://uat-ecom.excellonconnect.com/?Brand=Chetak")
        wait = WebDriverWait(setup, 10)

        # Click the register button
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='REGISTER'])[1]"))).click()

        Expected_Url = "https://uat-ecom.excellonconnect.com/register"
        wait.until(EC.url_to_be(Expected_Url))
        assert setup.current_url == Expected_Url, f"Expected_Url: {Expected_Url}, but got: {setup.current_url}"

    except Exception as e:
        print(f"An Error Occured: {e}")


def test_Registration_Page(setup):
    try:
        setup.get("https://uat-ecom.excellonconnect.com/register")
        wait = WebDriverWait(setup, 10)

        wait.until(EC.element_to_be_clickable((By.NAME, "firstName"))).send_keys("Aakash")
        setup.find_element(By.NAME, "lastName").send_keys("Patil")
        setup.find_element(By.NAME, "MobileNo").send_keys("77658007014")
        setup.find_element(By.NAME, "emailId").send_keys("nitinm@excellonsoft.com")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']"))).click()
        setup.implicitly_wait(10)

        # Enter OTP
        otp_fields = [
            "(//input[@aria-label='Please enter OTP character 1'])[1]",
            "(//input[@aria-label='Please enter OTP character 2'])[1]",
            "(//input[@aria-label='Please enter OTP character 3'])[1]",
            "(//input[@aria-label='Please enter OTP character 4'])[1]",
            "(//input[@aria-label='Please enter OTP character 5'])[1]",
            "(//input[@aria-label='Please enter OTP character 6'])[1]"
        ]
        for xpath in otp_fields:
            setup.find_element(By.XPATH, xpath).send_keys("9")
        Otp_fiels2 = [
            "(//input[@aria-label='Please enter OTP character 1'])[2]",
            "(//input[@aria-label='Please enter OTP character 2'])[2]",
            "(//input[@aria-label='Please enter OTP character 3'])[2]",
            "(//input[@aria-label='Please enter OTP character 4'])[2]",
            "(//input[@aria-label='Please enter OTP character 5'])[2]",
            "(//input[@aria-label='Please enter OTP character 6'])[2]"
        ]
        for xpath in Otp_fiels2:
            setup.find_element(By.XPATH, xpath).send_keys("9")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Verify & Proceed']"))).click()

        toggle_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='true']")))
        is_selected = toggle_button.is_selected()

        if is_selected:
            toggle_button.click()
        assert toggle_button.is_selected()

        wait.until(EC.element_to_be_clickable((By.NAME, "newPassword"))).send_keys("Aakash@123")
        setup.find_element(By.NAME, "reEnterPassword").send_keys("Aakash@123")

        toggle_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='true']"))).click()
        #is_selected = toggle_button.is_selected()

        # if toggle_button.is_selected:
        #     toggle_button.click()
        # assert not toggle_button.is_selected()

        setup.find_element(By.XPATH, "//span[normalize-space()='Save & Register']").click()

        Expected_URL = "https://uat-ecom.excellonconnect.com/?Brand=Chetak"
        wait.until(EC.url_to_be(Expected_URL))
        assert setup.current_url == Expected_URL, f"Expected_URL: {Expected_URL}, But got: {setup.current_url}"

    except Exception as e:
        print(f"An error occurred: {e}")
