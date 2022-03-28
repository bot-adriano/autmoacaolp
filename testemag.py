import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
navegador = webdriver.Chrome()#  navegador
url = "https://prontos.lopesnet.com.br/auth/login?ReturnUrl=%2f"
new_url = "https://prontos.lopesnet.com.br/ProductSearch"
navegador.get(url)

navegador.get("https://prontos.lopesnet.com.br/auth/login?ReturnUrl=%2f")
navegador.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/span/input[1]').click()
input_place = navegador.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/span/input[1]')
input_place.send_keys('34084123838')
input_pass = navegador.find_element_by_xpath('//*[@id="senha"]')
input_pass.send_keys(34084123838)
navegador.find_element_by_xpath('//*[@id="btn-login"]').click()
sleep(1)
navegador.find_element_by_xpath('//*[@id="login"]/div[7]/div/div/div[3]/button[2]').click()
sleep(2)
# webdriver.ActionChains('navegador').move_to_element('<span class="menu-text">Imóveis</span>').perform()
# navegador.find_element_by_xpath('//*[@id="sidebar"]/ul/li[1]/a/span').click()
# navegador.find_element_by_xpath('//*[@id="sidebar"]/ul/li[1]/ul/li[2]/a').click()
navegador.execute_script("window.open('');")
navegador.switch_to.window(navegador.window_handles[1])
navegador.get(new_url)
sleep(2)



navegador.find_element_by_xpath('//*[@id="RealtyStatus_chosen"]/ul/li[3]/input').click()
# input_place = navegador.find_element_by_xpath('//*[@id="RealtyStatus_chosen"]/ul/li[3]/input')
# input_place.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
# #input_place.submit()
#
input_loc = navegador.find_element_by_xpath('//*[@id="ValueMinRent"]')
input_loc.send_keys('350000')
input_loc2 = navegador.find_element_by_xpath('//*[@id="ValueMaxRent"]')
input_loc2.send_keys('352000')
# navegador.find_element_by_xpath('//*[@id="RealtyStatus_chosen"]/ul').click()
# navegador.find_element_by_xpath('//*[@id="RealtyStatus_chosen"]/ul').click()
# navegador.find_element_by_xpath('//*[@id="RealtyStatus_chosen"]/div/ul/li[4]').click()
# navegador.find_element_by_xpath('//*[@id="form-product-search"]/div[1]/div/div[2]/div[3]/div/label[2]').click()
# navegador.find_element_by_xpath('//*[@id="myCompanies"]').click()
# navegador.find_element_by_xpath('//*[@id="selected-localization-resume"]').click()
# sleep(2)
# navegador.find_element_by_xpath('//*[@id="tab-by-region"]').click()
# sleep(1)
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[3]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[5]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[6]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[10]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[11]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[17]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[12]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[15]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[16]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[18]/div/label/input').click()
# navegador.find_element_by_xpath('//*[@id="by-region"]/div[3]/div/ul/li[19]/div/label/input').click()

# casa verde //*[@id="by-region"]/div[3]/div/ul/li[3]/div/label/input
# horto //*[@id="by-region"]/div[3]/div/ul/li[5]/div/label/input
# jacana //*[@id="by-region"]/div[3]/div/ul/li[6]/div/label/input
# mandaqui //*[@id="by-region"]/div[3]/div/ul/li[10]/div/label/input
# pq edu chaves //*[@id="by-region"]/div[3]/div/ul/li[11]/div/label/input
# pq novo mundo //*[@id="by-region"]/div[3]/div/ul/li[12]/div/label/input
# santana //*[@id="by-region"]/div[3]/div/ul/li[15]/div/label/input
# tremembe //*[@id="by-region"]/div[3]/div/ul/li[16]/div/label/input
# vila guliherme //*[@id="by-region"]/div[3]/div/ul/li[18]/div/label/input
# vila maria //*[@id="by-region"]/div[3]/div/ul/li[19]/div/label/input
#tucuruvi //*[@id="by-region"]/div[3]/div/ul/li[17]/div/label/input

navegador.find_element_by_xpath('//*[@id="btn-select-neighborhoods"]').click()
sleep(1)
navegador.find_element_by_xpath('//*[@id="btn-search-product"]').click()
sleep(4)
#navegador.find_element_by_xpath('//*[@id="productResultTab"]').click()
#navegador.find_element_by_xpath('//*[@id="bloco"]/div[2]/div/ul/li[1]').click()

#navegadorps = navegador.page_source
# print(navegador.page_source)
# print(navegadorps)

# bs = BeautifulSoup(navegadorps, 'html.parser')
#
# #print(bs)
# #print(bs.prettify())
# print(bs.find_all('li'))
# linhas = bs.find_all('li', {'class': 'item marginB5 col-xs-12 col-lg-12 product-item'})
# placas = bs.find_all('li', class_='kind')
# placa = bs.find_all('li', class_='cardlist__item ng-star-inserted')
# # linhas = bs.find_all('li', {'class': 'item marginB5 col-xs-12 col-lg-12 product-item'})
# # placas = bs.find_all('li', class_='kind')
# # placa = bs.find_all('li', class_='cardlist__item ng-star-inserted')
# print(linhas)
# print(placas)
# print(placa)
# with open("precos_imoveis3.csv", "a", newline="", encoding="utf-8") as d:
#     for placa in placas:
#
#         # placa = placas[0]
#         marca = placa.find('p', class_='card__location').get_text().strip()
#
#         try:
#             preco = placa.find('h5', class_='red').get_text().strip()
#             num_preco = preco[12:]  # pra retirar o endereco
#         except:
#             num_preco = '0'  # caso nao exista valor va ficar em zero
#         #  preco= '0'
#
#         linha = num_preco + ';' + marca + '\n' + "\n"
#         print(linha)
#         d.write(linha)
sleep(50)