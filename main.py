from email import header
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = 'https://prontos.lopesnet.com.br/ProductSearch/SearchResultProduct/?OrderSearchBy=&StateId=26&CityId=9668&OrderReference=&OrderTypeId=&OrderNeighborhood=&OrderAddress=&OrderUnityNumber=&OrderArea=&OrderBedRoom=&OrderGarage=&OrderRegister=&OrderValueSale=&OrderValorRent=&HasFilledFilter=True&Reference=&NidoReference=&FACId=&RealtyStatus=2&RealtyStatus=1&Hidden_RealtyStatus=%5B1%2C2%5D&RealtyNumber=&Purposes=2&Hidden_RealtyTypes=&Hidden_RealtyUtilitys=&ValueMinSale=&ValueMaxSale=&SizeValueMin=&SizeValueMax=&ValueMinRent=2.455%2C55&ValueMaxRent=5.999%2C99&RealtyDescription=&RealtyDeveloperDescription=&RealtyDeveloper=&RealtyNumberInLocalization=&RealtyUnity=&RealtyCep=&Hidden_RealtyCondoFeatures=&Hidden_RealtyUnitFeatures=&RealtyFootageMin=&RealtyFootageMax=&RealtyCondominiumMaxValue=0%2C00&RealtyTaxValue=0%2C00&RealtyPackValue=0%2C00&RealtyAreaValue=0%2C00&RealtyRegisterDateRange=&RealtyRegisterDateFrom=&RealtyRegisterDateTo=&RealtyDaysWithoutUpdated=&RealtyUpdateDateFrom=&RealtyUpdateDateTo=&RealtyConstructionYear=&OwnerCPF=&OwnerPhone=&OwnerEmail=&OptionRealtyPhotos=&OptionRealtySign=&OptionRealtyAdm=&CheckRealtyDocuments=&OptionRealtyOnCall=&OptionRealtyExclusivity=&OptionAcceptsPermute=&OptionAcceptsInstallment=&OptionAcceptsDifferentiatedValue=&OptionFreeWarranty=&OptionHighStandard=&RealtyInnerText=&Hidden_ProfessionalRoleIds=&MyCompanyCaptivator=false&Hidden_BrokersIds=&OrderReference=&StateIds=9668&CityIds=9668&ValueZones%5B0%5D=181&LocalizationModal_Version=2.0.1+-+Atualizado+-+10%2F11%2F2016+16%3A32'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div',
                       class_='card__textbox_container')  # aqui teremos q inspecionar as paginas e achar oq queremos
ultima_pagina = soup.find('li', class_='pager-control active').get_text().strip()  # aqui definimos a ultima pagina

for i in range(1, int(ultima_pagina)):
    url_page = f'https://prontos.lopesnet.com.br/ProductSearch/SearchResultProduct/?OrderSearchBy=&StateId=26&CityId=9668&OrderReference=&OrderTypeId=&OrderNeighborhood=&OrderAddress=&OrderUnityNumber=&OrderArea=&OrderBedRoom=&OrderGarage=&OrderRegister=&OrderValueSale=&OrderValorRent=&HasFilledFilter=True&Reference=&NidoReference=&FACId=&RealtyStatus=2&RealtyStatus=1&Hidden_RealtyStatus=%5B1%2C2%5D&RealtyNumber=&Purposes=2&Hidden_RealtyTypes=&Hidden_RealtyUtilitys=&ValueMinSale=&ValueMaxSale=&SizeValueMin=&SizeValueMax=&ValueMinRent=2.455%2C55&ValueMaxRent=5.999%2C99&RealtyDescription=&RealtyDeveloperDescription=&RealtyDeveloper=&RealtyNumberInLocalization=&RealtyUnity=&RealtyCep=&Hidden_RealtyCondoFeatures=&Hidden_RealtyUnitFeatures=&RealtyFootageMin=&RealtyFootageMax=&RealtyCondominiumMaxValue=0%2C00&RealtyTaxValue=0%2C00&RealtyPackValue=0%2C00&RealtyAreaValue=0%2C00&RealtyRegisterDateRange=&RealtyRegisterDateFrom=&RealtyRegisterDateTo=&RealtyDaysWithoutUpdated=&RealtyUpdateDateFrom=&RealtyUpdateDateTo=&RealtyConstructionYear=&OwnerCPF=&OwnerPhone=&OwnerEmail=&OptionRealtyPhotos=&OptionRealtySign=&OptionRealtyAdm=&CheckRealtyDocuments=&OptionRealtyOnCall=&OptionRealtyExclusivity=&OptionAcceptsPermute=&OptionAcceptsInstallment=&OptionAcceptsDifferentiatedValue=&OptionFreeWarranty=&OptionHighStandard=&RealtyInnerText=&Hidden_ProfessionalRoleIds=&MyCompanyCaptivator=false&Hidden_BrokersIds=&OrderReference=&StateIds=9668&CityIds=9668&ValueZones%5B0%5D=181&LocalizationModal_Version=2.0.1+-+Atualizado+-+10%2F11%2F2016+16%3A32'
    site = requests.get(url_page, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='kind')
# with open('precos_imoveis1.csv','a', newline='', encoding='utf-8') as f : #o 'a' a de append é pra criar uma vez o arquivo e nas proximas vezes nao sobresscrever
with open("precos_imoveis3.csv", "a", newline="", encoding="utf-8") as d:
    for placa in placas:

        # placa = placas[0]
        marca = placa.find('p', class_='card__location').get_text().strip()

        try:
            preco = placa.find('h5', class_='red').get_text().strip()
            num_preco = preco[12:]  # pra retirar o endereco
        except:
            num_preco = '0'  # caso nao exista valor va ficar em zero
        #  preco= '0'

        linha = num_preco + ';' + marca + '\n' + "\n"
        print(linha)
        d.write(linha)

    # print(url_page)
# print(preco, endereco,num_marca)
