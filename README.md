# e-MAPP
e-MAPP - Monitoramento de Atividade e Projetos das Prefeituras

### 1. Criando o ambiente virtual ###

Dentro do folder do projeto, execute o comendo abaixo para criar o ambiente virtual.

```python -m venv venv```

Para ativar o ambiente virtual, execute:

* no Windows

    ```.\venv\Scripts\activate```

* no Mac/Linux

    ```source venv\bin\activate```

Atualize a ferramenta pip:

```python -m pip install --upgrade pip```

Para desativar o ambiente virtual, execute:

```deactivate```

### 2. Criando o banco de dados ###

Execute o comando abaixo no terminal:

```python manage.py migrate```

### 3. Executando a aplicação ###

Execute o comando abaixo no terminal, ele abrirá o navegador.

```python manage.py runserver```