GitHub Auth for Sentry
======================

An SSO provider for Sentry which enables GitHub organization-restricted authentication.


Setup
-----

Once the package is installed, you'll need to configure the following settings:

::

    GITHUB_APP_ID = ""

    GITHUB_API_SECRET = ""

Verified email addresses can optionally be required:

::

    GITHUB_REQUIRE_VERIFIED_EMAIL = True

Optionally you may also specify the domain (for GHE users):

::

    GITHUB_BASE_DOMAIN = "git.example.com"

    GITHUB_API_DOMAIN = "api.git.example.com"


If Subdomain isolation is disabled in GHE:

::

    GITHUB_BASE_DOMAIN = "git.example.com"

    GITHUB_API_DOMAIN = "git.example.com/api/v3"
