from bs4 import BeautifulSoup  # Correct import
import requests  # For making HTTP requests

# Request the webpage
url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all <p> tags with the class 'text'
paragraphs = soup.find_all("strong")

# Print the text from each paragraph

file = open("scrapping_data.txt", "a")

for p in paragraphs:
    
    file.write(p.text)
    
    
file.close()

file = open("scrapping_data.txt", "r")
print(file.read())
