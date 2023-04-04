<h1 align="center">Employee Manager</h1>

<p align="center">
  <a href="#cenario">Cenario</a> &#xa0; | &#xa0;
  <a href="#requerimentos">Requerimentos</a> &#xa0; | &#xa0;
  <a href="#inicializar">Inicializar</a> &#xa0; | &#xa0;
  <a href="#testar">Testar</a> &#xa0; | &#xa0;
  <a href="https://github.com/vitorleao" target="_blank">Autor</a>
</p>

<br>

# Cenario

Aplicação para gerenciar a informação dos colaboradores, como o nome, endereço de e-mail, e departamento. Ela deverá ter uma API para permitir integrações.

O aplicativo "Manager" deverá conter:

- Um painel no site administrativo do Django, para gerenciar dados de colaboradores e de departamentos
- Uma API Django com métodos para:
  - Listar, adicionar e remover colaboradores
  - Listar, adicionar e remover departamentos
- Um website público em Django ( fora do painel de administração, e sem necessidade de autenticação ) com uma única página contendo um tabela simples listando todos os colaboradores e seus departamentos. A página não precisa utilizar a API criada no item acima e pode ser implementado como uma view.

## Critérios de Aceite

- O código-fonte do projeto deve ser entregue como um repositório no site github.bom, com instruções em um arquivo README.md sobre sua execução;
- Devem existir modelos independentes (porém relacionados) para as entidades de colaboradores, e de departamentos;
- Todos os nomes de variáveis, métodos, objetos, classes e propriedades devem ser escritos em inglês;
- Todos os campos devem seguir tipos de dados coerentes e conter as validações relevantes;
- As boas práticas de codificação do Django e de Python devem ser seguidas;

## Pontos bônus!

Sinta-se livre para adicionar recursos ao projeto se você tiver o tempo e conhecimento para fazê-lo - como aumentar a testabilidade, leitura, gestão de ambiente de desenvolvimento e execução, ou documentação de API. Fique à vontade também para adicionar no arquivo README ou no próprio código comentários sobre suas decisões e abordagens técnicas ao desafio.

## Exemplo da API

### Requisição

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

### Resposta

```
[
  {
    "name": "Jose da Silva",
    "email": "jose.silva@email.com.br",
    "department": "Tester"
  },
  {
    "name": "Jose dos Santos",
    "email": "jose.santos@email.com.br",
    "department": "Developer"
  },
  {
    "name": "Jose Lima",
    "email": "jose.lima@email.com.br",
    "department": "RH"
  }
]
```

# Requerimentos

Antes de começar, você precisa instalar:

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/install/) 
- [Git](https://git-scm.com)
- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/getting-started/)

# Inicializar

Há duas formas de executar o projeto:

Com [Python](https://www.python.org/) através dos seguintes comandos:

```bash
# Clonar o projeto
git clone https://github.com/vitorleao/management_app

# Acessar o diretório e instale os requirementos
cd management_app && pip install -r requirements.txt

# Criar o seu super usuário
cd employee-manager && python manage.py createsuperuser

# Executar o projeto
python manage.py runserver

# Endereço do servidor: <http://localhost:8000>
# Lista com os colaboradores: <http://localhost:8000/employee/>
# Lista com os departamentos: <http://localhost:8000/departament/>
# Sistema administrativo: <http://localhost:8000/manager/>
```

Ou com [Docker](https://docs.docker.com/get-started/) através dos comandos:

```bash
# Clonar o projeto
git clone https://github.com/vitorleao/management_app

# Acessar o diretório
cd employee-manager

# Contruir e baixar recursos para a aplicação
docker-compose up --build -d

# Executar container e Crie o seu super usuário
docker exec -it management_app-web-1 /bin/bash
python3 manage.py createsuperuser

# Endereço do servidor: <http://localhost:8000>
# Lista com os colaboradores: <http://localhost:8000/employee/>
# Lista com os departamentos: <http://localhost:8000/departament/>
# Sistema administrativo: <http://localhost:8000/manager/>
```

# Testar

Para testar, execute os comandos a seguir:

```bash
# Executar todos os testes
python manage.py test
```

<a href="#top">Voltar ao topo da página</a>
