from cliente import Cliente
from cadastroCliente import CadastroCliente


def test_que_cliente_seja_cadastrado_com_sucesso():
    
    cliente = Cliente('Natan',24,'nata.assis@freiregerbasi.adv.br')
    
    cadastro_cliente = CadastroCliente()
    
    reposta = cadastro_cliente.cadastrar_cliente(cliente)
    
    assert "Cadastrado com Sucesso" == reposta
    

def test_que_o_clinte_nao_pode_ser_menor_idade():
    
    cliente = Cliente('Natan',17,'nata.assis@freiregerbasi.adv.br')
    
    cadastro_cliente = CadastroCliente()
    
    reposta = cadastro_cliente.cadastrar_cliente(cliente)
    
    assert "Cliente menor de idade, nao cadastrado" == reposta
    
    
def test_que_email_cadastro_deve_ser_valido():
    
    cliente = Cliente('Natan',24,'nata.assis')
    
    cadastro_cliente = CadastroCliente()
    
    reposta = cadastro_cliente.cadastrar_cliente(cliente)
    
    assert "Email invalido, nao cadastrado" == reposta
    
def test_que_nome_cliente_deve_ter_mais_de_3_caracteres():
    
    cliente = Cliente('Na',24,'nata.assis@freiregerbasi.adv.br')
    
    cadastro_cliente = CadastroCliente()
    
    reposta = cadastro_cliente.cadastrar_cliente(cliente)
    
    assert "Nome invalido, nao cadastrado" == reposta