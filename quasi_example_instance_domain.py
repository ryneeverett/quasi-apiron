from quasi_apiron import Service, JsonEndpoint


class GitHub(Service):
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


service = GitHub(domain='https://api.github.com')
response = service.user(username='defunkt')
print(response)
