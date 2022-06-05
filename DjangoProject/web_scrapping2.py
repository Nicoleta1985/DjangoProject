import requests
import bs4
import xlsxwriter

url = 'https://www.flanco.ro/laptop-it-tablete/laptop/gaming-laptop.html'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('li', class_='item product product-item produs')

context = {'data': []}
for case in cases:
    data = {}
    product_name = case.find('a', class_='product-item-link').text
    product_price = case.find('span', class_='price').text
    if product_name:
        data['product_name'] = product_name
    else:
        data['product_name'] = 'No data available'

    if product_price:
        data['product_price'] = product_price
    else:
        data['product_price'] = 'No data available'

    context['data'].append(data)


workbook = xlsxwriter.Workbook('Preturi laptop.xlsx')
worksheet = workbook.add_worksheet('Laptop')

row = 0
col = 0
for product in context['data']:
    worksheet.write(row, col, product['product_name'])
    worksheet.write(row, col + 1, product['product_price'])
    row += 1

workbook.close()