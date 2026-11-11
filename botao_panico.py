from localizacao import Localizacao


class BotaoDePanico:

    def __init__(self, dataHora, notificacaoAlerta, status,
                 latitude, longitude, endereco):

        self.dataHora = dataHora
        self.notificacaoAlerta = notificacaoAlerta
        self.status = status

        # Composição: BotaoDePanico possui uma Localizacao
        self.localizacao = Localizacao(latitude, longitude, endereco)

        self.historico = []

    def acionar(self):
        self.status = "Acionado"
        print("Botão de pânico acionado.")

    def cancelar(self):
        self.status = "Cancelado"
        print("Botão de pânico cancelado.")

    def enviarAlerta(self):
        print("Alerta de emergência enviado.")

    def registrarHistorico(self):
        print("Emergência registrada no histórico.")

    def adicionarHistorico(self, historico):
    # Associação entre BotaoDePanico e HistoricoEmergencia
        self.historico.append(historico)