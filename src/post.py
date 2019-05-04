from json.encoder import JSONEncoder
from src.db import DB


class Post:
    def __init__(self, result={}):
        self.title = ''
        self.link = ''
        self.snippet = ''

        self.parse_result(result)

    def parse_result(self, result={}):
        if not result:
            return

        self.set_title(result['title'])
        self.set_link(result['link'])
        self.set_snippet(result['snippet'])

    def set_title(self, title):
        self.title = title

    def set_link(self, link):
        self.link = link

    def set_snippet(self, snippet):
        self.snippet = snippet

    def get_title(self):
        return self.title

    def get_link(self):
        return self.link

    def get_snippet(self):
        return self.snippet

    # TODO:
    # Possibly not needed anymore, but still helpful to have for debugging
    # (JSON isn't super terrible to look at)
    def __repr__(self):
        encoder = JSONEncoder()
        return encoder.encode({
            'title': self.get_title(),
            'link': self.get_link(),
            'snippet': self.get_snippet(),
        })

    # TODO:
    # Ideally this should be separated out into a base Model class.
    # More ideally, using an ActiveRecord-esque library. :D
    def save(self):
        DB.make().run("insert into search_results (title, link, snippet) "
                      "select %(title)s title, %(link)s link, %(snippet)s "
                      "where not exists("
                      "select link from search_results where link = %(link)s"
                      ");", {'title': self.get_title(),
                             'link': self.get_link(),
                             'snippet': self.get_snippet()})
