from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json

url = "https://www.ettoday.net/news/news-list.htm"
response = urlopen(url)

#url = "https://www.ettoday.net/show_roll.php"
#post_data = {"offset":1, "tPage":3}
#response = requests.post(url, data=post_data)
html = BeautifulSoup(response)
#print(response.text)
#html = json.loads(response.text)
part_list_2 = html.find("div", class_="part_list_2")
news_list = part_list_2.find_all("h3")
for news in news_list:
    date = news.find("span", class_="date").text
    tag = news.find("em", class_="tag").text
    news_url = "https://www.ettoday.net" + news.find("a")["href"]
    news_title = news.find("a").text
    print(date, tag, news_url, news_title)