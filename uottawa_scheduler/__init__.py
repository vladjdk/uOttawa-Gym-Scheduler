import time

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import sys

def refresh_data(s, df):
    course_names = []
    available_slots = []
    dates = []
    times = []
    barcodes = []
    links = []
    link_type = []

    for i in range(6):  # TODO: fix magic number, 6 represents the number of pages that the school usually puts up
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

    df.to_csv("./uottawa_gym_info.csv")

def auto_request(s, df, session_code, request_time, baseline_link):
    count = 0
    while list(df[df['barcode'] == session_code].to_dict().get('links').values())[0] == 0:
        refresh_data()
        time.sleep(request_time * 0.001)
        count += 1
        print(count)
    add_to_cart_request = s.post(
        baseline_link + list(df[df['barcode'] == session_code].to_dict().get('links').values())[0][3:])
    checkout_request = s.post("{}/MyBasket/MyBasketCheckout.asp?URLAddress=/geegeereg/MyBasket/MyBasketCheckout.asp"
                              "&PayAuthorizeWait=Yes".format(baseline_link))
    checkout_again = s.post("{}/MyBasket/MyBasketCheckout.asp?ApplyPayment=true".format(baseline_link))
    waiver = s.post("{}/MyBasket/MyBasketProgramLiabilityWaiver.asp".format(baseline_link))
    final_checkout = s.post("{}/MyBasket/MyBasketCheckout.asp".format(baseline_link))
    print("Successfully scheduled for {}.".format(session_code))


def run(barcode, pin, session_code, request_time):
    df = DataFrame()
    baseline_link = "https://geegeereg.uottawa.ca/geegeereg"

    # Create a session
    s = requests.Session()
    # Landing request
    s.get('{}/Activities/ActivitiesDetails.asp?aid=316'.format(baseline_link))


    # Login Request
    s.post("https://geegeereg.uottawa.ca/geegeereg/MyAccount/MyAccountUserLogin.asp",
                           data={'ClientBarcode': barcode, 'AccountPin': pin, 'Enter': 'Login', 'FullPage': 'false'})

    refresh_data(s, df)
    auto_request(s, df, session_code, request_time, baseline_link)

def main(argv):
    run(argv[1], argv[2], argv[3], argv[4])


if __name__ == "__main__":
    main(sys.argv)