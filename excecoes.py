
class LoginInvalidoError(Exception):
    """Lançada quando usuário ou senha estão incorretos."""

    def __init__(self, mensagem="Login inválido: usuário ou senha incorretos."):
        super().__init__(mensagem)


class ContaBloqueadaError(Exception):
   

    def __init__(self, mensagem="Conta bloqueada."):
        super().__init__(mensagem)


class ArmazenamentoCheioError(Exception):
    

    def __init__(self, mensagem="Armazenamento cheio: não há espaço disponível."):
        super().__init__(mensagem)


class DadosInvalidosError(Exception):
    

    def __init__(self, mensagem="Dados inválidos."):
        super().__init__(mensagem)
