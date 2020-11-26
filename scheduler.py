import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

barcode = input("Input your barcode: ")
pin = input("Input your PIN: ")
barcode_to_reserve = input("Input the BARCODE of the session you want to reserve: ")
request_time_ms = int(input("Input how the MS between every request (recommended 5000): "))

df = pd.DataFrame()

# Create a session
s = requests.Session()
# Landing request
r = s.get('https://geegeereg.uottawa.ca/geegeereg/Activities/ActivitiesDetails.asp?aid=316')

baseline_link = "https://geegeereg.uottawa.ca/geegeereg/"

# Get initial cookies
asps_cookie = s.cookies['ASPSESSIONIDQCTTATCC']
sCheck_cookie = s.cookies['SCheck']

jar = s.cookies

print(asps_cookie)
print(sCheck_cookie)

print(r.headers)

print(s.cookies)




def refresh_data():
    course_names = []
    available_slots = []
    codes = []
    dates = []
    times = []
    days = []
    barcodes = []
    links = []
    link_type = []

    for i in range(6):  # fix magic number
        r4 = s.get(
            'https://geegeereg.uottawa.ca/geegeereg/Activities/ActivitiesDetails.asp?GetPagingData=true&aid=316&sEcho=4&iColumns=9&sColumns=&iDisplayStart=' + str(
                (i * 10)) + '&iDisplayLength=10&ajax=true')
        soup = BeautifulSoup(r4.text, 'lxml')
        for row in soup.find_all(headers="BasketLink"):
            try:
                links.append(row.a['href'])
                link_type.append(row.a.text.split()[0])
            except:
                links.append(0)
                link_type.append(0)
        for row in soup.find_all(headers='Course'):
            course_names.append(row.div.text)
        for row in soup.find_all(headers="Times"):
            times.append(row.text.split()[0] + "-" + row.text.split()[2])
        for row in soup.find_all(headers="Dates"):
            dates.append(row.text.split()[0])
        for row in soup.find_all(headers="Available"):
            available_slots.append(row.text.split()[0])
        for row in soup.find_all(headers="Barcode"):
            barcodes.append(row.text.split()[0])

    # print(len(links))
    # print(len(link_type))
    # print(len(course_names))
    # print(len(times))
    # print(len(dates))
    # print(len(available_slots))
    # print(len(barcodes))

    df['course_names'] = course_names
    df['times'] = times
    df['dates'] = dates
    df['available'] = available_slots
    df['barcode'] = barcodes
    df['links'] = links
    df['link_type'] = link_type

    # df.to_csv("./uottawa_gym_info.csv")


login_request = s.post("https://geegeereg.uottawa.ca/geegeereg/MyAccount/MyAccountUserLogin.asp",
                       data={'ClientBarcode': barcode, 'AccountPin': pin, 'Enter': 'Login', 'FullPage': 'false'})


def auto_request():
    count = 0
    while list(df[df['barcode'] == barcode_to_reserve].to_dict().get('links').values())[0] == 0:
        refresh_data()
        time.sleep(request_time_ms * 0.001)
        count += 1
        print(count)
    add_to_cart_request = s.post(
        baseline_link + list(df[df['barcode'] == barcode_to_reserve].to_dict().get('links').values())[0][3:])
    checkout_request = s.post(
        baseline_link + "MyBasket/MyBasketCheckout.asp?URLAddress=/geegeereg/MyBasket/MyBasketCheckout.asp&PayAuthorizeWait=Yes")


refresh_data()
auto_request()
