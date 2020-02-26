from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/58074774?v=4'
    resp_mock.json.return_value = {
        'login': 'Tchucknoia', 'id': 58074774,
        'avatar_url': url
    }
    print("LOL")
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Tchucknoia')
    assert 'https://avatars0.githubusercontent.com/u/58074774?v=4' == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Tchucknoia')
    assert 'https://avatars0.githubusercontent.com/u/58074774?v=4' == url
