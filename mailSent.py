import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import sys


# Set Chrome options to run in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Initialize the Chrome webdriver with headless option
driver = webdriver.Chrome(options=chrome_options)
#driver.minimize_window()

collect_url = "https://bet.hkjc.com/racing/pages/odds_wpq.aspx?lang=ch&raceno="

insert_url = "https://hkjc.ngt.hk/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36",
    "Other-Header": "Value"
}

session = requests.Session()

driver.get(collect_url + "1")
time.sleep(5)

try:
    rows = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]').get_attribute("outerHTML")
except selenium.common.exceptions.WebDriverException as e:
    sender_email = 'noreply@frogbid.com'
    receiver_emails = ['frogbidofficial@gmail.com', 'monoget1@gmail.com', 'sahamugdho@gmail.com',
                       'biplobkm87@gmail.com']
    subject = 'HKJC Python'
    body = 'Python Stop. Please Run it Quickly or Clifton Will be very angry!'

    for email in receiver_emails:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        smtp_server = 'mail.frogbid.com'
        smtp_port = 465
        username = 'noreply@frogbid.com'
        password = 'h3m(%@e1165_'

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(username, password)
            server.sendmail(sender_email, email, message.as_string())

    print("Email sent successfully!")
    sys.exit()


# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(rows, 'html.parser')

# Find the parent <div> element
parent_div = soup.find('div', class_='racebg')

# Find all <div> child elements inside the parent <div>
child_divs = parent_div.find_all('div')

# Count the total number of <div> child elements
total_child_divs = len(child_divs)

start_time = time.time()

hour = 8


seconds = hour*4200

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    j = 1

    while j < total_child_divs - 1:

        driver.get(collect_url + str(j))
        time.sleep(2)

        try:
            rows = driver.find_elements(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr')
        except selenium.common.exceptions.WebDriverException as e:
            sender_email = 'noreply@frogbid.com'
            receiver_emails = ['frogbidofficial@gmail.com', 'monoget1@gmail.com', 'sahamugdho@gmail.com', 'biplobkm87@gmail.com']
            subject = 'HKJC Python'
            body = 'Python Stop. Please Run it Quickly or Clifton Will be very angry!'

            for email in receiver_emails:
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = email
                message['Subject'] = subject

                message.attach(MIMEText(body, 'plain'))

                smtp_server = 'mail.frogbid.com'
                smtp_port = 465
                username = 'noreply@frogbid.com'
                password = 'h3m(%@e1165_'

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                    server.login(username, password)
                    server.sendmail(sender_email, email, message.as_string())

            print("Email sent successfully!")
            sys.exit()

        i = 1
        for data in rows:
            i = i + 1

        print('Race ' + str(j) + ' : rows ' + str(i - 1))

        x = 1

        while x < i - 1:

            try:
                sl = driver.find_element(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[1]').text
                horsename = driver.find_element(By.XPATH,
                                                '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[4]').text
                win = driver.find_element(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[5]').text
                place = driver.find_element(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[6]').text

                url = insert_url + "receive_data.php?page_no=" + str(j) + "&sl=" + str(sl) + "&horse_name=" + str(
                    horsename) + "&win=" + str(win) + "&place=" + str(place) + "&rows=" + str(
                    i)  # Replace with your desired URL
            except selenium.common.exceptions.WebDriverException as e:
                print("An error occurred:", e)

                sender_email = 'noreply@frogbid.com'
                receiver_emails = ['frogbidofficial@gmail.com', 'monoget1@gmail.com', 'sahamugdho@gmail.com',
                                   'biplobkm87@gmail.com']
                subject = 'HKJC Python'
                body = 'Python Stop. Please Run it Quickly or Clifton Will be very angry!'

                for email in receiver_emails:
                    message = MIMEMultipart()
                    message['From'] = sender_email
                    message['To'] = email
                    message['Subject'] = subject

                    message.attach(MIMEText(body, 'plain'))

                    smtp_server = 'mail.frogbid.com'
                    smtp_port = 465
                    username = 'noreply@frogbid.com'
                    password = 'h3m(%@e1165_'

                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                        server.login(username, password)
                        server.sendmail(sender_email, email, message.as_string())

                print("Email sent successfully!")
                sys.exit()

            try:
                response = session.get(url, headers=headers)

                if response.status_code == 200:
                    print(response.text + " " + sl)
                else:
                    print(f"Request failed with status code: {response.status_code}")

            except selenium.common.exceptions.WebDriverException as e:
                print("An error occurred:", e)

                sender_email = 'noreply@frogbid.com'
                receiver_emails = ['frogbidofficial@gmail.com', 'monoget1@gmail.com', 'sahamugdho@gmail.com',
                                   'biplobkm87@gmail.com']
                subject = 'HKJC Python'
                body = 'Python Stop. Please Run it Quickly or Clifton Will be very angry!'

                for email in receiver_emails:
                    message = MIMEMultipart()
                    message['From'] = sender_email
                    message['To'] = email
                    message['Subject'] = subject

                    message.attach(MIMEText(body, 'plain'))

                    smtp_server = 'mail.frogbid.com'
                    smtp_port = 465
                    username = 'noreply@frogbid.com'
                    password = 'h3m(%@e1165_'

                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                        server.login(username, password)
                        server.sendmail(sender_email, email, message.as_string())

                print("Email sent successfully!")
                sys.exit()

            x = x + 1

        j = j + 1

    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        subprocess.call(["shutdown", "-f", "-s", "-t", "1"])
        break