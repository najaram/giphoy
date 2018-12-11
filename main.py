from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def download_urls():
    browser = webdriver.Firefox()
    browser.get('https://giphy.com/')

    search_elem = browser.find_element_by_id('search-box')
    search_elem.send_keys('hello world')
    search_elem.send_keys(Keys.ENTER)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )
        lists = browser.find_elements_by_class_name('gif_gif__3Tdyi')

        for index in range(len(lists)):
            a_tag = lists[index].find_element_by_tag_name('a')
            print(a_tag.get_attribute('href'))
            link = a_tag.get_attribute('href')
            # write the links to a file
            text_file = open('gif_urls.txt', 'a')
            text_file.write(link+'\n')
        browser.close()
    except:
        print('No results found')


def send_urls():
    urls = open('gif_urls.txt')
    gip_links = urls.readlines()

    for i in range(len(gip_links)):
        browser = webdriver.Firefox()
        browser.get(gip_links[i])

        # facebook share link
        fb_share = browser.find_element_by_class_name('_2V0DNe9b5bQu46I_uujrG7')
        browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        browser.get(fb_share.get_attribute('href'))

        # login
        fb_email = browser.find_element_by_id('email')
        fb_email.send_keys('your-email')
        fb_password = browser.find_element_by_id('pass')
        fb_password.send_keys('your-password')
        fb_password.submit()

        try:
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
            )

            text_post = browser.find_element_by_tag_name('textarea')
            text_post.send_keys('This is an automated posts by Python')

            send_button = browser.find_element_by_name('__CONFIRM__')
            send_button.click()
        except:
            browser.quit()


download_urls()
send_urls()
