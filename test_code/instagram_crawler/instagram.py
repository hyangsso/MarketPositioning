import os
import re
from time import sleep

try:
    from selenium import webdriver as wb

except ImportError:
    print("Trying to Install required module: requests\n")
    os.system('python -m pip install selenium')
    from selenium import webdriver as wb

try:
    from bs4 import BeautifulSoup

except ImportError:
    print("Trying to Install required module: bs4\n")
    os.system('python -m pip install bs4')
    from bs4 import BeautifulSoup

try:
    import csv

except ImportError:
    print("Trying to Install required module: csv\n")
    os.system('python -m pip install csv')
    import csv


def crawl_insta_link(kwd, user_id, user_pw):
    driver = wb.Chrome('../chromedriver.exe')
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)

    id_input = driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')[0]
    id_input.send_keys(user_id)
    password_input = driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')[0]
    password_input.send_keys(user_pw)
    password_input.submit()
    sleep(3)

    url = "https://www.instagram.com/explore/tags/" + str(kwd)
    driver.get(url)
    sleep(3)

    item_link = []
    while True:
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        for tmp in soup.find_all(name="div", attrs={"class": "Nnq7C weEfm"}):
            dummy_link = tmp.select('a')
            for dummy in dummy_link:
                item_link.append(dummy.attrs['href'])

        if len(item_link) > 100:
            break

        # scroll down
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(30)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                continue

    print("Total link: ", end=' ')
    print(len(item_link))
    return item_link[:5]


def save_links_to_txt(file_name, link_list):
    file = open(file_name + '.txt', 'w')

    for link in link_list:
        file.write(str(link) + '\n')

    file.close()


def crawl_instagram_data(link_file_name):
    driver = wb.Chrome('../chromedriver.exe')
    link_list = []

    with open(link_file_name, 'r') as file:
        for link in file:
            link_list.append(link)

    link_list = list(set(link_list))
    print(len(list(set(link_list))))

    feed = []
    for link in link_list:
        article = 'https://www.instagram.com' + str(link)
        driver.get(article)
        sleep(3)

        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        for i, tmp in enumerate(soup.find_all(name='div', attrs={"class": "C4VMK"})):
            date_data = soup.find(name='time', attrs={"class": "_1o9PC Nzb55"}).attrs['datetime']
            tmp_list = [date_data]
            for j, word in enumerate(tmp):
                if i == 0 and j == 2:
                    writer_like_point = soup.find(name='div', attrs={"class": "Nm9Fw"})
                    try:
                        likes = str(writer_like_point.select('span'))
                        start = likes.find('<span>')
                        end = likes.find('</span>')
                        tmp_list.append(likes[start + 6: end])
                    except:
                        likes = str(soup.select('head > meta:nth-child(35)'))
                        tmp_list.append(likes)

                else:
                    tmp_list.append(word.get_text())
            feed.append(tmp_list)

    #pprint.pprint(feed)
    return feed


def save_to_csv(new_file_name, data_list):
    output = open(new_file_name + '.csv', 'w', encoding='utf-8-sig', newline='')
    wr = csv.writer(output)
    wr.writerow(['date', 'user_id', 'text', 'like', 'tag'])

    for record in data_list:
        wr.writerow(record)

    output.close()
