def criar_perfil(nome, idade):
    return {
        'nome': nome,
        'idade': idade
    }

def validar_idade(idade):
    if idade >= 18:
        return True
    else:
        return False