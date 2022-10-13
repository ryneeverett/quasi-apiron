import requests
from apiron import Service, JsonEndpoint


class GitHub(Service):
    domain = 'https://api.github.com'
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


SESSION = requests.Session()
response = GitHub.user(username='defunkt', session=SESSION)
print(response)
