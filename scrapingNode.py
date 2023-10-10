##https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python

import requests
import urllib
from requests_html import HTMLSession
from trafilatura import extract
import requests

class Scraper:
    def __init__(self):
        pass
    
    def is_wikipedia_url(self, url):
        return "wikipedia.org" in url  # Check if the URL contains "wikipedia.org"

    def remove_edit_links(self, text):
        text = text.replace("[edit]", "")
        text = text.replace("[Bearbeiten | Quelltext bearbeiten]", "")
        return text

    def fetchTextFromURL(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses (e.g., 404)
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch the URL: {e}")
            return None
        try:
            text = extract(html_content, favor_precision=True)  # Extract main content
        except Exception as e:
            print(f"Failed to extract text: {e}")
            return None

        if self.is_wikipedia_url(url):
            text = self.remove_edit_links(text)

        return text
    def saveExtractedText(self):
        text_file = open("test.txt", "w")
        #write string to file
        text_file.write(self.text)
        
        #close file
        text_file.close()
        print("DOCUMENT CLOSED<<>>> FETCHING SUCCESSFUL")

class GoogleScraper:
    def get_source(self, url):
        try:
            s = HTMLSession()
            response = s.get(url)
            return response
        
        except requests.exceptions.RequestException as e:
            print(e)
            
    def scrape_google(self, query):
        query = urllib.parse.quote_plus(query)
        response = self.get_source("https://www.google.de/search?q=" + query)

        urls = list(response.html.absolute_links)
        googleLinks = (
            'https://www.google.',
            'https://google.',
            'https://webcache.googleusercontent.',
            'http://webcache.googleusercontent.',
            'https://policies.google.',
            'https://support.google.',
            'https://maps.google.',
        )

        for url in urls[:]:
            if url.startswith(googleLinks):
                urls.remove(url)

        return urls


