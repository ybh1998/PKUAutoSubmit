import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
                    'div[class$="-active"], div[class*="-active "]'
                ))
            )
            print('Waiting for animation to finish')
            time.sleep(1)
        except:
            break


def input_select(driver, tag_for, text):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'label[for="' + tag_for + '"]')
        )
    ).find_element(By.XPATH, '..')
    element.find_element(By.TAG_NAME, 'input').click()
    wait_for_animation(driver)
    WebDriverWait(element, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//li/span[text()="' + text + '"]')
        )
    ).click()
    wait_for_animation(driver)


def input_text(driver, tag_for, tag_name, text):
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'label[for="' + tag_for + '"]')
        )
    ).find_element(By.XPATH, '..').find_element(By.TAG_NAME, tag_name)
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
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'label[for="' + tag_for + '"]')
        )
    ).find_element(By.XPATH, '..')
    wait_for_animation(driver)
    WebDriverWait(element, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//span[normalize-space(text()) = "' + text + '"]')
        )
    ).click()
    wait_for_animation(driver)


def goto_simso(driver):
    driver.get('''https://portal.pku.edu.cn/portal2017/util/appSysRedir.do?appId
=stuCampusExEn''')
    wait_for_loading(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="#/editApplyInfo"]')
        )
    ).find_element(By.CLASS_NAME, 'el-card__body').click()
    wait_for_loading(driver)


def submit(driver):
    name = b'\xe4\xbf\x9d\xe5\xad\x98'.decode('UTF-8')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button/span[normalize-space(text())="' + name + '"]')
        )
    ).click()
    name = b'\xe6\x8f\x90\xe7\xa4\xba'.decode('UTF-8')
    dialog_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="dialog"]')
        )
    )
    wait_for_animation(driver)
    name = b'\xe6\x8f\x90\xe4\xba\xa4'.decode('UTF-8')
    dialog_element.find_element(
        By.XPATH, './/button/span[normalize-space(text())="' + name + '"]'
    ).click()
    name = (b'\xe5\xa4\x87\xe6\xa1\x88\xe5\xae\x8c\xe6\x88\x90\xef\xbc\x8c' + 
        b'\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x80\x9a\xe8\xbf\x87\xe3\x80\x82'
    ).decode('UTF-8')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//p[contains(text(), "' + name + '")]')
        )
    )
    print('Submit successfully')


if __name__ == '__main__':
    print('PKUAutoSubmit by ybh1998, use at your own risk!')
    options = webdriver.firefox.options.Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get('''https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appNam
e=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97
%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https%3A%2F%2Fportal.pku.edu.cn%2Fpor
tal2017%2FssoLogin.do''')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'user_name'))
    ).send_keys(os.environ['USERNAME'])
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    ).send_keys(os.environ['PASSWORD'])
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'logon_button'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'stuCampusExEnReq'))
    )
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
    WebDriverWait(driver, 10).until(
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
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'el-checkbox__inner'))
    ).click()
    wait_for_animation(driver)
    submit(driver)
    time.sleep(3)
    driver.quit()
