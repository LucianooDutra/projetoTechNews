# Projeto Tech News!

## Sobre o projeto:

  Projeto, feito em Python, que tem como principal objetivo fazer consultas em notícias sobre tecnologia.

  As notícias foram obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).


# Técnologias utilizadas:

 - Python;
 - Parsel;
 - Requests;
 - Flake8;
 - Pymongo;
 - Pytest;

# Habilidades trabalhadas:

 - terminal interativo do Python;
 - Escrever seus próprios módulos e importá-los em outros códigos;
 - Aplicar técnicas de raspagem de dados;
 - Extrair dados de conteúdo HTML;
 - Armazenar os dados obtidos em um banco de dados - MongoDB;
 - testes com Pytest;

## Instalando as dependências

<details>

  ```json
    # Clone o repositório:
    git clone git@github.com:LucianooDutra/projetoTechNews.git
    
    # Entre no diretório:
    cd projetoTechNews
    
    # Crie o ambiente virtual para o projeto:
    python3 -m venv .venv && source .venv/bin/activate
    
    # Instale as dependências:
    python3 -m pip install -r dev-requirements.txt
  ```
</details>


## Executando os testes

<details>
 <summary><strong>Testes</strong></summary><br />

 Foi utilizado o Pytest para a realização dos testes;

- Para rodar todos os testes:

Para executar todos os testes digite o seguinte comando no terminal a partir da raiz do projeto:

  ```json
    python3 -m pytest
  ```
  
Obs: Nem todos os testes ainda não foram implementados.

</details>


## Funcionalidades

<details>
 <summary><strong>Funcionalidades</strong></summary><br />

##### Popular o banco com notícias:
  Essa funcionalidade busca a quantidade de notícias digitada no site do [_blog da Trybe_](https://blog.betrybe.com), e as salva no banco de dados.

##### Buscar notícias por título:
  Essa funcionalidade busca notícias por título no [_blog da Trybe_](https://blog.betrybe.com)  e as exibem no console, se não existir notícias com o título buscado retorna uma lista vazia.

##### Buscar notícias por data:
  Essa funcionalidade busca notícias por data no [_blog da Trybe_](https://blog.betrybe.com) e as exibem no console, se não existir notícias com a data buscada retorna uma lista vazia.

##### Buscar notícias por categoria:
  Essa funcionalidade busca notícias por categoria no [_blog da Trybe_](https://blog.betrybe.com)  e as exibem no console, se não existir notícias com a categoria buscada retorna uma lista vazia.

##### Listar top 5 categorias:
 Essa funcionalidade busca as 5 primeiras categorias do [_blog da Trybe_](https://blog.betrybe.com), listando em ordem alfabética.

</details>



