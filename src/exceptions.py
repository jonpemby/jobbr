class JobbrException(Exception):
    pass


class MissingCxError(JobbrException):
    pass


class MissingApiKeyError(JobbrException):
    pass


class NoResultsError(JobbrException):
    pass


class ResponseError(JobbrException):
    def __init__(self, response):
        super().__init__(response['errors'][0]['message'])
