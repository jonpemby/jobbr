# import requests
from src.db import DB


db = DB.make()

ranked_words = {
    'python', 'javascript', 'java', 'elixir', 'php', 'postgresql', 'postgres',
    'pgsql', 'sql', 'nosql', 'mongodb', 'android', 'kotlin', 'css', 'scss',
    'sass', 'less', 'webpack', 'pycharm', 'wordpress', 'drupal', 'cms',
    'jetbrains', 'algorithms', 'machine learning', 'learning',
    'artificial intelligence', 'databases', 'database', 'api', 'website',
    'web', 'development', 'developer', 'engineer', 'engineering', 'ide',
    'vim', 'paid vacation', 'dental', 'vision', 'insurance', 'remote',
    'mobile', 'networking', 'network', 'networks', 'unlimited', 'catering',
    'catered meals', 'flexible', 'gym', 'gym membership',
}

# TODO:
# 1) Can use this database of words to train a model on broader spectrum of job listings
# 2) For now just use a simple 'buzzword' database generated above
# words = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').content.decode('utf8')

for word in ranked_words:
    db.run("insert into words (word) values (%(word)s)", {'word': word})
