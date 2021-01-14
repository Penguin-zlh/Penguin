from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import cv2 as cv


# 根据快递单号查询物流信息
def get_screenshot_and_info():

    options = webdriver.ChromeOptions()
    # 关闭左上方 Chrome 正受到自动测试软件的控制的提示
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # 开启浏览器对象
    browser = webdriver.Chrome(options=options)
    # 访问这个url
    browser.get('https://www.kuaidi100.com/')
    wait = WebDriverWait(browser, 10)
    browser.refresh()
    # 显示等待
    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_element_located((By.ID, 'menu-track')))
    # 窗口最大化
    browser.maximize_window()
    browser.find_element_by_name('postid').send_keys(nums)
    browser.find_element_by_id('query').click()
    time.sleep(1)
    browser.find_element_by_id('query').click()
    time.sleep(2)
    browser.execute_script("window.scrollBy(0, 488)")
    # 截图
    browser.get_screenshot_as_file(filename='info.png')
    items = browser.find_elements_by_xpath('//table[@class="result-info"]/tbody/tr')
    print('物流信息查询结果如下：\n')
    for item in items:
        time_ = item.find_element_by_xpath('.//td[1]').text.replace('\n', ' ')
        contex = item.find_element_by_xpath('.//td[3]').text
        print(f'时间：{time_}')
        print(f'状态：{contex}\n')
    browser.quit()
    # 显示截图
    src = cv.imread(filename='info.png')
    src = cv.resize(src, None, fx=0.7, fy=0.7)
    cv.imshow('result', src)
    cv.waitKey(0)


if __name__ == '__main__':
    nums = input('请输入您的单号：')
    print('\n')
    get_screenshot_and_info()
