from servico_armazenamento import ServicoArmazenamento


class GravacaoAudio:

    def __init__(self, arquivo, duracao, dataHora):
        self.arquivo = arquivo
        self.duracao = duracao
        self.dataHora = dataHora

        # Associação entre GravacaoAudio e ServicoArmazenamento
        self.armazenamento = None

    def iniciarGravacao(self):
        print("Gravação de áudio iniciada.")

    def encerrarGravacao(self):
        print("Gravação de áudio encerrada.")

    def enviarAudio(self):
        if self.armazenamento is not None:
            self.armazenamento.enviarAudio()
        else:
            print("Nenhum serviço de armazenamento foi definido.")