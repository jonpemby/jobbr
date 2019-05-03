import requests
from urllib.parse import quote_plus
from threading import Thread
from src.exceptions import MissingApiKeyError, MissingCxError, NoResultsError, ResponseError
from src.post import Post


class Searcher(Thread):
    def __init__(self, query, params={}):
        super().__init__()

        self.current_query = ''
        self.set_query(query)
        self.index = 1

        self.params = params
        self.results = []

    def get_query(self):
        return self.current_query

    def set_query(self, query):
        self.current_query = quote_plus(query)

    def get_params(self):
        return self.params

    def get_param(self, param):
        return self.params[param]

    def get_cx(self):
        try:
            return self.get_param('cx')
        except ValueError:
            raise MissingCxError("You need a custom search engine ID for this to work")

    def get_api_key(self):
        try:
            return self.get_param('api-key')
        except ValueError:
            raise MissingApiKeyError("You need a Google API key for this to work")

    def get_queries(self):
        try:
            return self.get_param('queries')
        except ValueError:
            return 1

    def run(self):
        for i in range(self.get_queries()):
            response = self.send_query()
            results = response.json()
            if 'error' in results:
                raise ResponseError(results['error'])
            self.push_results(results)
            if i < self.get_queries() and 'nextPage' in results['queries']:
                self.set_page(results['queries']['nextPage'][0]['startIndex'])

        return self.get_results()

    def get_results(self):
        return self.results

    def send_query(self):
        return requests.get("https://www.googleapis.com/customsearch/v1?q={}&key={}&cx={}&startIndex={}&dateRestrict={}"
                            .format(self.get_query(),
                                    self.get_api_key(),
                                    self.get_cx(),
                                    self.get_page(),
                                    self.get_date_range()))

    def push_results(self, results):
        if 'items' not in results:
            raise NoResultsError("No results found for {}".format(self.get_query()))
        for item in results['items']:
            self.results.append(Post(item))

    def set_page(self, index):
        self.index = index

    def get_page(self):
        return self.index

    def get_date_range(self):
        return self.get_param('date-range')
