from src.searcher import Searcher
from src.args import read_args
from src.exceptions import ResponseError
from src.utilities import print_err


def app():
    (queries, options) = read_args()

    results = []

    # TODO:
    # 1) Make this actually multi-threaded using the multi-threading module... will reduce time to search by a lot!
    # 2) Insert results into the database once they are all processed and
    #    found (if the particular job isn't already in the db, that is)

    for query in queries:
        print("Searching for {}".format(query))
        searcher = Searcher(query, options)

        try:
            for result in searcher.run():
                results.append(result)
        except ResponseError as e:
            print_err("There was an error while searching:\n"
                      "{}".format(e))
            break

        print("Done searching for {}".format(query))

    for result in results:
        print(result)

    exit(0)
