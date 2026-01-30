from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)

yc = response.text

soup = BeautifulSoup(yc, "html.parser")
articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:   
    text = article_tag.getText()
    
    link_tag = article_tag.find("a")
    link = link_tag.get("href")

    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score") ]


index = article_upvotes.index(max(article_upvotes))
# print(max(article_upvotes), index)


print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])

















# import lxml
# with open("./bs4-start/website.html", 'r') as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# all_anchors = soup.find_all("a")

# for tag in all_anchors:
#     print(tag.get("href"))

# print(all_anchors)
