import time

from selenium.webdriver.common.by import By


def test_main_page(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "#logo")
    browser.find_element(By.CSS_SELECTOR, "#search")
    browser.find_element(By.CSS_SELECTOR, "#cart")
    browser.find_element(By.CSS_SELECTOR, "#menu")
    browser.find_element(By.CSS_SELECTOR, "#slideshow0")
    browser.find_element(By.CSS_SELECTOR, "#carousel0")
    browser.find_elements(By.CSS_SELECTOR, ".product-layout")


def test_catalog_page(browser, url):
    browser.get(url + "/desktops")
    browser.find_element(By.CSS_SELECTOR, ".breadcrumb")
    browser.find_element(By.CSS_SELECTOR, "#column-left")
    browser.find_element(By.CSS_SELECTOR, "#banner0")
    browser.find_element(By.CSS_SELECTOR, "h2")
    browser.find_element(By.CSS_SELECTOR, "#list-view")
    browser.find_element(By.CSS_SELECTOR, "#grid-view")
    browser.find_element(By.CSS_SELECTOR, "#compare-total")
    browser.find_elements(By.CSS_SELECTOR, ".form-group.input-group.input-group-sm")
