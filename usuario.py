from abc import ABC
from datetime import datetime, timedelta
import re

try:
    # Exceções compartilhadas com o restante do grupo (Pessoa 4).
    from excecoes import LoginInvalidoError, ContaBloqueadaError
    try:
        from excecoes import UsuarioNaoEncontradoError
    except ImportError:
        class UsuarioNaoEncontradoError(LoginInvalidoError):
            pass
except ImportError:
    # Permite executar usuario.py enquanto o arquivo excecoes.py ainda
    # não foi integrado ao projeto do grupo.
    class LoginInvalidoError(Exception):
        pass

    class ContaBloqueadaError(Exception):
        pass

    class UsuarioNaoEncontradoError(LoginInvalidoError):
        pass


class Usuario(ABC):
    TEMPO_BLOQUEIO = timedelta(minutes=5)
    MAX_TENTATIVAS = 3

    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = None
        self.senha = None
        self.telefone = telefone

        self.tentativas_login = 0
        self.bloqueado_ate = None

        self.setEmail(email)
        self.setSenha(senha)

    def login(self, email, senha):
       
        agora = datetime.now()

        if self.bloqueado_ate is not None:
            if agora < self.bloqueado_ate:
                restante = self.bloqueado_ate - agora
                segundos = max(1, int(restante.total_seconds()))
                raise ContaBloqueadaError(
                    f"Conta temporariamente bloqueada. Tente novamente em "
                    f"aproximadamente {segundos} segundo(s)."
                )
            # O prazo terminou: libera a conta e reinicia a contagem.
            self.bloqueado_ate = None
            self.tentativas_login = 0

        if email != self.email:
            raise UsuarioNaoEncontradoError("Usuário não encontrado. Verifique o e-mail.")

        if senha != self.senha:
            self.tentativas_login += 1

            if self.tentativas_login >= self.MAX_TENTATIVAS:
                self.bloqueado_ate = agora + self.TEMPO_BLOQUEIO
                raise ContaBloqueadaError(
                    "Três tentativas incorretas. A conta foi bloqueada por cinco minutos."
                )

            restantes = self.MAX_TENTATIVAS - self.tentativas_login
            raise LoginInvalidoError(
                f"Senha incorreta! Você ainda tem {restantes} tentativa(s)."
            )

        self.tentativas_login = 0
        self.bloqueado_ate = None
        return True

    def recuperarSenha(self, email=None):
        """Inicia a recuperação se o e-mail informado pertencer ao usuário."""
        if email is None:
            email = self.email

        if email != self.email:
            raise UsuarioNaoEncontradoError(
                "Não existe uma conta cadastrada com esse e-mail."
            )

        print(f"Processo de recuperação de senha iniciado para {self.email}.")
        return True

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        if not isinstance(email, str) or not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email
        ):
            raise ValueError("E-mail inválido. Informe um endereço válido.")

        self.email = email
        # Alterar o e-mail não deve manter tentativas/bloqueio da credencial antiga.
        if hasattr(self, "tentativas_login"):
            self.tentativas_login = 0
            self.bloqueado_ate = None

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        if not isinstance(senha, str) or len(senha) < 6:
            raise ValueError("A senha deve conter pelo menos 6 caracteres.")

        self.senha = senha
        if hasattr(self, "tentativas_login"):
            self.tentativas_login = 0
            self.bloqueado_ate = None
