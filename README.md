# Projeto de Aprendizagem da framework Flask

## Preparação

1. Instale o pyenv e o python 3.7.0
2. Clone o projeto do git 
3. Acesse a raiz do projeto (flask-started)
4. Crie a pasta virtual do ambiente

    ```sh
    python -m venv .venv
    ```

5. Ative o ambiente virtual

    ```sh
    source .venv/bin/activate
    ```

6. Instale os pacotes requeridos do projeto

    ```sh
    pip install -r requirements.txt
    ```

7. Pronto! Para executar em desenvolvimento:

    ```sh
    python manage.py runserver
    ```

## Facilitando ativação com Autoenv

 O Autoenv automatiza a ativação do _.venv_ quando entra dentro da pasta do projeto via terminal.

### Instalação

1. Clone o projeto git <https://github.com/kennethreitz/autoenv> na pasta _.autoenv_
2. No final do arquivo _.bashrc_ cole o trecho de código:

    ```sh
    # Autoenv Configs
    AUTOENV_ENABLE_LEAVE="true"
    AUTOENV_ASSUME_YES="true"
    source ~/.autoenv/activate.sh
    ```

3. Pronto! Quando entrar dentro da raiz do projeto os comandos dentro do arquivo __.env__ serão executados e o ambiente virtual (_.venv_) será ativado automativamente. 

    > "Executado os procedimentos do autoenv, não precisará executar o **item 5** da instalação do projeto."