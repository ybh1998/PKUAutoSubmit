import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import *


def goto_simso(driver):
    driver.get('''https://portal.pku.edu.cn/portal2017/util/appSysRedir.do?appId
=stuCampusExEn''')
    wait_for_loading(driver)
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="#/editApplyInfo"]')
        )
    ).find_element(By.CLASS_NAME, 'el-card__body').click()
    wait_for_loading(driver)


def submit(driver):
    name = b'\xe4\xbf\x9d\xe5\xad\x98'.decode('UTF-8')
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button/span[normalize-space(text())="' + name + '"]')
        )
    ).click()
    name = b'\xe6\x8f\x90\xe7\xa4\xba'.decode('UTF-8')
    dialog_element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="dialog"]')
        )
    )
    wait_for_animation(driver)
    name = b'\xe6\x8f\x90\xe4\xba\xa4'.decode('UTF-8')
    dialog_element.find_element(
        By.XPATH, './/button/span[normalize-space(text())="' + name + '"]'
    ).click()
    name = (b'\xe5\xa4\x87\xe6\xa1\x88\xe5\xae\x8c\xe6\x88\x90\xef\xbc\x8c\xe7'
        b'\xb3\xbb\xe7\xbb\x9f\xe9\x80\x9a\xe8\xbf\x87\xe3\x80\x82'
    ).decode('UTF-8')
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.XPATH, '//p[contains(text(), "' + name + '")]')
        )
    )
    print('Submit successfully')


def run(driver):
    loginPortal(driver)
    goto_simso(driver)
    input_select(driver, 'sqlb',
        b'\xe5\x87\xba\xe6\xa0\xa1'.decode('UTF-8'))
    input_select(driver, 'szxq', os.environ['SZXQ'])
    input_text(driver, 'email', 'input', os.environ['EMAIL'])
    input_text(driver, 'lxdh', 'input', os.environ['LXDH'])
    input_select(driver, 'crxsyxx', os.environ['CRXSYXX'])
    input_text(driver, 'crxsy', 'textarea', os.environ['CRXSY'])
    input_select(driver, 'cxmdd', os.environ['CXMDD'])
    input_text(driver, 'cxxdgj', 'textarea', os.environ['CXXDGJ'])
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'el-checkbox__inner'))
    ).click()
    wait_for_animation(driver)
    submit(driver)
    goto_simso(driver)
    input_select(driver, 'sqlb',
        b'\xe5\x85\xa5\xe6\xa0\xa1'.decode('UTF-8'))
    input_select(driver, 'szxq', os.environ['SZXQ'])
    input_text(driver, 'email', 'input', os.environ['EMAIL'])
    input_text(driver, 'lxdh', 'input', os.environ['LXDH'])
    input_select(driver, 'crxsyxx', os.environ['CRXSYXX'])
    input_text(driver, 'crxsy', 'textarea', os.environ['CRXSY'])
    input_select(driver, 'rxjzd', os.environ['RXJZD'])
    input_select(driver, 'jzdbjqx', os.environ['JZDBJQX'])
    input_text(driver, 'jzdbjjd', 'textarea', os.environ['JZDBJJD'])
    input_select_radio(driver, 'jzdbjyzzj14', os.environ['JZDBJYZZJ14'])
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'el-checkbox__inner'))
    ).click()
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
