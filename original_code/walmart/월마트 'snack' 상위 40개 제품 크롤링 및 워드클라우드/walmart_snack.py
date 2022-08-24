from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=options)
from bs4 import BeautifulSoup as bs
import time
import requests

import csv
file = open('../walmart_snack(REAL).csv', 'w')
writer = csv.writer(file)

#write header rows
writer.writerow(['score', 'author', 'date', 'comment'])

chrome_driver = driver_path = '../chromedriver'
driver = webdriver.Chrome(chrome_driver)
driver.implicitly_wait(3)


driver.get('https://www.walmart.com/search/?query=snack')
count = 0
time.sleep(2)
item_boxes = driver.find_elements_by_css_selector("a.product-title-link.line-clamp.line-clamp-2")
print("item_boxes :", len(item_boxes))
for i in range(4): #한 화면에 40개, 크롤링
    driver.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[' + str(i + 1) + ']').click() # 1위부터 하나씩
    time.sleep(3)
    sub_url = "https://www.walmart.com/reviews/product/" + driver.current_url.split('/').pop()  # see all reviews
    driver.get(sub_url)
    time.sleep(2)
    time.sleep(2)
    if i > 0:
        repeat = driver.find_elements_by_css_selector("ul.paginator-list li")
        print("reviews page num to be scanned: ", repeat[-1].text)
        print("number of repeat", repeat[-1].text)
        for repeat in range(1, int(repeat[-1].text) + 1):
            driver.get(sub_url + "?page=" + str(repeat))
            time.sleep(2)
            sub_boxes = driver.find_elements_by_css_selector("div.review")
            for j in range(len(sub_boxes)):
                try:
                    stars = sub_boxes[j].find_elements_by_css_selector("span.stars-container span.elc-icon.star.star-small.star-rated.elc-icon-star-rating")
                    score = len(stars)
                    author = sub_boxes[j].find_element_by_css_selector("span.review-footer-userNickname").text
                    date = sub_boxes[j].find_element_by_css_selector(".review-footer-submissionTime").text
                    comment = sub_boxes[j].find_element_by_css_selector("div.review-text").text
                    writer.writerow([score, author, date, comment])
                    count += 1
                    print(count)
                except:
                    print("there is an error with " + str(i) + "번째 스낵에서 에러")
    driver.back()
    driver.back()
driver.close()

