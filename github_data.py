import requests


class GithubAPICrawler:

    def __init__(self, username):
        self.username = username

    def request_repos_data(self, page_number):
        return requests.get(f"https://api.github.com/users/{self.username}/repos?simple=yes&per_page=100&page={page_number}").json()

    def catch_error_message(self, repos):
        try:
            if repos["message"] != None:
                message = repos["message"]
        except:
            return None
        return message

    def get_user_repos(self):
        repos_list = []
        page_number = 1
        repos = self.request_repos_data(page_number)
        # if error message apeared return it 
        if self.catch_error_message(repos) != None:
            return {"message" : self.catch_error_message(repos)}
        # loop thorugh pages untill there is an empty page
        while len(repos) > 0:
            for repo in repos:
                # apend to repos list current repo info (name and number of stars)
                repos_list.append({
                    "name": repo["name"],
                    "stars": repo["stargazers_count"]
                })
            # go to the next page
            page_number += 1
            repos = self.request_repos_data(page_number)
        # sort repos_list by stars given in descending order
        repos_list = sorted(
            repos_list, key=lambda item: item["stars"], reverse=True)

        return repos_list

    def get_number_of_stars(self):
        stars_counter = 0
        page_number = 1
        repos = self.request_repos_data(page_number)
        # if error message apeared return it 
        if self.catch_error_message(repos) != None:
            return {"message" : self.catch_error_message(repos)}
        # loop thorugh pages untill there is an empty page
        while len(repos) > 0:
            for repo in repos:
                stars_counter += repo["stargazers_count"]
            # go to the next page
            page_number += 1
            repos = self.request_repos_data(page_number)

        return {"total number of stars given to this user": stars_counter}

    def list_used_languages_simplified(self):
        languages_list = []
        page_number = 1
        repos = self.request_repos_data(page_number)
        # if error message apeared return it 
        if self.catch_error_message(repos) != None:
            return {"message" : self.catch_error_message(repos)}
        # loop thorugh pages untill there is an empty page
        while len(repos) > 0:
            for repo in repos:
                # if language not defined in repo skip that repo
                if repo['language'] == None:
                    continue
                # if language already in the list add to the size value
                if len(languages_list) > 0:
                    listed_language = next(
                        (item for item in languages_list if item["language"] == repo["language"]), None)
                    if listed_language != None:
                        listed_language['size'] += repo['size']
                        continue
                # else add new language to the list with size property
                language = {
                    "language": repo['language'],
                    "size": repo['size'],
                }
                languages_list.append(language)
            # go to next the page
            page_number += 1
            repos = self.request_repos_data(page_number)
        # sort languge list by size in descending order
        languages_list = sorted(
            languages_list, key=lambda item: item["size"], reverse=True)

        return languages_list

    def list_used_languages(self):
        languages_list = []
        page_number = 1
        repos = self.request_repos_data(page_number)
        # if error message apeared return it 
        if self.catch_error_message(repos) != None:
            return {"message" : self.catch_error_message(repos)}
        # loop thorugh pages untill there is an empty page
        while len(repos) > 0:
            for repo in repos:
                # if language__ur not defined in repo skip that repo
                if repo['languages_url'] == None:
                    continue
                # request to language_url 
                languages_dict = requests.get(repo['languages_url']).json()
                repo_languages = list(languages_dict.keys())
                for repo_language in repo_languages: 
                    # if language already in the list add to the size value
                    if len(languages_list) > 0:
                        listed_language = next(
                            (item for item in languages_list if item["language"] == repo_language), None)
                        if listed_language != None:
                            listed_language['size'] += languages_dict[repo_language]
                            continue
                    # else add new language to the list with size property
                    language = {
                        "language": repo_language,
                        "size": languages_dict[repo_language],
                    }
                    languages_list.append(language)
            # go to next the page
            page_number += 1
            repos = self.request_repos_data(page_number)
        # sort languge list by size in descending order
        languages_list = sorted(
            languages_list, key=lambda item: item["size"], reverse=True)

        return languages_list

