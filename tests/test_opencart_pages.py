from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#search input[name=search]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#cart button[data-toggle=dropdown]")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#slideshow0")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#carousel0")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.product-layout")))


def test_catalog_desktop_page(browser, url):
    browser.get(url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#search input[name=search]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#cart button[data-toggle=dropdown]")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#column-left")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#banner0")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#list-view")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#grid-view")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#compare-total")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select#input-sort")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select#input-limit")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.product-layout")))


def test_tablet_item_page(browser, url):
    browser.get(url + "/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.thumbnails a.thumbnail")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-toggle=tab]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for=input-quantity]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#input-quantity")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#button-cart")))


def test_login_admin_page(browser, url):
    browser.get(url + "/admin/")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-logo")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.panel-title")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for=input-username]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-username")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for=input-password]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.help-block a"), "Forgotten Password"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = submit]")))


def test_register_page(browser, url):
    browser.get(url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#search input[name=search]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#cart button[data-toggle=dropdown]")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "fieldset#account div.form-group.required")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "fieldset#account input[name=customer_group_id]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset#account input#input-firstname")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset#account input#input-lastname")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset#account input#input-email")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset#account input#input-telephone")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset input#input-password")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset input#input-confirm")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=checkbox][name=agree]")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=submit][value=Continue]")))
