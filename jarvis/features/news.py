import requests
import json
from jarvis.config import config

apikey = config.news_api_key
def get_news():
    url = f'http://newsapi.org/v2/top-headlines?country=id&apiKey={apikey}'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return f'http://newsapi.org/v2/top-headlines?country=id&apiKey={apikey}'