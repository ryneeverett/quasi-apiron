from quasi_apiron import Service, JsonEndpoint


class GitHub(Service):
    domain = 'https://api.github.com'
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


service = GitHub()
response = service.user(username='defunkt')
print(response)
