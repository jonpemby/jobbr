from termcolor import colored


def print_help():
    print_header()
    print_opt('queries-per-day', 'number of queries to perform each day')
    exit(0)


def print_header():
    print("{} ({} {})".format(
        colored("jobbr", 'green'),
        colored("Jonathon Pemberton", 'white'),
        colored('<jonpemby@icloud.com>', 'grey')))


def print_opt(option, description):
    print("  {}   {}".format(
        colored('--' + option, 'grey'),
        colored(description, 'white')))


def print_err(message, code=1):
    print(colored(message, 'red'))
    exit(code)
