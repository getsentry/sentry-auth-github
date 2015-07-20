from __future__ import absolute_import, print_function

from django import forms
from sentry.auth.view import AuthView, ConfigureView

from .client import GitHubClient
from .constants import ERR_NO_ORG_ACCESS


class FetchUser(AuthView):
    def __init__(self, client_id, client_secret, org=None, *args, **kwargs):
        self.org = org
        self.client = GitHubClient(client_id, client_secret)
        super(FetchUser, self).__init__(*args, **kwargs)

    def is_valid_org(self, org_id, org_list):
        for o in org_list:
            if str(o['id']) == org_id:
                return True
        return False

    def handle(self, request, helper):
        access_token = helper.fetch_state('data')['access_token']

        if self.org is not None:
            org_list = self.client.get_org_list(access_token)
            if not self.is_valid_org(self.org['id'], org_list):
                return helper.error(ERR_NO_ORG_ACCESS)

        user = self.client.get_user(access_token)

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
