import requests
from quasi_apiron import Service, Endpoint


class PaginatedEndpoint(Endpoint):
    def __call__(self, *args, **kwargs):
        # Use one session for all pages.
        kwargs['session'] = kwargs.get('session', requests.Session())

        response = super().__call__(*args, **kwargs)
        yield from response.json()

        method = kwargs.get('method', 'GET')

        while 'next' in response.links:
            url = response.links['next']['url']
            response = kwargs['session'].request(method, url)
            yield from response.json()


class GitHub(Service):
    domain = 'https://api.github.com'
    issues = PaginatedEndpoint(
        path='/repos/{username}/{repo}/issues',
        params={'per_page': '5', 'state': 'all'})
    pulls = PaginatedEndpoint(
        path='/repos/{username}/{repo}/pulls',
        params={'per_page': '20', 'state': 'all'})


service = GitHub()
response = service.issues(username='ithaka', repo='apiron')
for issue in response:
    print(issue['title'])
