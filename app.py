from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time


def sign_in_gmail():
    """
    Login into gmail via stackoverflow
    :return: None
    """
    print("Logging in into Gmail account...")
    url = "https://stackoverflow.com/users/login"
    driver.get(url)
    try:
        login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "s-btn__google")))
        time.sleep(2)
        login_btn.click()
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
        time.sleep(2)
        email_input.send_keys("1941012410.c.subhransudash")
        email_input.send_keys(Keys.ENTER)
        pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        time.sleep(2)
        pass_input.send_keys("skywalker69")
        pass_input.send_keys(Keys.ENTER)
        print("Logged in into Gmail account")
    except Exception as e:
        print(e)


def navigate_to_meeting_link(link):
    driver.get(link)


def mute_mic_and_cam():
    print("Muting mic and camera...")
    try:
        # close popup
        dismiss = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")))
        dismiss.click()
        # dismiss alert
        alert = Alert(driver)
        alert.dismiss()
        # mute mic
        mic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div["
                       "1]/div/div[4]/div[1]/div/div/div")))
        mic.click()
        print("Muted mic and camera")
    except Exception as e:
        print(e)


def join_meeting():
    print("Joining meeting...")
    try:
        join_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  "/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")))
        join_now.click()
    except Exception as e:
        print(e)


def leave_meeting():
    print("Leaving meeting...")
    pass


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    URL = "https://meet.google.com/yfq-cwor-hqc"

    sign_in_gmail()
    time.sleep(2)

    navigate_to_meeting_link(URL)
    time.sleep(5)

    mute_mic_and_cam()
    time.sleep(5)

    join_meeting()

    time.sleep(1000)

    driver.close()

    print("Test completed")
