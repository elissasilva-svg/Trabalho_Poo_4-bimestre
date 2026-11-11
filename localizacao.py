'''
class Localizacao:

    def __init__(self, latitude, longitude, endereco):
        self.latitude = latitude
        self.longitude = longitude
        self.endereco = endereco

    def capturarLocalizacao(self):
        print("Localização atual capturada.")

    def obterEndereco(self):
        return self.endereco
'''

class Localizacao:

    def __init__(self, latitude, longitude, endereco):
        self.setLatitude(latitude)
        self.setLongitude(longitude)
        self.setEndereco(endereco)

    def capturarLocalizacao(self):
        print("Localização atual capturada.")

    def obterEndereco(self):
        return self.endereco

    # Getter e setter da latitude
    def getLatitude(self):
        return self.latitude

    def setLatitude(self, latitude):
        if isinstance(latitude, bool) or not isinstance(latitude, (int, float)):
            raise TypeError("A latitude deve ser um número.")

        if latitude < -90 or latitude > 90:
            raise ValueError("A latitude deve estar entre -90 e 90.")

        self.latitude = latitude

    # Getter e setter da longitude
    def getLongitude(self):
        return self.longitude

    def setLongitude(self, longitude):
        if isinstance(longitude, bool) or not isinstance(longitude, (int, float)):
            raise TypeError("A longitude deve ser um número.")

        if longitude < -180 or longitude > 180:
            raise ValueError("A longitude deve estar entre -180 e 180.")

        self.longitude = longitude

    # Getter e setter do endereço
    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        if not isinstance(endereco, str) or not endereco.strip():
            raise ValueError("O endereço não pode estar vazio.")

        self.endereco = endereco.strip()