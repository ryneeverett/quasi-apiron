from apiron import Service, JsonEndpoint


class GitHub(Service):
    domain = 'https://api.github.com'
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


response = GitHub.user(username='defunkt')
print(response)
