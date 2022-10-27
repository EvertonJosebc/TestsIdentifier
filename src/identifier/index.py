from src.identifier.identifier import Identifier

def main():
    id = Identifier()

    entrada = input('Digite uma entrada: ')

    if id.identificador(entrada):
        print('A entrada: ', entrada, ' é válida!')
    else:
        print('A entrada: ', entrada, ' é inválida!')

main()