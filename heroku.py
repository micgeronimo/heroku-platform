import os
import coreapi
from jsonhyperschema_codec import JSONHyperSchemaCodec

class HerokuResource:
    """A Heroku Resource"""
    def __init__(self):
        pass

def convert_to_dicts(c):
    c2 = c.copy()

    if hasattr(c, 'items'):
        for key in c:
            try:
                c2[key] = dict(c2[key])
            except (TypeError, ValueError):
                pass

        return dict(c2)
    else:
        for i, item in enumerate(c):
            try:
                c2[i] = convert_to_dicts(c2[i])
            except (TypeError, ValueError):
                pass

        return c2

class Heroku:
    """A Heroku instance."""
    base_url = 'https://api.heroku.com/'
    schema_url = 'schema'

    def __init__(self, token=None):
        # Default to environment variable, if no token was provided.
        if token is None:
            token = os.environ['HEROKU_TOKEN']

        self.__token = token
        self.client = coreapi.Client(auth=self)
        self.schema = self.load(self.schema_url)

    def load(self, url=None, d=None):

        if not (url or d):
            raise ValueError('Either url or d must be provided to load().')

        # Complete the URL if a relative link was provided.
        if url:
            if not url.startswith('http'):
                url = '{}{}'.format(self.base_url, url)

        if not d:
            try:
                return JSONHyperSchemaCodec().load(bytes=self.client.get(url).read())
            except AttributeError:
                d = self.client.get(url)

        d = convert_to_dicts(d)

        return d

    def get(self, links):
        url = '/'.join(links)
        return self.load(url)

    def action(self, links, **kwargs):
        return self.load(d=self.client.action(self.schema, links, **kwargs))

    def __call__(self, r):
        """Auth handler for Requests."""
        r.headers['Accept'] = "application/vnd.heroku+json; version=3"
        r.headers['Authorization'] = "Bearer {}".format(self.__token)
        return r

    @property
    def apps(self):
        # return heroku.client.
        return self.load('apps')
