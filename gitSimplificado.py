import hashlib


def simular_git(conteudo_arquivo):
   
    return hashlib.sha1(conteudo_arquivo.encode()).hexdigest()


print("\nTeste de Git")
versao1 = "Olá"
versao2 = "Olá!"

hash_v1 = simular_git(versao1)
hash_v2 = simular_git(versao2)

print(f"Hash Versão 1: {hash_v1}")
print(f"Hash Versão 2: {hash_v2}")
