import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    # Setup (ligamento do servidor)
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear down (desligamento do servidor)
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()