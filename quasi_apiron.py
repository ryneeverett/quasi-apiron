import requests
from urllib.parse import urljoin


class Endpoint:
    def __init__(self, path, *args, method='GET', session=None, **kwargs):
        self.method = method
        self.path = path
        self.session = session
        self.args = args
        self.kwargs = kwargs

    def __call__(self, service, *args, **kwargs):
        domain = service._domain or service.domain
        session = service._session or self.session or requests.Session()
        path = self.path.format(*args, **kwargs)

        return session.request(
            self.method, urljoin(domain, path),
            *self.args, *service._args, **self.kwargs, **service._kwargs)


class JsonEndpoint(Endpoint):
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs).json()


class ServiceMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        """ Mask class attributes with bound instance methods. """
        for k, v in namespace.items():
            if isinstance(v, Endpoint):
                def wrapped_method(v):
                    """ Wrap method so v is included in closure. """
                    def method(self, *m_args, **m_kwargs):
                        """ Pass service class instance into __call__. """
                        return v(self, *m_args, **m_kwargs)
                    return method
                namespace[k] = wrapped_method(v)
        return super().__new__(mcs, name, bases, namespace, **kwargs)


class Service(metaclass=ServiceMeta):
    def __init__(self, *args, session=None, domain=None, **kwargs):
        self._domain = domain
        self._session = session
        self._args = args
        self._kwargs = kwargs
