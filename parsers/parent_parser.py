from locators import QuoteLocator
from bs4 import BeautifulSoup
from parsers.child_parser import QuoteContents


class Quote:
    def __init__(self, page):
        self.page = BeautifulSoup(page, 'html.parser')

    @property
    def give_quotes(self):
        quotes = []
        for quote_section in self.page.select(QuoteLocator.QUOTESECTION):
            quote_section = QuoteContents(quote_section)
            quotes.append(quote_section.give_quote_content)
        return quotes
