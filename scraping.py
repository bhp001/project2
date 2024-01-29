import requests
from bs4 import BeautifulSoup

def get_latest_python_articles():
    url = "https://www.python.org/"
    
    # Make a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract titles directly into a list
        articles = [article.a.text.strip() for article in soup.select(".blog-widget li")]

        return articles
    else:
        print(f"Request failed with status code: {response.status_code}")
        return []

if __name__ == "__main__":
    python_articles = get_latest_python_articles()

    if python_articles:
        print("New News in the python.org section")
        for index, article in enumerate(python_articles, 1):
            print(f"{index}. {article}")
    else:
        print('No articles found')
