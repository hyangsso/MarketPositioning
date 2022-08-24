from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=options)

import time
import csv
file = open('../walmart_snack123.csv', 'w')
writer = csv.writer(file)

#write header rows
writer.writerow(['score', 'author', 'date', 'comment'])

chrome_driver = driver_path = '../data/chromedriver'
driver = webdriver.Chrome(chrome_driver)
driver.implicitly_wait(3)


driver.get('https://www.walmart.com/search/?query=snack')
time.sleep(2)
item_boxes = driver.find_elements_by_css_selector("a.product-title-link.line-clamp.line-clamp-2")
for i in range(1,len(item_boxes)): #한 화면에 40개, 크롤링 len(item_boxes)
    try:
        driver.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[' + str(i + 1) + ']').click() # 1위부터 하나씩
        time.sleep(2)
        product = driver.find_element_by_css_selector("h1.prod-ProductTitle.prod-productTitle-buyBox.font-bold").text
        sub_url = "https://www.walmart.com/reviews/product/" + driver.current_url.split('/').pop()  # see all reviews
        driver.get(sub_url)
        time.sleep(2)
        repeat = driver.find_elements_by_css_selector("ul.paginator-list li")
        print("item # at: ", i)
        for repeat in range(int(repeat[-1].text) + 1): #review-page
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
                    print(str(score) + "\t" + product + "\t" + author + "\t" + date + "\t" + comment)
                    #writer.writerow([score,product, author, date, comment])
                except:
                    print("there is an error with: " + str(j) + "번째 댓글, 페이지: ", str(repeat))
    except:
        print("scanning item #" + str(i) + "failed")
    driver.get('https://www.walmart.com/search/?query=snack')
driver.close()
