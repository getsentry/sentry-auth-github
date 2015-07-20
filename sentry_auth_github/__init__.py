from __future__ import absolute_import

from sentry.auth import register

from .provider import GitHubOAuth2Provider

register('github', GitHubOAuth2Provider)
