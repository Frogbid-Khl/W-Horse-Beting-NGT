import requests
from lxml import html

# Create a session object
session = requests.Session()

# Define headers including User-Agent and Other-Header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Other-Header": "Value"
}

# Update session headers with desired headers
session.headers.update(headers)

# Define the cookies
cookies = {
    'cookie_name': 'cookie_value',
    # Add more cookies if needed
}

# Set the cookies in the session
session.cookies.update(cookies)

# Send a GET request to the webpage
response = session.get("https://bet.hkjc.com/racing/pages/odds_wpq.aspx?lang=ch&raceno=1")

# Check if cookies are enabled
cookies_enabled = session.cookies

# Return the appropriate message
if cookies_enabled:
    message = "Cookies are enabled"
    try:
        if response.status_code == 200:
            tree = html.fromstring(response.text)
            print(response.text)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
else:
    message = "Cookies are not enabled"

# Print or return the message as needed
print(message)

