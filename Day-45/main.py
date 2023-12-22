from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')


yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find(class_="titleline").find_all('a')
article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvotes = soup.find_all(name='span', class_='score').getText()

print(article_text, article_link, article_upvotes)