
MENOR_IDADE = 18
CHAR_OBRIGATORIO = '@'
MININO_CHAR_NOME = 3


class CadastroCliente:
    def __init__(self):
        self.cliente_cadastrado = []
        
    def cadastrar_cliente(self,cliente):
        
        
        if len(cliente.nome) < MININO_CHAR_NOME:
            return "Nome invalido, nao cadastrado"
        
        if cliente.idade < MENOR_IDADE:
            return "Cliente menor de idade, nao cadastrado"
        
        if not CHAR_OBRIGATORIO in cliente.email:
            return "Email invalido, nao cadastrado"
        
        self.cliente_cadastrado.append(cliente)
        
        if len(self.cliente_cadastrado) > 0:
            return "Cadastrado com Sucesso"