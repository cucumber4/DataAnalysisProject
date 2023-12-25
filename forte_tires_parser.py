from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tires_link_generator import fortebank_market_links
import time
import pandas as pd

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

item_table = pd.DataFrame(columns=['Tire Name', 'Brand', 'Price in ₸', 'Season', 'Spikes', 'Diameter', 'High', 'Width'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

page_count = 0

for link in fortebank_market_links:
    URL = link
    driver.get(URL)
    time.sleep(5)

    content = driver.page_source
    soup = bs(content, 'html.parser')
    item_link = []

    items = soup.find_all(class_='category-grid ng-star-inserted')


    item_count = 0

    for item in items:
        links = item.findAll(class_='link ng-star-inserted')
        print('##### '+ link + ' ####')
        page_count=page_count+1
        print(page_count)

        for link in links:
            href_value = link.get('href')
            item_link.append(href_value)

            driver.get('https://market.forte.kz/'+href_value)

            chars = soup.find(class_='ng-star-inserted')

            try:
                name_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[@class="title"]')))
                name = name_element.text.strip()
                print(name)
            except Exception as e:
                name = None

            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="description ng-star-inserted"]')
                div_text = div_element.text
                brand_name = div_text.split(':')[-1].strip()
                print(brand_name)
            except Exception as e:
                brand_name = None

            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="merchant--price"]')
                div_text = div_element.text
                price = div_text.split(':')[-1].strip().replace('&nbsp;', '').replace('₸', '').replace(' ', '')
                print(price)
            except Exception as e:
                price = None

            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="description ng-star-inserted"][2]')
                div_text = div_element.text
                season = div_text.split(':')[-1].strip()
                print(season)
            except Exception as e:
                season = None

            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="description ng-star-inserted"][3]')
                div_text = div_element.text
                spikes = div_text.split(':')[-1].strip()
                print(spikes)
            except Exception as e:
                spikes = None


            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="description ng-star-inserted"][4]')
                div_text = div_element.text
                diameter = div_text.split(':')[-1].strip()
                print(diameter)
            except Exception as e:
                diameter = None


            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="description ng-star-inserted"][5]')
                div_text = div_element.text
                high = div_text.split(':')[-1].strip()
                print(high)
            except Exception as e:
                high = None


            try:
                div_element = driver.find_element(By.XPATH, '//div[@class="description ng-star-inserted"][6]')
                div_text = div_element.text
                width = div_text.split(':')[-1].strip()
                print(width)
            except Exception as e:
                width = None


            row = [name, brand_name, price, season, spikes, diameter, high, width]
            item_table.loc[len(item_table)] = row


            item_count=item_count+1
            print(item_count)

            time.sleep(3)

item_table.to_excel('DataSets/FORTEBANK_tires.xlsx', index=False)
item_table.to_csv('DataSets/FORTEBANK_tires.csv', index=False)