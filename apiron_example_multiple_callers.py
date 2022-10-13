import threading
from apiron import Service, JsonEndpoint


class GitHub(Service):
    repos = JsonEndpoint(path='/repos/{org}')
    issues = JsonEndpoint(path='/repos/{org}/{repo}/issues')
    pulls = JsonEndpoint(path='/repos/{org}/{repo}/pulls')


class GitHubOrg:
    def __init__(self, org, client, domain, auth):
        self.org = org
        self.client = client
        self.domain = domain
        self.auth = auth

    def repos(self):
        with threading.Lock:
            self.client.domain = self.domain
            return self.client.repos(org=self.org, auth=self.auth)

    def issues(self, repo):
        with threading.Lock:
            self.client.domain = self.domain
            return self.client.issues(org=self.org, repo=repo, auth=self.auth)

    def pulls(self, repo):
        with threading.Lock:
            self.client.domain = self.domain
            return self.client.pulls(org=self.org, repo=repo, auth=self.auth)


foo_repo = GitHubOrg('foo', GitHub, 'https://foo.com/api/v3', 'foo_auth_key')
bar_repo = GitHubOrg('bar', GitHub, 'https://bar.com/api/v3', 'bar_auth_key')

print("Example does nothing because these are fake accounts and domains.")
