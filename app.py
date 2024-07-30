import requests
from parsers.parent_parser import Quote


page = requests.get('https://quotes.toscrape.com/')
quote = Quote(page.content)
# print(quote.give_quotes)
for i in quote.give_quotes:
    print(i)