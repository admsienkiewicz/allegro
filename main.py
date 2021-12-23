from fastapi import FastAPI
from starlette.responses import RedirectResponse
from github_data import GithubAPICrawler

app = FastAPI()

@app.get("/")
async def root():
    # redirect to swaggerUI within docs page
    response = RedirectResponse(url="/docs")
    return response

@app.get("/repos/{username}")
async def repos(username : str):
    gh_crawler = GithubAPICrawler(username)
    return gh_crawler.get_user_repos()

@app.get("/stars/{username}")
async def stars(username : str):
    gh_crawler = GithubAPICrawler(username)
    return gh_crawler.get_number_of_stars()

@app.get("/languages_stats/{username}")
async def language_stats(username : str):
    gh_crawler = GithubAPICrawler(username)
    return gh_crawler.list_used_languages()