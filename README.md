# API de cadastro de clientes
## Codificado em Python, Django REST Framework e MySQL
API que faz a conexão entre sistema e database para cadastro de dados de clientes e endereços, além da busca por formulario e filtro no DB

## Acesso ao admin em localhost
http://127.0.0.1:8000/admin/

## Telas do sistema:
![print_menu](https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/img/tela-raiz-admin.png)
- Raiz do admin - Aqui é possível acessar a tela de cadastro de clientes e endereços.  

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/img/tela-vis-cli.png)
- Visualização de clientes - Nessa tela são visualizados e acessados todos os clientes cadastrados, e é possivel fazer a busca pelo id ou filtrar pelo nome e cpf, também da acesso ao link para cadastro de novos clientes.

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/img/tela-cad-ed-cli.png)
- Cadastro e edição de clientes - Aqui é possivel cadastrar, editar ou apagar os dados dos clientes assim como acessar o link para cadastro de novos endereços.  

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/img/tela-vis-end.png)
- Visualização de endereços - Nessa tela são visualizados e acessados todos os endereços cadastrados, e é possivel fazer a busca pelo logradouro, cidade, estado ou cep, também da acesso ao link para cadastro de novos endereços.  

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/img/tela-cad-ed-end.png)
- Cadastro e edição de endereços - Aqui é possivel cadastrar, editar ou apagar os endereços.

## Configuração do DB:
O dump do DB usado está no caminho: https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/db

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/blob/main/docs/img/acesso-db-localhost.png)
- O DB está configurado no arquivo settings.py como localhost.