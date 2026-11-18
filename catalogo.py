from musica import Musica

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favoritos = []
        
    def adicionar_musica(self, musica):
        # Validação
        if not isinstance(musica, Musica):
            raise ValueError('É necessário informar um objeto da classe Musica.')
        
        if self.verificar_duplicidade(musica):
            raise ValueError(f'A música "{musica.nome}" já está cadastrada no catálogo.')
        else:
            self.musicas.append(musica)
            self.reproducoes[musica] = 0 # Personalizar da forma que quiser!
        
        print(f'A música "{musica.nome}" foi adicionada ao catálogo com sucesso!')
    
    def verificar_duplicidade(self, musica):
        for musica_verificar in self.musicas:
            if (musica_verificar.nome == musica.nome and 
                musica_verificar.cantor == musica.cantor and 
                musica_verificar.genero == musica.genero and 
                musica_verificar.duracao == musica.duracao and 
                musica_verificar.ano == musica.ano):
                return True
        return False
