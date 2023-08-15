#Spript to get top-headlines from a specific county. Using Japan for an example.

import requests

def news(country,api_Key='6a2297b099574b1b9ed2bc269aa1d0d1'):

  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_Key}'
  r = requests.get(url)
  content = r.json()
  articles = content["articles"]
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nTITLE\n',{article['description']}")
  return results  
  
print(news(country="jp",api_Key="6a2297b099574b1b9ed2bc269aa1d0d1"))
  
  




  