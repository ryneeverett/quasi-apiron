from apiron import Service, JsonEndpoint


class GitHub(Service):
    user = JsonEndpoint(path='/users/{username}')
    repo = JsonEndpoint(path='/repos/{org}/{repo}')


GitHub.domain = 'https://api.github.com'
response = GitHub.user(username='defunkt')
print(response)
