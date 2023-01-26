import os

import requests

from apiron import Service, JsonEndpoint

os.environ['APIRON_INSTANTIATED_SERVICES'] = "1"


class GitHub(Service):
    domain = 'https://api.github.com'
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


service = GitHub(session=requests.Session())
response = service.user(username='defunkt')
print(response)
