import pytest
from src.identifier.identifier import Identifier

obj = Identifier()

class TestsIdentifier:

    def test1NumberLetterValid(self):
        print('Entrada com Números e Letras com quantidade permitida')
        entrada = "a19763"
        esperado = True
        obtido = obj.identificador(entrada)

        assert obtido == esperado
    
    def teste2OneLetter(self):
        print('Entrada com uma letra')
        entrada = "a"
        esperado = True
        obtido = obj.identificador(entrada)

        assert obtido == esperado
  
    def teste3EntryNull(self):
        print('Entrada sem caracteres')
        entrada = ""
        esperado = False
        obtido = obj.identificador(entrada)

        assert obtido == esperado

    def teste4InitNumber(self):
        print('Entrada iniciada com número')
        entrada = "3"
        esperado = False
        obtido = obj.identificador(entrada)

        assert obtido == esperado

    def teste5EntryVeryLong(self):
        print('Entrada de caracteres mais longa que o esperado')
        entrada = "a123456"
        esperado = False
        obtido = obj.identificador(entrada)

        assert obtido == esperado

    def teste6SpecialCharacteres(self):
        entrada = "b#4%S"
        esperado = False
        obtido = obj.identificador(entrada)

        assert obtido == esperado
