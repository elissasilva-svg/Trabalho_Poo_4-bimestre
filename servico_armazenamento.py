class ServicoArmazenamento:

    def __init__(self, capacidade, tamanho):
        self.capacidade = capacidade
        self.tamanho = tamanho

    def salvarAudio(self):
        print("Áudio salvo no armazenamento.")

    def removerAudio(self):
        print("Áudio removido do armazenamento.")

    def enviarAudio(self):
        print("Áudio enviado.")