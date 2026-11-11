from collections import deque


# =========================================================
# 1. LISTAGEM DAS COLEÇÕES OFERECIDAS PELA LINGUAGEM PYTHON
# =========================================================
# list (lista): armazena vários elementos, permite duplicatas
#                e pode ser alterada. Ex.: contatos de confiança.
# tuple (tupla): armazena vários elementos, permite duplicatas,
#                mas não pode ser alterada. Ex.: categorias.
# set (conjunto): armazena elementos sem duplicidade.
#                 Ex.: tipos de alerta.
# dict (dicionário): armazena dados em pares chave: valor.
#                    Ex.: informações de uma emergência.
#
# Coleções do módulo collections incluem:
# deque: fila que permite adicionar/remover nas duas pontas.
# Counter: contabiliza ocorrências de elementos.
# defaultdict: dicionário com valor padrão para chaves novas.
# namedtuple: tupla com campos nomeados.
# (Nesta implementação, deque será importada e utilizada.)


# =========================================================
# 2. EXCEÇÃO PRÓPRIA DO PROJETO
# =========================================================
class ColecaoAlertasVaziaError(Exception):
    """Exceção para quando não há alertas na fila."""
    pass


# =========================================================
# 3. COLEÇÃO PRÓPRIA: ColecaoAlertas
# =========================================================
class ColecaoAlertas:
    """
    Coleção própria do Penhas que organiza alertas em uma fila.
    Utiliza deque internamente (FIFO: primeiro a entrar,
    primeiro a sair).
    """

    def __init__(self):
        self.alertas = deque()

    def adicionar_alerta(self, alerta):
        """Adiciona um alerta ao final da fila."""
        if not isinstance(alerta, dict):
            raise TypeError("O alerta deve ser um dicionário.")

        if "tipo" not in alerta or "data_hora" not in alerta:
            raise ValueError("O alerta precisa conter 'tipo' e 'data_hora'.")

        self.alertas.append(alerta)
        print("Alerta adicionado à fila.")

    def remover_alerta(self):
        """Remove e retorna o alerta mais antigo da fila."""
        try:
            if not self.alertas:
                raise ColecaoAlertasVaziaError(
                    "Não existem alertas pendentes para remover."
                )
            return self.alertas.popleft()

        except ColecaoAlertasVaziaError as erro:
            print(f"Erro: {erro}")
            return None

        finally:
            print("Operação de remoção finalizada.")

    def listar_alertas(self):
        """Retorna os alertas pendentes como uma lista."""
        return list(self.alertas)

    def quantidade_alertas(self):
        """Retorna a quantidade de alertas pendentes."""
        return len(self.alertas)

    def esta_vazia(self):
        """Retorna True se não houver alertas."""
        return not self.alertas


# =========================================================
# 4. DEMONSTRAÇÃO DAS COLEÇÕES NATIVAS DO PYTHON
# =========================================================

# LIST (list): lista de contatos de confiança.
contatos_confianca = ["João", "Ana", "Mariana"]
contatos_confianca.append("Carlos")  # método append adiciona elemento

# TUPLE (tuple): categorias de emergência; tupla é imutável.
categorias_emergencia = (
    "Violência",
    "Perseguição",
    "Assédio",
    "Emergência médica"
)

# SET (set): tipos de alerta sem duplicidade.
tipos_alerta = {"SOS", "Localização", "SOS"}
tipos_alerta.add("Contato de confiança")  # método add adiciona elemento

# DICT (dict): dados de uma emergência em chave e valor.
dados_emergencia = {
    "tipo": "SOS",
    "data_hora": "07/11/2026 16:00",
    "local": "Porto Velho - RO",
    "status": "Pendente"
}
dados_emergencia["status"] = "Em andamento"  # atualiza um valor


# =========================================================
# 5. IMPORTAÇÃO E USO DA COLEÇÃO deque (collections)
# =========================================================
# deque é importada no início: from collections import deque
# append() adiciona um item ao final da fila.
# appendleft() adiciona um item ao início.
# popleft() remove o item do início.
# pop() remove o item do final.

fila_exemplo = deque()
fila_exemplo.append("Alerta de emergência")
fila_exemplo.append("Solicitação de ajuda")
fila_exemplo.appendleft("Alerta prioritário")

print("\n=== DEMONSTRAÇÃO DE deque ===")
print("Fila após append e appendleft:", fila_exemplo)
alerta_inicio = fila_exemplo.popleft()
print("Item removido com popleft():", alerta_inicio)
alerta_fim = fila_exemplo.pop()
print("Item removido com pop():", alerta_fim)
print("Fila restante:", fila_exemplo)


# =========================================================
# 6. EXECUÇÃO E DEMONSTRAÇÃO DA COLEÇÃO PRÓPRIA
# =========================================================
if __name__ == "__main__":
    print("\n=== COLEÇÕES NATIVAS DO PYTHON ===")
    print("list - contatos de confiança:", contatos_confianca)
    print("tuple - categorias de emergência:", categorias_emergencia)
    print("set - tipos de alerta (sem repetição):", tipos_alerta)
    print("dict - dados da emergência:", dados_emergencia)

    print("\n=== COLEÇÃO PRÓPRIA DO PENHAS ===")
    fila_alertas_penhas = ColecaoAlertas()

    fila_alertas_penhas.adicionar_alerta(dados_emergencia)

    segundo_alerta = {
        "tipo": "Solicitação de ajuda",
        "data_hora": "07/11/2026 16:05",
        "local": "Porto Velho - RO",
        "status": "Pendente"
    }
    fila_alertas_penhas.adicionar_alerta(segundo_alerta)

    print("Alertas pendentes:", fila_alertas_penhas.listar_alertas())
    print("Quantidade de alertas:",
          fila_alertas_penhas.quantidade_alertas())

    alerta_removido = fila_alertas_penhas.remover_alerta()
    print("Alerta removido:", alerta_removido)
    print("Quantidade após remoção:",
          fila_alertas_penhas.quantidade_alertas())