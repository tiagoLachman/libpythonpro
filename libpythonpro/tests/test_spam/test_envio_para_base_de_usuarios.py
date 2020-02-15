from unittest.mock import Mock
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.tests.test_spam.confitest import *
from libpythonpro.spam.modelos import Usuario
import pytest


@pytest.mark.parametrize(
    'usuarios',
    [
            [
                Usuario(nome='Tiago', email='tiagolachman@gmail.com'),
                Usuario(nome='Mateus', email='mateuslachman@gmail.com')
            ],
            [
                Usuario(nome='Tiago', email='tiagolachman@gmail.com')
            ]
    ]
)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tiagolachman@gmail.com',
        'Salve karai',
        'Salve tiago'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Mateus', email='mateuslachman@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tiagolachman@gmail.com',
        'Salve karai',
        'Salve tiago'
    )
    enviador.enviar.assert_called_once_with(
        'tiagolachman@gmail.com',
        'mateuslachman@gmail.com',
        'Salve karai',
        'Salve tiago'
    )
