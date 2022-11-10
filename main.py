import parsel
import os
import platform
from pprint import pprint
from time import sleep
from isbn import isbn10to13
from dotenv import load_dotenv
from xpaths import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ChromeOptions

load_dotenv()

API_URL = 'https://api.bookscouter.com/v4/prices/sell/{}?base64=1'
BOOK_URL = 'https://bookscouter.com/book/{}?type=sell'

driver = None
chrome_options = ChromeOptions()
#Uncomment this line
chrome_options.add_argument("log-level=3")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
#until this line to switch to headless mode

if platform.system() == 'Windows':
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH_WINDOWS'), chrome_options=chrome_options)
elif platform.system() == 'Linux':
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH_LINUX'), chrome_options=chrome_options)


while True:
    isbn = str(input('Enter isbn:'))
    driver.get(BOOK_URL.format(isbn))
    try:

        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, VENDOR_XPATH))
        )

        selector = parsel.Selector(text=driver.page_source)
        vendors_html = selector.xpath(VENDOR_XPATH).getall()
        vendors = []
        for vendor_html in vendors_html:
            vendor = {}
            vendor_selector = parsel.Selector(text=vendor_html)
            seller = vendor_selector.xpath('string(//div/div[2])').get()
            vendor['seller'] = 'N/A' if seller is None else seller.strip()
            price = vendor_selector.xpath('string(//div/div[4])').get()
            vendor['price'] = 'N/A' if price is None else price.strip()
            pprint(vendor)
    except TimeoutException:
        print('Element not found')




