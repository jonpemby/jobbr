from os import environ
from sys import argv
from src.utilities import print_help, print_err


def read_args():
    opts = {
        'queries-per-day': 100,
        'date-range': 'w[1]',
        'api-key': environ['JOBBR_API_KEY'] or '',
        'cx': environ['JOBBR_CX_KEY'] or '',
        'help': False
    }

    queries = []

    for arg in argv[1:]:
        if len(arg) > 2 and arg[0:2] == '--':
            try:
                key_end = arg.index('=')
            except ValueError:
                key_end = len(arg)

            key = arg[2:key_end]

            if key == 'help':
                opts['help'] = True
                break

            value = arg[key_end + 1:]
            opts[key] = value
        else:
            queries.append(arg)

    if opts['help']:
        print_help()

    # TODO:
    # 1) Might need a class to handle this kind of thing
    # if 'vvv' in opts:
    #     opts['verbosity'] = 3
    # elif 'vv' in opts:
    #     opts['verbosity'] = 2
    # elif 'v' in opts:
    #     opts['verbosity'] = 1

    if not queries:
        print_err("No queries specified, please add at least 1 query")

    opts['queries-per-day'] = int(opts['queries-per-day'])
    opts['queries'] = int(opts['queries-per-day'] / len(queries))

    return queries, opts
