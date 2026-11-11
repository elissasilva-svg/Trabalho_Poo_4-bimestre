''''
from usuario import Usuario
from endereco_fixo import EnderecoFixo

# Relacionamento de herança: Usuaria herda de Usuario
class Usuaria(Usuario):

    def __init__(self, nome, email, senha, telefone, cpf, rua, numero, bairro, cep):
        super().__init__(nome, email, senha, telefone)

        self.cpf = cpf
        self.contatos = []
        self.historico = []
        self.localizacao = None
        self.gravacoes = []

    # Composição: Usuaria possui um EnderecoFixo
        self.endereco = EnderecoFixo(rua, numero, bairro, cep)

    def acionarPanico(self):
        print("Botão de pânico acionado.")

    def iniciarGravacao(self):
        print("Gravação de áudio iniciada.")

    def adicionarGravacao(self, gravacao):
        # Associação entre Usuaria e GravacaoAudio
        self.gravacoes.append(gravacao)

    def getCpf(self):
        return self.cpf

    def setLocalizacao(self, localizacao):
        self.localizacao = localizacao
'''

from usuario import Usuario
from endereco_fixo import EnderecoFixo
from localizacao import Localizacao


# Relacionamento de herança: Usuaria herda de Usuario
class Usuaria(Usuario):

    def __init__(self, nome, email, senha, telefone, cpf, rua, numero, bairro, cep):
        super().__init__(nome, email, senha, telefone)

        self.cpf = cpf
        self.contatos = []
        self.historico = []
        self.localizacao = None
        self.gravacoes = []

        # Composição: Usuaria possui um EnderecoFixo
        self.endereco = EnderecoFixo(rua, numero, bairro, cep)

    def acionarPanico(self):
        print("Botão de pânico acionado.")

    def iniciarGravacao(self):
        print("Gravação de áudio iniciada.")

    def adicionarGravacao(self, gravacao):
        # Associação entre Usuaria e GravacaoAudio
        self.gravacoes.append(gravacao)

    # Getter e setter do CPF
    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        cpf = str(cpf).replace(".", "").replace("-", "")

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("O CPF deve conter exatamente 11 números.")

        self.cpf = cpf

    # Getter e setter da localização
    def getLocalizacao(self):
        return self.localizacao

    def setLocalizacao(self, localizacao):
        if localizacao is not None and not isinstance(localizacao, Localizacao):
            raise TypeError("A localização deve ser um objeto da classe Localizacao.")

        self.localizacao = localizacao

    # Getters das listas e do endereço
    def getContatos(self):
        return self.contatos

    def getHistorico(self):
        return self.historico

    def getGravacoes(self):
        return self.gravacoes

    def getEndereco(self):
        return self.endereco
