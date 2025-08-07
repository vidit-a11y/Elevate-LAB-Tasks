import requests
from bs4 import BeautifulSoup
import datetime

URL = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN%3Aen"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
def scrape_headlines():
    print("Fetching the webpage")
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    headline_tags = soup.find_all('a', class_='gPFEn')
    
    if not headline_tags:
        print("Could not find any headline tags. The website's HTML structure may have changed.")
        return

    headlines = []
    for tag in headline_tags:
        headline_text = tag.text.strip()
        if headline_text:
            headlines.append(headline_text)

    if headlines:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"headlines_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            print(f"\n Saving {len(headlines)} headlines to {filename}...")
            f.write(f"Top Headlines from Google News India - Scraped on {timestamp}\n")
            f.write("="*60 + "\n\n")
            for i, headline in enumerate(headlines, 1):
                f.write(f"{i}. {headline}\n")
        
        print("\nScraping complete!")
        print(f"File '{filename}' created successfully in your current directory.")
    else:
        print("No headlines were extracted, even though tags were found. Check the content.")

if __name__ == "__main__":
    scrape_headlines()
