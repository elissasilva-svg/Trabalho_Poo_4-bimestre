
'''
from usuario import Usuario


# Relacionamento de herança: ContatoDeConfianca herda de Usuario
class ContatoDeConfianca(Usuario):

    def __init__(self, nome, email, senha, telefone, afinidade):
        super().__init__(nome, email, senha, telefone)
        self.afinidade = afinidade

    def receberAlerta(self):
        print("Alerta de emergência recebido.")

    def confirmarRecebimento(self):
        print("Recebimento do alerta confirmado.")
'''

from usuario import Usuario


# Relacionamento de herança: ContatoDeConfianca herda de Usuario
class ContatoDeConfianca(Usuario):

    def __init__(self, nome, email, senha, telefone, afinidade):
        super().__init__(nome, email, senha, telefone)
        self.setAfinidade(afinidade)

    def receberAlerta(self):
        print("Alerta de emergência recebido.")

    def confirmarRecebimento(self):
        print("Recebimento do alerta confirmado.")

    # Getter da afinidade
    def getAfinidade(self):
        return self.afinidade

    # Setter da afinidade com validação
    def setAfinidade(self, afinidade):
        if not isinstance(afinidade, str) or not afinidade.strip():
            raise ValueError("A afinidade não pode estar vazia.")

        self.afinidade = afinidade.strip()
