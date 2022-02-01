import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import *


def goto_ssop(driver):
    driver.get('''https://portal.pku.edu.cn/portal2017/util/appSysRedir.do?appId
=epidemic''')
    wait_for_loading(driver)
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(
            (By.ID, 'tab-daily_info_tab')
        )
    ).click()
    wait_for_loading(driver)


def submit(driver):
    name = (b'\xe4\xbf\x9d\xe5\xad\x98\xe4\xbb\x8a\xe6\x97\xa5\xe4\xbf\xa1\xe6'
        b'\x81\xaf').decode('UTF-8')
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button/span[normalize-space(text())="' + name + '"]')
        )
    ).click()
    name = (b'\xe5\xa1\xab\xe6\x8a\xa5\xe6\x8f\x90\xe7\xa4\xba\xef\xbc\x9a\xe4'
        b'\xbb\x8a\xe6\x97\xa5\xe5\xb7\xb2\xe5\xa1\xab\xe6\x8a\xa5\xe3\x80\x82'
    ).decode('UTF-8')
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.XPATH, '//span[contains(text(), "' + name + '")]')
        )
    )
    print('Submit successfully')


def run(driver):
    loginPortal(driver)
    goto_ssop(driver)
    input_select_radio(driver, 'sfhx', os.environ['SFHX'])
    input_select(driver, 'dqszdsm', os.environ['DQSZDSM'])
    input_select(driver, 'dqszddjsm', os.environ['DQSZDDJSM'])
    input_select(driver, 'dqszdxjsm', os.environ['DQSZDXJSM'])
    input_text(driver, 'dqszdxxdz', 'textarea', os.environ['DQSZDXXDZ'])
    input_select_radio(driver, 'sfmjqzbl', os.environ['SFMJQZBL'])
    input_select_radio(driver, 'sfmjmjz', os.environ['SFMJMJZ'])
    input_select_radio(driver, 'sfzgfxdq', os.environ['SFZGFXDQ'])
    input_text(driver, 'jrtw', 'input', os.environ['JRTW'])
    input_select_radio(driver, 'sfczzz', os.environ['SFCZZZ'])
    input_select(driver, 'yqzd', os.environ['YQZD'])
    input_text(driver, 'jqxdgj', 'textarea', os.environ['JQXDGJ'])
    input_text(driver, 'qtqksm', 'textarea', os.environ['QTQKSM'])
    wait_for_animation(driver)
    submit(driver)


if __name__ == '__main__':
    driver = getWebDriver()
    try:
        run(driver)
    except Exception as e:
        print(e)
    time.sleep(3)
    driver.quit()
