# Usandos Testes TDD

Escopo :

Realizar um sistema de cadastro  de clinete para no futuro disparar email de acordo com a idade;
- O cliente deve ter nome, idade, email
- O cliente nao pode ser menor de idade
- O email cadastro deve ser valido 
- O nome do clinete deve ter no minimo 3 caracterers 


Para iniciar instale a biblioteca:

    > pip install pytest

Para executar os teste no arquivo sem mostra os resultados que passaram:

    > pytest -q .\teste_cadastro_Cliente.py

Para execut os teste e mostra os resultados que passaram

    > pytest --verbose  .\teste_cadastro_Cliente.py

