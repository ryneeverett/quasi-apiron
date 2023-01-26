import os

from apiron import Service, JsonEndpoint

os.environ['APIRON_INSTANTIATED_SERVICES'] = "1"


class GitHub(Service):
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


service = GitHub(domain='https://api.github.com')
response = service.user(username='defunkt')
print(response)
