from quasi_apiron import Service, JsonEndpoint


class GitHub(Service):
    repos = JsonEndpoint(path='/repos/{org}')
    issues = JsonEndpoint(path='/repos/{org}/{repo}/issues')
    pulls = JsonEndpoint(path='/repos/{org}/{repo}/pulls')


class GitHubOrg:
    def __init__(self, org, client, domain, auth):
        self.org = org
        self.client = client

    def repos(self):
        return self.client.repos(org=self.org)

    def issues(self, repo):
        return self.client.issues(org=self.org, repo=repo)

    def pulls(self, repo):
        return self.client.pulls(org=self.org, repo=repo)


foo_repo = GitHubOrg(
    'foo', GitHub(domain='https://foo.com/api/v3', auth='foo_auth_key'))
bar_repo = GitHubOrg(
    'bar', GitHub(domain='https://bar.com/api/v3', auth='bar_auth_key'))

print("Example does nothing because these are fake accounts and domains.")
