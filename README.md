# Allegro Spring TECH e-Xperience 2022 - Software Engineer

This is an recruitment assignment repository for Allegro Spring TECH e-Xperience 2022, containing source code of an API app bulit in FastApi Framework getting repos info from desire GitHub user.

The entire application is contained within the `main.py` file, with additional `github_data.py` file containg class used for geting data from GitHub API. All libraries used within app are in `requirements.txt` file

## Installation
* Clone repo
* Create virtual environment `venv` in repo folder by runnig `python3 -m venv venv`
* Activate created virtual enviroment by running 
  * `source venv/bin/activate` on Linux and MacOS
  * `venv\scripts\activate` on Windows
* Install python dependencies related to this project by running `pip3 install -r requirements.txt`

## Run server
To run server paste following to your terminal: `uvicorn main:app`, this creates server on `http://127.0.0.1:8000/` go to that page and you should see default Swagger UI created by FastApi Framework wherefrom you can test API methods and see documentation
![swagger ui image](https://i.ibb.co/HYwbyMB/Screenshot-from-2021-12-24-00-51-06.png)

## API methods
### Get user's repos list with information about repo's name and stars it was given (sorted by number of stars)
#### Exaple:

Curl:
```
`curl -X 'GET' \
  'http://127.0.0.1:8000/repos/admsienkiewicz' \
  -H 'accept: application/json'
```
Request URL:
```
http://127.0.0.1:8000/repos/admsienkiewicz
```
Response: 
```
[
  {
    "name": "allegro",
    "stars": 1
  },
  {
    "name": "assignments",
    "stars": 0
  },
  {
    "name": "autodiff",
    "stars": 0
  },
  {
    "name": "flappy_bird",
    "stars": 0
  },
  {
    "name": "PiastGliwiceChampionshipSeason",
    "stars": 0
  },
  {
    "name": "recipes",
    "stars": 0
  },
  {
    "name": "SimpleYAMLValidator",
    "stars": 0
  },
  {
    "name": "tic_tac_toe",
    "stars": 0
  },
  {
    "name": "ToDoList",
    "stars": 0
  }
]
```

### Get total numbers of stars given to user's repositories

#### Example

Curl: 
```
curl -X 'GET' \
  'http://127.0.0.1:8000/stars/allegro' \
  -H 'accept: application/json'
```
Request URL:
```
http://127.0.0.1:8000/stars/allegro
```
Response:
```
{
  "total number of stars given to this user": 14398
}
```
### Get list of languages used in users repositories with comabain size (in kb's) of repos in that language (SIMPLIFIED VERSION LANGUAGE SIZE AS A REPO SIZE SEE LIMITATIONS PARAGRAPH)
#### Example

Curl:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/languages_stats_simple/allegro' \
  -H 'accept: application/json'
```
Request URL:
```
http://127.0.0.1:8000/languages_stats_simple/allegro
```
Response:

```
[
  {
    "language": "TypeScript",
    "size": 483366
  },
  {
    "language": "Python",
    "size": 381392
  },
  {
    "language": "HTML",
    "size": 281379
  },
  {
    "language": "SCSS",
    "size": 270041
  },
  {
    "language": "Go",
    "size": 94662
  },
  {
    "language": "Java",
    "size": 67550
  },
  {
    "language": "Jupyter Notebook",
    "size": 47078
  },
  {
    "language": "JavaScript",
    "size": 42063
  },
  {
    "language": "Kotlin",
    "size": 2973
  },
  {
    "language": "Groovy",
    "size": 2749
  },
  {
    "language": "C",
    "size": 882
  },
  {
    "language": "Dockerfile",
    "size": 505
  },
  {
    "language": "Swift",
    "size": 383
  },
  {
    "language": "PHP",
    "size": 381
  },
  {
    "language": "Scala",
    "size": 148
  }
]
```
### Get list of languages used in users repositories with comabain size (in bytes) of files in that language

#### Example:

Curl:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/languages_stats/admsienkiewicz' \
  -H 'accept: application/json'
```

Request URL:
```
http://127.0.0.1:8000/languages_stats/admsienkiewicz
```
Response:
```
[
  {
    "language": "Jupyter Notebook",
    "size": 3166355
  },
  {
    "language": "Python",
    "size": 40902
  },
  {
    "language": "JavaScript",
    "size": 15520
  },
  {
    "language": "CSS",
    "size": 9527
  },
  {
    "language": "HTML",
    "size": 6340
  }
]
```

## Limitation 
* GitHub Api which was used in that project allows up to 60 requests in one hour therefore this the maximum number of times created Rest Api would return propper response, when user tries to request more than 60 times in one hour api returns message that API rate limit was exceeded
* Size of the programming language shown in simplified version of get languge stats isnt excaclly size of that language files, it's size of repo where that laguage is "main language" (It is that way couse of limitation mantion above, every repo has it own languages endpoint and its possible to check every language file sizes but it will not work with users with over 60 repos, it will exceeded GitHub API limits therefore applied method returns only repo size and assign it to main language size and is preffered over normal method in bigger collection of repos)

## Posible development in the future
* geting more infos than name and stars from repos
* results paging
* methods optimization 
