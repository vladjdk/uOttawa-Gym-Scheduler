import json
import time

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import sys
from datetime import datetime, timedelta
import pandas as pd

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
    df['weekdays'] = pd.to_datetime(df['dates']).dt.weekday
    df['available'] = available_slots
    df['barcode'] = barcodes
    df['links'] = links
    df['link_type'] = link_type


    df.to_csv("./uottawa_gym_info.csv")
    return df


def auto_request(s, schedule, request_time, baseline_link):
    df = DataFrame()
    df = refresh_data(s, df)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', "friday", "saturday", "sunday"]
    day = datetime.now().weekday()+2
    filtered_df = df[df['weekdays'] == day]
    filtered_df = filtered_df[filtered_df['times'].str.lower() == schedule[days[day]].lower()]
    session_code = filtered_df['barcode'].iloc[0]

    count = 0
    today = datetime.today()
    time_to_start = datetime(today.year, today.month, today.day, 20, 55)

    has_time = False
    for i in range(7):
        if schedule[days[day]] != "":
            has_time = True
            break

    if not has_time:
        raise Exception("Make sure you have a time inputted into info.json")


    while(True):

        while schedule[days[time_to_start.weekday()]] == "":
            time_to_start = time_to_start + timedelta(days=1)

        if datetime.today() < time_to_start:
            print("Sleeping {} seconds, until 5 mins before the opening time. Now we wait! Check back on {}/{}/{} at {}:{} to see progress.".format((time_to_start - today).seconds+(time_to_start-today).days*86400, time_to_start.year, time_to_start.month, time_to_start.day, time_to_start.hour, time_to_start.minute))
            time.sleep((time_to_start-today).seconds+(time_to_start-today).days*86400)
            s = login(json.loads(open("./info.json").read())["login"]["barcode"], json.loads(open("./info.json").read())["login"]["pin"])
            time_to_start = time_to_start + timedelta(days=1)



        while list(df[df['barcode'] == session_code].to_dict().get('links').values())[0] == 0:
            df = refresh_data(s,df)

            day = datetime.now().weekday() + 2
            filtered_df = df[df['weekdays'] == day]
            filtered_df = filtered_df[filtered_df['times'].str.lower() == schedule[days[day]].lower()]
            session_code = filtered_df['barcode'].iloc[0]

            time.sleep(int(request_time) * 0.001)
            count += 1
            print(count, flush=True)

        if list(df[df['barcode'] == session_code].to_dict().get('link_type').values())[0] == "Waitlist":
            time_to_start = datetime(time_to_start + timedelta(days=1))
        else:
            add_to_cart_request = s.post(
                baseline_link + list(df[df['barcode'] == session_code].to_dict().get('links').values())[0][2:])
            checkout_request = s.post("{}/MyBasket/MyBasketCheckout.asp?URLAddress=//MyBasket/MyBasketCheckout.asp"
                                      "&PayAuthorizeWait=Yes".format(baseline_link))
            checkout_again = s.post("{}/MyBasket/MyBasketCheckout.asp?ApplyPayment=true".format(baseline_link))
            waiver = s.post("{}/MyBasket/MyBasketProgramLiabilityWaiver.asp".format(baseline_link))
            final_checkout = s.post("{}/MyBasket/MyBasketCheckout.asp".format(baseline_link))
            print("Successfully scheduled for {}.".format(session_code), flush=True)


def run(request_time):
    baseline_link = "https://geegeereg.uottawa.ca/geegeereg"
    j = json.loads(open("info.json").read())
    schedule = j['times']
    s = login(j['login']['barcode'], j['login']['pin'])


    df = DataFrame()

    updated_df = refresh_data(s, df)
    print("df: {}".format(updated_df), flush=True)
    auto_request(s, schedule, request_time, baseline_link)

def main(argv):
    run(argv[1])


def login(barcode, pin):
    baseline_link = "https://geegeereg.uottawa.ca/geegeereg"

    # Create a session
    s = requests.Session()
    # Landing request
    r = s.get('{}/Activities/ActivitiesDetails.asp?aid=316'.format(baseline_link)).content
    while r == b"<BR><BR><strong>L'acc\xc3\xa8s au site est pr\xc3\xa9sentement indisponible. Si vous souhaitez vous inscrire \xc3\xa0 une activit\xc3\xa9, veuillez, s'il vous pla\xc3\xaet, r\xc3\xa9essayer apr\xc3\xa8s 3 h.\r\n<br><br>\r\nAccess to the site is currently unavailable. To register for activities, please try again after 3 am. </strong><BR><BR>Nous \xc3\xa9prouvons pr\xc3\xa9sentement des probl\xc3\xa8mes techniques avec le programme d'inscription en ligne. Nous faisons tout en notre pouvoir pour r\xc3\xa9gler la situation. Veuillez revenir plus tard aujourd'hui pour terminer votre inscription en ligne aux programmes intra-muros et aux activit\xc3\xa9s r\xc3\xa9cr\xc3\xa9atives.\r\n<br><br>":
        time.sleep(10)
        # creating a new session to avoid cookies getting blocked
        s = requests.Session()
        r = s.get('{}/Activities/ActivitiesDetails.asp?aid=316'.format(baseline_link)).content
        print("Page Issues", flush=True)

    # Login Request
    s.post("https://geegeereg.uottawa.ca/geegeereg/MyAccount/MyAccountUserLogin.asp",
           data={'ClientBarcode': barcode, 'AccountPin': pin, 'Enter': 'Login', 'FullPage': 'false'})

    return s

if __name__ == "__main__":
    main(sys.argv)