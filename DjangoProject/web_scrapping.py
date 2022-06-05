import requests
import bs4
import xlsxwriter

url = 'https://www.emag.ro/label/Snowboard-mm?ref=hp_menu_quick-nav_651_15&type=link'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='card-v2')

context = {'data': []}
for case in cases:
    data = {}
    product_name = case.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url').text
    product_price = case.find('p', class_='product-new-price').text
    if product_name:
        data['product_name'] = product_name
    else:
        data['product_name'] = 'No data available'

    if product_price:
        data['product_price'] = product_price
    else:
        data['product_price'] = 'No data available'

    context['data'].append(data)


workbook = xlsxwriter.Workbook('Preturi snowboard.xlsx')
worksheet = workbook.add_worksheet('Snowboards')

row = 0
col = 0
for product in context['data']:
    worksheet.write(row, col, product['product_name'])
    worksheet.write(row, col + 1, product['product_price'])
    row += 1

workbook.close()

#pip install lxml
#pip install requests
#pip install bs4
#pip install xlsxwriter