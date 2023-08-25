# API de cadastro de clientes
## Codificado em Python, Django REST Framework e MySQL
API que faz a conexão entre sistema e database para cadastro de dados de clientes e endereços, além da busca por formulario e filtro no DB

## Acesso ao admin em localhost
http://127.0.0.1:8000/admin/

## Telas do sistema:
![print_menu](https://github.com/Lz-Rod/CRUD-DRF/docs/img/tela-raiz-admin.PNG)
- Raiz do admin - Aqui é possível acessar a tela de cadastro de clientes e endereços.

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/docs/img/tela-vis-cli.PNG)
- Visualização de clientes - Nessa tela são visualizados e acessados todos os clientes cadastrados, e é possivel fazer a busca pelo id ou filtrar pelo nome e cpf, também da acesso ao link para cadastro de novos clientes.

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/docs/img/tela-cad-ed-cli.PNG)
- Cadastro e edição de clientes - Aqui é possivel cadastrar, editar ou apagar os dados dos clientes assim como acessar o link para cadastro de novos endereços.

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/docs/img/tela-vis-end.PNG)
- Visualização de endereços - Nessa tela são visualizados e acessados todos os endereços cadastrados, e é possivel fazer a busca pelo logradouro, cidade, estado ou cep, também da acesso ao link para cadastro de novos endereços.

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/docs/img/tela-cad-ed-end.PNG)
- Cadastro e edição de endereços - Aqui é possivel cadastrar, editar ou apagar os endereços.

## Configuração do DB:
O dump do DB usado está no caminho: https://github.com/Lz-Rod/CRUD-DRF/docs/db

![print_menu](https://github.com/Lz-Rod/CRUD-DRF/docs/img/acesso-db-localhost.PNG)
- O DB está configurado no arquivo settings.py como localhost.