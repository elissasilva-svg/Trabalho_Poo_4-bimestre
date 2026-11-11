'''
class EnderecoFixo:

    def __init__(self, rua, numero, bairro, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep

    def capturarLocalizacaoFixa(self):
        print("Localização fixa do endereço capturada.")

    def obterEndereco(self):
        return f"{self.rua}, {self.numero} - {self.bairro} - CEP: {self.cep}"
'''

class EnderecoFixo:

    def __init__(self, rua, numero, bairro, cep):
        self.setRua(rua)
        self.setNumero(numero)
        self.setBairro(bairro)
        self.setCep(cep)

    def capturarLocalizacaoFixa(self):
        print("Localização fixa do endereço capturada.")

    def obterEndereco(self):
        return f"{self.rua}, {self.numero} - {self.bairro} - CEP: {self.cep}"

    # Getter e setter da rua
    def getRua(self):
        return self.rua

    def setRua(self, rua):
        if not isinstance(rua, str) or not rua.strip():
            raise ValueError("A rua não pode estar vazia.")

        self.rua = rua.strip()

    # Getter e setter do número
    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        if isinstance(numero, bool):
            raise TypeError("O número do endereço é inválido.")

        if isinstance(numero, int):
            if numero <= 0:
                raise ValueError("O número deve ser positivo.")
        elif isinstance(numero, str):
            if not numero.strip():
                raise ValueError("O número não pode estar vazio.")
            numero = numero.strip()
        else:
            raise TypeError("O número deve ser um inteiro ou texto.")

        self.numero = numero

    # Getter e setter do bairro
    def getBairro(self):
        return self.bairro

    def setBairro(self, bairro):
        if not isinstance(bairro, str) or not bairro.strip():
            raise ValueError("O bairro não pode estar vazio.")

        self.bairro = bairro.strip()

    # Getter e setter do CEP
    def getCep(self):
        return self.cep

    def setCep(self, cep):
        cep = str(cep).replace("-", "").replace(".", "").strip()

        if not cep.isdigit() or len(cep) != 8:
            raise ValueError("O CEP deve conter exatamente 8 números.")

        self.cep = cep