senhas_validas = ["1234" , "4321", "1111", "2222"]

print(senhas_validas[0]) # imprimir 1234, que é o primeiro item da lista;

n = 0
print(len(senhas_validas)) 
senha_digitada = input('Digite sua senha: ')

while n < len(senhas_validas):
    if senha_digitada == senhas_validas[n]:
        print('Acesso concedido')
        break
    else:
        senha_digitada = input('Senha incorreta, tente novamente: ')
    n = n + 1
    if(n == 4):
    print('Acesso Bloqueado, numero de tentativas máximas esgotado')
