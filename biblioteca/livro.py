class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Livro: {self.titulo} | {self.autor} | {self.ano_publicacao}'

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]



livro1 = Livro("O Estagiário", "Gustavo Guanabara", 2018)
livro2 = Livro("Programação", "John Cena", 2020)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

print(livro1)
print(livro2)

print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")
