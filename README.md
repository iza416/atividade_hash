Explicação solicitada

No arquivo senhas, utilizei a função PBKDF2 combinada com um salt aleatório. 
Realizei o cadastro da usuário: joana e seu  login, testando um correto e outro incorreto. 

No arquivo gitSimplificado, demonstrei que uma mudança pequena altera totalmente o hash. Por exemplo, no meu caso escrevi: olá e olá! 

RESULTADO:
hash1: 528e38504016437b6f206506af055091016719a4
hash2: d3a0420c5887c1d348c670f00ca38f3b622815ae

No arquivo de blockchain, criei três blocos onde cada um depende da hash do bloco anterior.
Se houver uma alteração no primeiro bloco (como fiz mudando o valor de 10 para 100), o hash dele muda completamente.
