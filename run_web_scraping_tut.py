#Web Scraping
#This is for interfacing directly with a website without needing a browser
#Parsing HTML with beautifulsoup4,   pip install beautifulsoup4
import bs4  #beautiful soup
import requests

res = requests.get('https://www.mtggoldfish.com/price/Duel+Decks+Jace+vs+Chandra/Fireblast#online')
try:
	res.raise_for_status()
except:
	print('could''t get website')
	
soup = bs4.BeautifulSoup(res.text, 'html.parser')

title_selector = '.price-card-name-header-name'
price_css_selector = 'div.price-box:nth-child(2) > div:nth-child(2)'

title = soup.select(title_selector)  #you can find this by enabling HTML inpector F12, then right click and inspect element on what you want to find and right clicking on thehighlighted text and copy and past CSS selector
price = soup.select(price_css_selector)
print("The price of " +title[0].text.strip() +" is $" +price[0].text.strip())