# -*- coding: utf-8 -*-
"""
Version:    V1.0
Time:       2020.09.27
Author:     Gaozhl
"""
import os
import time
from selenium import webdriver

# 获取webdriver
# 此处使用的是火狐浏览器，需要匹配对应的版本
FirefoxDriver = "./geckodriver.exe"
os.environ["geckodriver"] = FirefoxDriver
driver = webdriver.Firefox(executable_path=FirefoxDriver)


def url_open(url):
    """
    打开页面
    :param url:     要打开的url地址
    :return:
    """
    driver.get(url)
    # 最大化页面防止某些情况下遮挡元素
    driver.maximize_window()


def click(element_type, element):
    """
    点击页面上的元素
    :param element_type:    需要点击的元素类型，
                            包括如下的内容：
                             xpath, class, css, id
    :param element:         元素内容
    :return:
    """
    if element_type == 'xpath':
        driver.find_element_by_xpath(element).click()
    elif element_type == 'class':
        driver.find_element_by_class_name(element).click()
    elif element_type == 'css':
        driver.find_element_by_css_selector(element).click()
    elif element_type == 'id':
        driver.find_element_by_id(element).click()
    else:
        return False


def clear(element_type, element):
    """
    清楚选中页面上的元素中内容
    :param element_type:    需要点击的元素类型，
                            包括如下的内容：
                             xpath, class, css, id
    :param element:         元素内容
    :return:
    """
    if element_type == 'xpath':
        driver.find_element_by_xpath(element).clear()
    elif element_type == 'class':
        driver.find_element_by_class_name(element).clear()
    elif element_type == 'css':
        driver.find_element_by_css_selector(element).clear()
    elif element_type == 'id':
        driver.find_element_by_id(element).clear()
    else:
        return False


def send_key(element_type, element, msg):
    """
    输入相关内容
    :param element_type:    需要点击的元素类型，
                            包括如下的内容：
                             xpath, class, css, id
    :param element:         元素内容
    :param msg:             输入的内容
    :return:
    """
    if element_type == 'xpath':
        driver.find_element_by_xpath(element).send_keys(msg)
    elif element_type == 'class':
        driver.find_element_by_class_name(element).send_keys(msg)
    elif element_type == 'css':
        driver.find_element_by_css_selector(element).send_keys(msg)
    elif element_type == 'id':
        driver.find_element_by_id(element).send_keys(msg)
    else:
        return False


if __name__ == '__main__':
    url_open("url")

    time.sleep(5)
    login_input_xpath = 'xxxxx'

    click(element_type='Xpath', element=login_input_xpath)
    clear(element_type='Xpath', element=login_input_xpath)
    send_key(element_type="xpath", element=login_input_xpath, msg="xxx")
