from locators import ContentLocator


class QuoteContents:
    def __init__(self, quote_section):
        self.quote_section = quote_section

    @property
    def give_quote(self):
        return self.quote_section.select_one(ContentLocator.QUOTE).string

    @property
    def give_author(self):
        return self.quote_section.select_one(ContentLocator.AUTHOR).string

    @property
    def give_tags(self):
        tags = self.quote_section.select(ContentLocator.TAG)
        tags = [tag.string for tag in tags]
        return tags

    @property
    def give_quote_content(self):
        return {
            'name': self.give_quote,
            'author': self.give_author,
            'tags': self.give_tags
        }