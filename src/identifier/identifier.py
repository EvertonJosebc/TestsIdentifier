class Identifier():
    def caseTestLen(self, valor):
        if len(valor) >= 1 and len(valor) <= 6:
            return True
        return False

    def caseTestInicioLetra(self, valor):
        if valor[0].isalpha():
            return True
        return False
    
    def caseTestLetraseNumeros(self, valor):
        if valor.isalnum():
            return True
        return False

    def identificador(self, valor):
        if self.caseTestLen(valor) and self.caseTestInicioLetra(valor) and self.caseTestLetraseNumeros(valor):
            return True
        else:
            return False