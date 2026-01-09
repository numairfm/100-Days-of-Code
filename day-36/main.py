import requests
import datetime
import random
import os
import dotenv

dotenv.load_dotenv()

now = datetime.datetime.now()
date = now.date()
yesterday = date - datetime.timedelta(days=1)
before_yesterday = yesterday - datetime.timedelta(days=1)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

percentage_threshold = 0.001
percentage_formatted = str(percentage_threshold * 100) + "%"

AVS_KEY = os.environ.get("AVS_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_info():
    news: list
    
    url = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AVS_KEY,
    }
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    
    print(data)
    
    try:
        yesterday_close_price = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
        before_yesterday_close_price = float(data["Time Series (Daily)"][str(before_yesterday)]["4. close"])
    except KeyError:
        two_days_ago = date - datetime.timedelta(days=2)
        three_days_ago = two_days_ago - datetime.timedelta(days=1)
        
        yesterday_close_price = float(data["Time Series (Daily)"][str(two_days_ago)]["4. close"])
        before_yesterday_close_price = float(data["Time Series (Daily)"][str(three_days_ago)]["4. close"])
    
    difference = yesterday_close_price - before_yesterday_close_price
    percent_change = difference / before_yesterday_close_price
    
    if percent_change >= percentage_threshold:
        news = get_news()
        status = "UP"
    elif percent_change <= -percentage_threshold:
        news = get_news()
        status = "DOWN"
    else:
        news = ["Price is normal :)"]
        status = "NORM"
        
    return news, yesterday_close_price, before_yesterday_close_price, status

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news():
    url = "https://newsapi.org/v2/everything"
    
    parameters = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": NEWS_KEY,
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    if len(data) < 1:
        return
    articles = [{item["title"]: item["description"]} for item in data["articles"]]
    return articles
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# I dont have stable signal to test so I will not use twilio.

def send_news(news, status):
    message = ""
    try:
        news_to_send = random.choice(news)
    except IndexError:
        return
    key = list(news_to_send.keys())[0]
    value = news_to_send[list(news_to_send.keys())[0]]
    if status == "UP":
        message = f"""
{STOCK}: 🔺{percentage_formatted}
Headline: {key}
Brief: {value}
        """
    elif status == "DOWN":
        message = f"""
{STOCK}: 🔺-{percentage_formatted}
Headline: {key}
Brief: {value}
        """
    return message


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":
    news, ycp, bycp, status = get_stock_info()
    if status == "UP" or status == "DOWN":
        message = send_news(news, status)
        print(message)
    else:
        print(news)