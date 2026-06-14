import hashlib

def gerar_hash_bloco(dados, hash_anterior):
    conteudo = dados + hash_anterior
    return hashlib.sha256(conteudo.encode()).hexdigest()

print("\n Teste de Blockchain")

hash_bloco_1 = gerar_hash_bloco("A paga 10 para B", "0000")
hash_bloco_2 = gerar_hash_bloco("B paga 5 para C", hash_bloco_1)
hash_bloco_3 = gerar_hash_bloco("C paga 2 para D", hash_bloco_2)


print(f"Bloco 1: {hash_bloco_1}")
print(f"Bloco 2: {hash_bloco_2}")
print(f"Bloco 3: {hash_bloco_3}")

print("\n Alteração no Bloco 1")

hash_bloco_1_alterado = gerar_hash_bloco("A paga 100 para B", "0000")
print(f"Novo Hash Bloco 1: {hash_bloco_1_alterado}")