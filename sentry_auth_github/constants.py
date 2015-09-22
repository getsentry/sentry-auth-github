from __future__ import absolute_import, print_function

from django.conf import settings

CLIENT_ID = getattr(settings, 'GITHUB_APP_ID', None)

CLIENT_SECRET = getattr(settings, 'GITHUB_API_SECRET', None)

ERR_NO_ORG_ACCESS = 'You do not have access to the required GitHub organization.'

ERR_MISSING_EMAIL = 'We were unable to determine the email address of your GitHub account.'

ERR_MISSING_NAME = 'We were unable to determine your name from your GitHub account.'

# we request repo as we share scopes with the other GitHub integration
SCOPE = 'user:email,read:org,repo'

# deprecated please use GITHUB_API_DOMAIN and GITHUB_BASE_DOMAIN
DOMAIN = getattr(settings, 'GITHUB_DOMAIN', 'api.github.com')

BASE_DOMAIN = getattr(settings, 'GITHUB_BASE_DOMAIN', 'github.com')
API_DOMAIN = getattr(settings, 'GITHUB_API_DOMAIN', DOMAIN)

ACCESS_TOKEN_URL = 'https://{0}/login/oauth/access_token'.format(BASE_DOMAIN)
AUTHORIZE_URL = 'https://{0}/login/oauth/authorize'.format(BASE_DOMAIN)
