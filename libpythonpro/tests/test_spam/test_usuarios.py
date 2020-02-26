from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.confitest import *

def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Tiago', email='tiagolachman@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Tiago', email='tiagolachman@gmail.com'),
                Usuario(nome='Mateus', email='tiagolachman@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
