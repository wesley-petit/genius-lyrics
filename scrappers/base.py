class Scrapper:
    """Implement scrap logic in each platform"""

    def scrap(self, query_terms, scrap_limit):
        """Scrap data

        Keyword arguments:
        query_terms -- search terms
        scrap_limit -- number of document to scrap
        """
        pass


class ScrapperFilter:
    def is_filtered(self, raw_post):
        """If a post is useless or not"""
        return True

    def is_empty_or_null(self, raw_text):
        return raw_text is None or raw_text == ""


class CastScrapperDatas:
    def can_cast(self, raw_post):
        return False

    def to_document(self, raw_post):
        """Cast scrapping datas in a document format"""
        return None

    @classmethod
    def format_text(cls, text):
        return text.replace("\n", "")
