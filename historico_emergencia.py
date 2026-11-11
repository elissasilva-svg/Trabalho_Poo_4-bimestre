class HistoricoEmergencia:

    def __init__(self, id, dataHora, tipoDeEmergencia):
        self.id = id
        self.dataHora = dataHora
        self.tipoDeEmergencia = tipoDeEmergencia

    def listar(self):
        print(
            f"Emergência {self.id}: "
            f"{self.tipoDeEmergencia} - {self.dataHora}"
        )

    def filtrarPorData(self, dataInicial, dataFinal):
        print(
            f"Filtrando histórico entre "
            f"{dataInicial} e {dataFinal}."
        )