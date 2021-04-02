import requests
from repos.exceptions import GithubExceptions
from repos.models import GithubRepo


GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, min_stars):
    """
    creates a query string for the github api based on the language
    and number of min_stars that we provide
    :return: query
    """

    query = " ".join(f"language: {language.strip()}" for language in languages)
    query = query + f" stars:>{min_stars}"
    return query


def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    print(parameters)
    response = requests.get(GITHUB_API_URL, parameters)

    if response.status_code != 200:
        raise GithubExceptions(response.status_code)

    response_json = response.json()
    items = response_json["items"]
    return [GithubRepo(item["name"], item["languages"], item["stargazers_count"])
            for item in items]
