import sys
import requests
from typing import Optional, Union, List
from algoliasearch.exceptions import RequestException
# at first sight, I was willing to inherit from
# algoliasearch.configs.Config
# Using the same mecanics, I had troubles querying status.algolia.com
# without error, even when using an HostsCollection containing only
# this URL.
# As a shortcut, I'm directly using the requests module here.

# Python 3
if sys.version_info >= (3, 0):
    from urllib.parse import quote
else:
    from urllib import quote


class HealthClient(object):
    '''
    Designed to query API availability related facts,
    like status or incidents
    '''
    
    def __init__(self, config):
        # type: (dict) -> None
        self._config = config


    def try_http_query(self, relative_url):
        # type: (str) -> dict
        '''
        Wraps operations around the 
        `Requests` library and eventually
        translates its exceptions
        '''
        try:
            r = requests.get(
                "{}{}".format(
                    self._config['host'],
                    relative_url
                )
            )
            if r.status_code != 200:
                raise RequestException(r.text, None)
            return r.json()

        except requests.exceptions.RequestException as e:
            raise RequestException(str(e), None)


    def status(self, *servers):
        # type: (*str) -> dict
        '''
        get current API status.
        '''

        if len(servers):
            print(servers)
            servers_list = ",".join((quote(s) for s in servers))
            return self.try_http_query('/1/status/{}'.format(servers_list))
        else:
            return self.try_http_query('/1/status')


    def incidents(self, *servers):
        # type: (*str) -> dict
        '''
        get incidents
        '''

        if len(servers):
            servers_list = ",".join((quote(s) for s in servers))
            return self.try_http_query('/1/incidents/{}'.format(servers_list))
        else:
            return self.try_http_query('/1/incidents')
    
    
    @staticmethod
    def create(app_id=None, api_key=None):
        config = {
            'host': 'https://status.algolia.com'

        }
        return HealthClient.create_with_config(config)

    @staticmethod
    def create_with_config(config):
        # type: (dict) -> HealthClient
        client = HealthClient(config)
        # here we could manage asynchronous client
        # if is_async_available():
        # from ... import HeathClientAsync
        #     return HeathClientAsync(..
        return client


if __name__ == '__main__':
    # quick testing
    h = HealthClient.create('', '')
    print(h.status())
    print(h.status("c10-eu", "c4-eu"))
    print(h.incidents())
    print(h.incidents("c10-eu", "c4-eu"))
