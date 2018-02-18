Heroku Platform API Client for Python
=====================================

Creating an OAuth authorization token::

    $ heroku authorizations:create --description "For use with heroku python client"
    Creating OAuth Authorization... done
    Client:      <none>
    ID:          xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    Description: For use with heroku python client
    Scope:       global
    Token:       xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Get a list of all apps your account has access to::

    >>> heroku = Heroku(token='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
    >>> for app in heroku.get(['apps']):
    >>>    print(app['name'])

Get a list of addons for a given app::

    >>> for addon in heroku.get(['apps', 'httpbin-org', 'addons']):
    >>>    print(addon)

    {'actions': {}, 'config_vars': ['SENTRY_DSN'], 'created_at': '2017-03-20T01:40:11Z', 'id': 'bdb9324f-6c86-4403-b045-3e9a242da249', 'name': 'sentry-spherical-26924', 'addon_service': {'id': '75588c33-73c1-4352-a9af-f5b785fd5993', 'name': 'sentry'}, 'plan': {'id': '8f0f5a79-12e5-4718-9737-22d041605f1e', 'name': 'sentry:small29'}, 'app': {'id': 'af5e2f0b-1eeb-492e-a227-8f1ff38b9d50', 'name': 'httpbin-org'}, 'provider_id': '9575', 'state': 'provisioned', 'updated_at': '2017-03-20T01:40:13Z', 'web_url': 'https://addons-sso.heroku.com/apps/xxxxxxxxxxx', 'billed_price': {'cents': 2900, 'unit': 'month'}}

Get formation information for a given app::

    >>> heroku.get(['apps', 'httpbin-org', 'formation'])
    [{'app': {'id': 'af5e2f0b-1eeb-492e-a227-8f1ff38b9d50', 'name': 'httpbin-org'}, 'command': 'gunicorn httpbin:app --log-file - --worker-class="egg:meinheld#gunicorn_worker"', 'created_at': '2017-03-14T20:59:09Z', 'id': 'c7eaae28-3be6-46af-80a8-7d3d69c19de6', 'type': 'web', 'quantity': 4, 'size': 'Performance-M', 'updated_at': '2017-08-31T02:26:53Z'}]

Create a new app::

    >>> heroku.action(['app', 'create'])
    {'acm': False, 'archived_at': None, 'buildpack_provided_description': None, 'build_stack': {'id': 'ee582d3c-717d-4a57-ba5f-8b3a39f3a817', 'name': 'heroku-16'}, 'created_at': '2018-02-18T17:31:19Z', 'id': 'f164aca8-9de9-4e69-a289-6bbb21fa02c5', 'git_url': 'https://git.heroku.com/afternoon-ocean-57686.git', 'maintenance': False, 'name': 'afternoon-ocean-57686', 'owner': {'email': 'kenneth@heroku.com', 'id': 'e7317c6d-e49d-496e-9091-d4a03904d1d6'}, 'region': {'id': '59accabd-516d-4f0e-83e6-6e3757701145', 'name': 'us'}, 'organization': None, 'team': None, 'space': None, 'released_at': '2018-02-18T17:31:19Z', 'repo_size': None, 'slug_size': None, 'stack': {'id': 'ee582d3c-717d-4a57-ba5f-8b3a39f3a817', 'name': 'heroku-16'}, 'updated_at': '2018-02-18T17:31:20Z', 'web_url': 'https://afternoon-ocean-57686.herokuapp.com/'}

Scale an app