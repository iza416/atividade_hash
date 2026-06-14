
import hashlib
import os


usuarios = {}

def cadastrar_usuario(usuario, senha):
    
    salt = os.urandom(16) 
    
    
    hash_senha = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, 100000)
    
    
    usuarios[usuario] = {"salt": salt, "hash": hash_senha}
    print(f" Usuário '{usuario}' cadastrado com sucesso!")

def fazer_login(usuario, senha_digitada):
    if usuario in usuarios:
        dados = usuarios[usuario]
        salt = dados["salt"]
        hash_salvo = dados["hash"]
        
        
        novo_hash = hashlib.pbkdf2_hmac("sha256", senha_digitada.encode(), salt, 100000)
        
        
        if novo_hash == hash_salvo:
            return "Login efetuado com sucesso!"
        else:
            return " Senha incorreta!"
    return " Usuário não encontrado!"


print("Teste")
cadastrar_usuario("joana", "senhaBoa123")
print(f"Login Correto: {fazer_login('joana', 'senhaBoa123')}")
print(f"Login Incorreto: {fazer_login('joana', 'errada123')}")