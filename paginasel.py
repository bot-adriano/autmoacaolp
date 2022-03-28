import requests
from bs4 import BeautifulSoup
from selenium import webdriver
DRIVER_PATH ='/path/to/chromedriver'
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
driver = webdriver.chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')
options = Options()
driver = webdriver.chrome(options=options, executable_path=DRIVER_PATH)
#
#options.add_argument('--headless')
#options.add_argument('window-size=400,800')
#from selenium.webdriver.common.by import By class_name


navegador = webdriver.Chrome()
#navegador.get('http://corretor.associadolopesone.com.br/index.html')
driver.get('https://www.letscode.com.br/blog/aprenda-a-utilizar-o-selenium-para-web-scraping')
print(driver.page_source)
sleep(2)


input_place = driver.find_element(By.CLASS_NAME, "header-item-label")

#input_place = navegador.find_element_by_class_name('header-item-label')
input_place.click()
#site = BeautifulSoup(navegador.page_source,'html.parser')
#print(site.prettify())


from selenium.webdriver.common.by import By
#fnd_btn = driver.find_element(By.CLASS_NAME, 'box-content')

#elemento.click()
