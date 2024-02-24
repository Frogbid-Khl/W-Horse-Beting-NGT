from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import subprocess

driver = webdriver.Chrome()
driver.minimize_window()

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

rows = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]').get_attribute("outerHTML")

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

        rows = driver.find_elements(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr')

        i = 1
        for data in rows:
            i = i + 1

        print('Race ' + str(j) + ' : rows ' + str(i - 1))

        x = 1

        while x < i - 1:
            sl = driver.find_element(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[1]').text
            horsename = driver.find_element(By.XPATH,
                                            '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[4]').text
            win = driver.find_element(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[5]').text
            place = driver.find_element(By.XPATH, '//*[@id="wpt' + str(j) + '"]/table/tbody/tr[' + str(x) + ']/td[6]').text

            url = insert_url + "receive_data.php?page_no=" + str(j) + "&sl=" + str(sl) + "&horse_name=" + str(
                horsename) + "&win=" + str(win) + "&place=" + str(place) + "&rows=" + str(
                i)  # Replace with your desired URL

            try:
                response = session.get(url, headers=headers)

                if response.status_code == 200:
                    print(response.text + " " + sl)
                else:
                    print(f"Request failed with status code: {response.status_code}")

            except requests.exceptions.RequestException as e:
                # Error occurred during the request
                print("An error occurred:", e)

            x = x + 1

        j = j + 1

    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        subprocess.call(["shutdown", "-f", "-s", "-t", "1"])
        break