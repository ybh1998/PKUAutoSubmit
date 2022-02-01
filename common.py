import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 60

def wait_for_loading(driver):
    while True:
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'el-loading-mask')
                )
            )
            print('Waiting for "loading" to disappear')
            time.sleep(1)
        except:
            break


def wait_for_animation(driver):
    while True:
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    'div[class$="-enter-active"], div[class*="-enter-active "] '
                    'div[class$="-leave-active"], div[class*="-leave-active "]'
                ))
            )
            print('Waiting for animation to finish')
            time.sleep(1)
        except:
            break


def input_select(driver, tag_for, text):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'label[for="' + tag_for + '"]')
        )
    ).find_element(By.XPATH, '..')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.find_element(By.TAG_NAME, 'input').click()
    wait_for_animation(driver)
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH,
        '//div[@class="el-select-dropdown el-popper" and '
        'not(contains(@style, "display: none"))]'))
    )
    element = WebDriverWait(element, timeout).until(
        EC.presence_of_element_located(
            (By.XPATH, './/li/span[normalize-space(text())="' + text + '"]')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    wait_for_animation(driver)


def input_text(driver, tag_for, tag_name, text):
    input_element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'label[for="' + tag_for + '"]')
        )
    ).find_element(By.XPATH, '..').find_element(By.TAG_NAME, tag_name)
    driver.execute_script("arguments[0].scrollIntoView();", input_element)
    input_element.click()
    wait_for_animation(driver)
    input_element.clear()
    wait_for_animation(driver)
    curr_text = ''
    for curr_char in text:
        curr_text = curr_text + curr_char
        while input_element.get_attribute('value') != curr_text:
            input_element.send_keys(curr_char)
            time.sleep(0.1)
    wait_for_animation(driver)


def input_select_radio(driver, tag_for, text):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'label[for="' + tag_for + '"]')
        )
    ).find_element(By.XPATH, '..')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    wait_for_animation(driver)
    WebDriverWait(element, timeout).until(
        EC.element_to_be_clickable(
            (By.XPATH, './/span[normalize-space(text()) = "' + text + '"]')
        )
    ).click()
    wait_for_animation(driver)


def loginPortal(driver):
    driver.get('''https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appNam
e=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97
%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https%3A%2F%2Fportal.pku.edu.cn%2Fpor
tal2017%2FssoLogin.do''')
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'user_name'))
    ).send_keys(os.environ['USERNAME'])
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'password'))
    ).send_keys(os.environ['PASSWORD'])
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, 'logon_button'))
    ).click()
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'stuCampusExEnReq'))
    )
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'fav_epidemic'))
    )
    print('Login Successful!')


def getWebDriver():
    print('Another PKUAutoSubmit by ybh1998, use at your own risk!')
    headless = os.getenv("HEADLESS", 'False').lower() in ('true', '1', 't')
    if os.environ['DRIVER'].lower() == 'firefox':
        options = webdriver.firefox.options.Options()
        options.headless = headless
        driver = webdriver.Firefox(options=options)
    elif os.environ['DRIVER'].lower() == 'chrome':
        options = webdriver.chrome.options.Options()
        options.headless = headless
        driver = webdriver.Chrome(options=options)
    else:
        print('Unknown driver:', os.environ['DRIVER'])
        sys.exit(os.EX_SOFTWARE)
    return driver
