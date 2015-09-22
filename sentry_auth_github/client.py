from __future__ import absolute_import, print_function

from requests.exceptions import RequestException
from sentry import http
from sentry.utils import json
from urllib import urlencode

from .constants import DOMAIN


class GitHubApiError(Exception):
    def __init__(self, message='', status=None):
        super(GitHubApiError, self).__init__(message)
        self.status = status


class GitHubClient(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.http = http.build_session()

    def _request(self, path, access_token):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        headers = {
            'Authorization': 'token {0}'.format(access_token),
        }

        try:
            req = self.http.get('https://{0}/{1}'.format(DOMAIN, path.lstrip('/')),
                params=params,
                headers=headers,
            )
        except RequestException as e:
            raise GitHubApiError(unicode(e), status=e.status_code)
        return json.loads(req.content)

    def get_org_list(self, access_token):
        return self._request('/user/orgs', access_token)

    def get_user(self, access_token):
        return self._request('/user', access_token)

    def get_user_emails(self, access_token):
        return self._request('/user/emails', access_token)

    def is_org_member(self, access_token, org_id):
        org_list = self.get_org_list(access_token)
        org_id = str(org_id)
        for o in org_list:
            if str(o['id']) == org_id:
                return True
        return False
