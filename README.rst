GitHub Auth for Sentry
======================

An SSO provider for Sentry which enables GitHub organization-restricted authentication.


Setup
-----

Once the package is installed, you'll need to configure the following settings:

::

    GITHUB_APP_ID = ""

    GITHUB_API_SECRET = ""


Optionally you may also specify the domain (for GHE users):

::

    GITHUB_DOMAIN = "api.github.com"

