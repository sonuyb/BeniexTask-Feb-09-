from urllib.request import urlopen
from urllib.error import URLError, HTTPError
url = input("Enter the URL of the website: ")
 
try:
    with urlopen(url) as response:
        html_content = response.read().decode('utf-8')
        print("Connection successful! HTML content:")
        print(html_content)
except HTTPError as e:
    print(f"HTTP Error: {e}")
except URLError as e:
    print(f"URL Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")