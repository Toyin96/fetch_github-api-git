from flask import Flask, render_template, request
from repos.exceptions import GithubExceptions
from repos.api import repos_with_most_stars

app = Flask(__name__)
available_languages = ["Python", "JavaScript", "Ruby", "Java"]


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # code for a GET
        # use the list of all languages
        selected_languages = available_languages
    elif request.method == 'POST':
        # code for a post
        # Use the languages we selected in the request form
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html', selected_languages=selected_languages,
        available_languages=available_languages,
        results=results
    )


@app.errorhandler(GithubExceptions)
def handle_api_error(error):
    return render_template('error.html', message=error)


if __name__ == "__main__":
    app.run()
