import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['caah.2000.nickel@gmail.com', 'tiagolachman@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'angelojm01@gmail.com',
        'Teste de python',
        'LOLOLOLOLOLOLOLOLOLOL'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'tiagolachman']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'angelojm01@gmail.com',
            'Teste de python',
            'LOLOLOLOLOLOLOLOLOLOL'
        )
