import requests
from bs4 import BeautifulSoup


# Make a request to the website
response = requests.get("https://www.python.org/")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant data (adjust as needed)
    data_to_save = soup.get_text()

    # Save data to a text file
    with open('python_website_data.txt', 'w', encoding='utf-8') as file:
        file.write(data_to_save)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
