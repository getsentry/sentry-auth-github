from __future__ import absolute_import, print_function

from django import forms
from sentry.auth.view import AuthView, ConfigureView

from .client import GitHubClient
from .constants import ERR_NO_ORG_ACCESS, ERR_MISSING_EMAIL


def _get_name_from_email(email):
    """
    Given an email return a capitalized name. Ex. john.smith@example.com would return John Smith.
    """
    name = email.rsplit('@', 1)[0]
    name = ' '.join([n_part.capitalize() for n_part in name.split('.')])
    return name


class FetchUser(AuthView):
    def __init__(self, client_id, client_secret, org=None, *args, **kwargs):
        self.org = org
        self.client = GitHubClient(client_id, client_secret)
        super(FetchUser, self).__init__(*args, **kwargs)

    def handle(self, request, helper):
        access_token = helper.fetch_state('data')['access_token']

        if self.org is not None:
            if not self.client.is_org_member(access_token, self.org['id']):
                return helper.error(ERR_NO_ORG_ACCESS)

        user = self.client.get_user(access_token)
        # TODO(dcramer): they should be able to enter an email
        if not user.get('email'):
            # User is hiding his email in the profile, so we fetch only the primary one
            emails = self.client.get_emails(access_token)
            emails = [entry['email'] for entry in emails if entry['primary']]
            if not emails:
                return helper.error(ERR_MISSING_EMAIL)
            user['email'] = emails[0]

        # A user hasn't set their name in their Github profile so it isn't populated in the response
        if not user.get('name'):
            user['name'] = _get_name_from_email(user['email'])

        helper.bind_state('user', user)

        return helper.next_step()


class SelectOrganizationForm(forms.Form):
    org = forms.ChoiceField(label='Organization')

    def __init__(self, org_list, *args, **kwargs):
        super(SelectOrganizationForm, self).__init__(*args, **kwargs)

        self.fields['org'].choices = [
            (o['id'], o['login']) for o in org_list
        ]
        self.fields['org'].widget.choices = self.fields['org'].choices


class SelectOrganization(AuthView):
    def __init__(self, client_id, client_secret, *args, **kwargs):
        self.client = GitHubClient(client_id, client_secret)
        super(SelectOrganization, self).__init__(*args, **kwargs)

    def handle(self, request, helper):
        access_token = helper.fetch_state('data')['access_token']
        org_list = self.client.get_org_list(access_token)

        form = SelectOrganizationForm(org_list, request.POST or None)
        if form.is_valid():
            org_id = form.cleaned_data['org']
            org = [o for o in org_list if org_id == str(o['id'])][0]
            helper.bind_state('org', org)
            return helper.next_step()

        return self.respond('sentry_auth_github/select-organization.html', {
            'form': form,
            'org_list': org_list,
        })


class GitHubConfigureView(ConfigureView):
    def dispatch(self, request, organization, auth_provider):
        return self.render('sentry_auth_github/configure.html')
