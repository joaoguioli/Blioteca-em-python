Biblioteca de Livros em Python
Este projeto implementa uma classe Livro para gerenciar livros de uma biblioteca, incluindo funcionalidades como empréstimo e verificação de disponibilidade por ano de publicação.

Estrutura do Projeto
projeto/
├── biblioteca/
│   ├── __init__.py
│   └── livro.py          # Define a classe Livro
├── main.py               # Script principal para testar a classe Livro

Descrição da Classe Livro
Atributos:

titulo (str): título do livro.

autor (str): autor do livro.

ano_publicacao (int): ano de publicação.

disponivel (bool): status de disponibilidade (inicia como True).

Métodos:

__init__: inicializa o livro e adiciona à lista de livros.

__str__: retorna string formatada com informações do livro.

emprestar(): marca o livro como indisponível.

verificar_disponibilidade(ano): método estático que retorna lista de livros disponíveis naquele ano.
