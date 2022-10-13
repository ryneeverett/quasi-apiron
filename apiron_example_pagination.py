import requests
from apiron import Service, Endpoint


class PaginatedEndpoint(Endpoint):

    def __get__(self, *args):
        def paging_caller(*fargs, **kwargs):
            # Use one session for all pages.
            kwargs['session'] = kwargs.get('session', requests.Session())

            response = super(type(self), self).__get__(*args)(*fargs, **kwargs)
            yield from response.json()

            method = kwargs.get('method', 'GET')

            while 'next' in response.links:
                url = response.links['next']['url']
                response = kwargs['session'].request(method, url)
                yield from response.json()

        return paging_caller

    def format_response(self, response):
        return response


class GitHub(Service):
    domain = 'https://api.github.com'
    issues = PaginatedEndpoint(
        path='/repos/{username}/{repo}/issues',
        default_params={'per_page': '5', 'state': 'all'})
    pulls = PaginatedEndpoint(
        path='/repos/{username}/{repo}/pulls',
        default_params={'per_page': '20', 'state': 'all'})


response = GitHub.issues(username='ithaka', repo='apiron')
for issue in response:
    print(issue['title'])
