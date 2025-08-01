
from biblioteca import Livro



livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
Livro("Aprendendo Python", "João Dev", 2020)
Livro("Dominando Python", "Maria Code", 2020)


print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")


ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}:")
for livro in livros_disponiveis_ano:
    print(livro)
