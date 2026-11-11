# --------------------------------------------------------------

# Curso: Técnico em Informática
# Data: 23/09/2026
# Turma: 2º B de Informática
# Disciplina: Programação Orientada a Objetos (POO)
# Projeto: Aplicativo Penhas
# Grupo:
# - Élissa Silva Sales
# - Letícia Vargas de Morais
# - Luize Maria Izel Golin
# - Windelson Vertus

# --------------------------------------------------------------

from usuaria import Usuaria
from contato_confianca import ContatoDeConfianca
from botao_panico import BotaoDePanico
from gravacao_audio import GravacaoAudio
from servico_armazenamento import ServicoArmazenamento
from historico_emergencia import HistoricoEmergencia
from central_emergencia import CentralDeEmergencia190
from localizacao import Localizacao


# Criando uma usuária
usuaria = Usuaria(
    "Maria",
    "maria@email.com",
    "123456",
    "69999999999",
    "12345678900",
    "Rua das Flores",
    123,
    "Centro",
    "76800000"
)

print("=== USUÁRIA ===")
print("Nome:", usuaria.nome)
print("E-mail:", usuaria.email)
print("CPF:", usuaria.getCpf())

# Testando a composição Usuaria -> EnderecoFixo
print("\n=== ENDEREÇO FIXO ===")
print(usuaria.endereco.obterEndereco())
usuaria.endereco.capturarLocalizacaoFixa()

print("\n=== TESTANDO ENDERECO FIXO ===")

endereco = usuaria.getEndereco()

print("Rua:", endereco.getRua())
print("Número:", endereco.getNumero())
print("Bairro:", endereco.getBairro())
print("CEP:", endereco.getCep())

endereco.setRua("Avenida Brasil")
endereco.setNumero(150)
endereco.setBairro("Centro")
endereco.setCep("76801-000")

print("\nNovo endereço:", endereco.obterEndereco())

try:
    endereco.setCep("123")
except ValueError as erro:
    print("Erro:", erro)


# Criando um contato de confiança
contato = ContatoDeConfianca(
    "João",
    "joao@email.com",
    "654321",
    "69988888888",
    "Irmão"
)

print("\n=== TESTANDO GETTERS E SETTERS DO CONTATO ===")

# Consultando a afinidade
print("Afinidade:", contato.getAfinidade())

# Alterando a afinidade
contato.setAfinidade("Amigo")
print("Nova afinidade:", contato.getAfinidade())

# Testando a validação
try:
    contato.setAfinidade("")
except ValueError as erro:
    print("Erro:", erro)

print("\nContato:", contato.nome)
print("Afinidade:", contato.afinidade)

contato.receberAlerta()
contato.confirmarRecebimento()

# Criando um botão de pânico
botao = BotaoDePanico(
    "20/09/2026 19:00",
    "Alerta de emergência",
    "Desativado",
    -8.7612,
    -63.9004,
    "Porto Velho - RO"
)

print("\n=== BOTÃO DE PÂNICO ===")
botao.acionar()

# Testando a composição BotaoDePanico -> Localizacao
print("Endereço da emergência:", botao.localizacao.obterEndereco())
botao.localizacao.capturarLocalizacao()

botao.enviarAlerta()
botao.registrarHistorico()

# Criando uma gravação de áudio
gravacao = GravacaoAudio(
    "emergencia.mp3",
    30,
    "20/09/2026 19:05"
)

# Criando o serviço de armazenamento
armazenamento = ServicoArmazenamento(
    1000,
    30
)

print("\n=== TESTANDO LOCALIZACAO ===")

localizacao_teste = Localizacao(
    -8.7612,
    -63.9004,
    "Porto Velho - RO"
)

# Testando getters
print("Latitude:", localizacao_teste.getLatitude())
print("Longitude:", localizacao_teste.getLongitude())
print("Endereço:", localizacao_teste.getEndereco())

# Testando setters
localizacao_teste.setLatitude(-8.7600)
localizacao_teste.setLongitude(-63.9100)
localizacao_teste.setEndereco("Centro - Porto Velho")

print("Nova latitude:", localizacao_teste.getLatitude())
print("Nova longitude:", localizacao_teste.getLongitude())
print("Novo endereço:", localizacao_teste.getEndereco())

# Testando validação
try:
    localizacao_teste.setLatitude(150)
except ValueError as erro:
    print("Erro:", erro)

# Associação entre GravacaoAudio e ServicoArmazenamento
gravacao.armazenamento = armazenamento

# Associação entre Usuaria e GravacaoAudio
usuaria.adicionarGravacao(gravacao)

print("\n=== GRAVAÇÃO DE ÁUDIO ===")
gravacao.iniciarGravacao()
gravacao.encerrarGravacao()
gravacao.enviarAudio()

print("Quantidade de gravações da usuária:", len(usuaria.gravacoes))

# Criando um registro de emergência
historico = HistoricoEmergencia(
    1,
    "20/09/2026 19:00",
    "Acionamento do botão de pânico"
)

# Associação entre BotaoDePanico e HistoricoEmergencia
botao.adicionarHistorico(historico)

print("\n=== HISTÓRICO DE EMERGÊNCIA ===")
historico.listar()
historico.filtrarPorData(
    "20/09/2026",
    "20/09/2026"
)

print("Quantidade de registros:", len(botao.historico))

# Criando a Central de Emergência 190
central = CentralDeEmergencia190()

print("\n=== CENTRAL DE EMERGÊNCIA ===")
print("Número:", central.numero)

central.realizarLigacao()
central.cancelarLigacao()

print("\n=== TESTANDO GETTERS E SETTERS ===")

# Testando o CPF
print("CPF:", usuaria.getCpf())

usuaria.setCpf("11122233344")
print("Novo CPF:", usuaria.getCpf())

# Testando a localização
localizacao_teste = Localizacao(
    -8.7612,
    -63.9004,
    "Porto Velho - RO"
)

usuaria.setLocalizacao(localizacao_teste)

print("Endereço:", usuaria.getLocalizacao().obterEndereco())

# Testando a validação do CPF
try:
    usuaria.setCpf("123")
except ValueError as erro:
    print("Erro:", erro)


