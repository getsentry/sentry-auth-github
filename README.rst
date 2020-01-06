GitHub Auth for Sentry
======================
DEPRECATED: This project now lives in `sentry <https://github.com/getsentry/sentry/tree/master/src/sentry/auth/providers/github>`_

An SSO provider for Sentry which enables GitHub organization-restricted authentication.

Install
-------

::

    $ pip install https://github.com/getsentry/sentry-auth-github/archive/master.zip

Setup
-----

Create a new application under your organization in GitHub with at least the following configured. Example values given use `https://example.sentry.com` for the Sentry URL prefix and should be replaced with whatever hostname you use to access Sentry.

===============================  =====================================================
App Option                       Value
===============================  =====================================================
Homepage URL                     https://example.sentry.com
User authorization callback URL  https://example.sentry.com/auth/sso
Webhook URL                      https://example.sentry.com/extensions/github/webhook/
===============================  =====================================================

========================  ===========================
Permissions               Access
========================  ===========================
Organization permissions  Members - Read-only
User permissions          Email addresses - Read-only
========================  ===========================

Afterwards, you will need to `install the GitHub app`__ on your organization.

Once done, you will need the app's `Client ID` and `Client secret` to add them in your ``sentry.conf.py``:

.. code-block:: python

    GITHUB_APP_ID = "" # client id

    GITHUB_API_SECRET = "" # client secret


Verified email addresses can optionally be required:

.. code-block:: python

    GITHUB_REQUIRE_VERIFIED_EMAIL = True


Optionally you may also specify the domain (for GHE users):

.. code-block:: python

    GITHUB_BASE_DOMAIN = "git.example.com"

    GITHUB_API_DOMAIN = "api.git.example.com"


If Subdomain isolation is disabled in GHE:

.. code-block:: python

    GITHUB_BASE_DOMAIN = "git.example.com"

    GITHUB_API_DOMAIN = "git.example.com/api/v3"

__ https://developer.github.com/apps/installing-github-apps/#installing-your-private-github-app-on-your-repository
