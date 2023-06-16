class Cliente:
    def __init__(self, nome, dataNascimento, endereco):
        self.__nome = nome
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self.listaClientes = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def dataNascimento(self):
        return self.__dataNascimneto

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimneto = dataNascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def addCliente(self, objetoCliente):
        self.__listaContas += [objetoCliente]

    def retornaDadosCliente(self):
        return f"Nome:{self.nome}\nData de nascimento: {self.dataNascimento}\nEndereço: {self.endereco}\n"

class PessoaFisica(Cliente):
    def __init__(self, n, dn, e, CPF):
        super().__init__(n, dn, e)
        self.CPF = CPF

    @property
    def CPF(self):
        return self.__CPF

    def retornaDadosCliente(self):
        return super().retornaDadosCliente + f"CPF: {self.CPF}\n\n"

class PessoaJuridica(Cliente):
    def __init__(self, n, dn, e, CNPJ):
        super().__init__(n, dn, e)
        self.CNPJ = CNPJ

    @property
    def CNPJ(self):
        return self.__CNPJ

    def retornaDadosCliente(self):
        return super().retornaDadosCliente + f"CNPJ: {self.CNPJ} \n\n"