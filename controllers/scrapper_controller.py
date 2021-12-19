class ScrapperController:
    """Asbtract scraping operations on several platforms"""

    def __init__(self, scrap_limit, scrappers):
        self.scrap_limit = scrap_limit
        self.scrappers = scrappers

    def scrap_datas(self, query_terms):
        """Scrap, filter and format with specified query terms"""
        result = []

        # For each platform
        for scrapper, filter, formater in self.scrappers:
            raw_datas = scrapper.scrap(query_terms, self.scrap_limit)

            for current_data in raw_datas:
                if not filter.is_filtered(current_data):
                    song = formater.to_document(current_data)
                    if song is not None:
                        result.append(song)

        return result
