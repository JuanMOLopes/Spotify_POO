from musica import Musica

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favoritos = []
    
    @staticmethod
    def _normalizar(texto): 
        return texto.strip().lower()
    
    def verificar_duplicidade(self, musica):
        if not isinstance(musica, Musica):
            raise TypeError('É necessário informar um objeto da classe Musica.')
        
        for cadastrada in self.musicas:
            if (self._normalizar(cadastrada.nome) == self._normalizar(musica.nome) and 
                self._normalizar(cadastrada.cantor) == self._normalizar(musica.cantor) and 
                self._normalizar(cadastrada.genero) == self._normalizar(musica.genero) and 
                cadastrada.duracao == musica.duracao and 
                cadastrada.ano == musica.ano):
                return True
        return False
     
    def adicionar_musica(self, musica):
        # Validação
        if not isinstance(musica, Musica):
            raise ValueError('É necessário informar um objeto da classe Musica.')
        
        if self.verificar_duplicidade(musica):
            print(f'Cadastro não realizado! A música "{musica.nome}" já está cadastrada no catálogo.')
            return False
      
        self.musicas.append(musica)
        self.reproducoes[musica] = 0 # Personalizar da forma que quiser!
        
        print(f'A música "{musica.nome}" foi adicionada ao catálogo com sucesso!')
    
    #=========================================================================================#
    
    def remover_musica(self, musica):
        # Verificando se não existe no catálogo
        if musica not in self.musicas:
            return False
    
        # Verificando se a música a ser removida é a música atual
        if self.musica_atual is musica:
            self.musica_atual = None
            
        # Remover dos favoritos
        
        # Removendo de reproduções e da lista
        self.reproducoes.pop(musica, None)
        self.musicas.remove(musica)
        return True
    
    #=========================================================================================#
    
    def reproduzir(self, musica):
        if musica not in self.musicas:
            print("A música não está cadastrada no catálogo!")
            return False
        
        if self.musica_atual is musica:
            print(f"A música {musica.nome} já está sendo reproduzida!")
            return False
        
        self.musica_atual = musica
        self.reproducoes[musica] += 1
        print(f"Reproduzindo: {musica.nome}")
        return True
    
    def pausar(self):
        if self.musica_atual is None:
            print("Nenhuma música está sendo reproduzida!")
            return False
        
        print(f"Reprodução pausada: {self.musica_atual.nome}")
        self.musica_atual = None
        return True

    #=========================================================================================#
    
    def listar_musicas(self):
        for musica in self.musicas:
            print(musica) 
            
    #=========================================================================================#
    
    def favoritar_musica(self, musica):
        if musica not in self.musicas or musica in self.favoritos:
            return False
        self.favoritos.append(musica)
        return True
    
    def desfavoritar_musica(self, musica):
        if musica not in self.favoritos:
            return False
        self.favoritos.remove(musica)
        return True
    
    def listar_favoritas(self):
        for musica in self.favoritos:
            print(musica)
                    
    #=========================================================================================#
            
    def filtrar_por_nome(self, termo):
        termo = self._normalizar(termo)
        
        return [musica for musica in self.musicas 
                if termo in self._normalizar(musica.nome)]
    
    def filtrar_por_cantor(self, termo):
        termo = self._normalizar(termo)
        
        return [musica for musica in self.musicas 
                if termo in self._normalizar(musica.cantor)]
    
    def filtrar_por_genero(self, termo):
        termo = self._normalizar(termo)
        
        return [musica for musica in self.musicas 
                if termo in self._normalizar(musica.genero)]
    
    def filtrar_por_ano(self, ano):
        return [musica for musica in self.musicas 
                if musica.ano == ano]
        
    def filtrar_por_duracao(self, min, max):
        segundos_min = min * 60 
        segundos_max = max * 60
        
        return [musica for musica in self.musicas
                if segundos_min <= musica.duracao <= segundos_max]
        
    #=========================================================================================#

        