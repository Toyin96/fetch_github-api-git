class GithubExceptions(Exception):
    """A custom exception class for the project"""

    def __init__(self, status_code):
        """"""
        if status_code == 403:
            message = "Rate limit reached"
        else:
            message = f"status code was {status_code}"
        super().__init__(self, message)
