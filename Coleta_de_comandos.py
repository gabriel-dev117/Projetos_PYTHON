import os

acoes = [
    'iniciar', 'começar', 'abrir', 
    'fechar', 'finalizar', 'parar',
    'copiar', 'colar', 'recortar',
    'apagar', 'deletar', 'excluir'
]
acoes = set(acoes)

itens = [
    'word', 'excel', 'powerpoint',
    'calculadora', 'discord', 'vscode',
    'linha', 'arquivo', 'programa'
]
itens = set(itens)


comandos = {
    'abrirword': 'abrindo o Word...',
    'abrirexcel': 'abrindo o Excel...',
    'abrirpowerpoint': 'abrindo o PowerPoint...',
    'abrircalculadora': 'abrir Calculadora...',
    'fecharword': 'fechando o Word...',
    'fecharexcel': 'fechando o Excel...',
    'fecharpowerpoint': 'fechando o PowerPoint...',
    'fecharcalculadora': 'fechando a Calculadora...',
}


user = input("Diga o que deseja: ").lower().split()
requisicao = set()

for palavra in user:
    requisicao.add(palavra)

chave1 = acoes & requisicao
chave2 = itens & requisicao

chave3 = str(*chave1)
chave4 = str(*chave2)

chave_final = (chave3 + chave4)

try:
    os.system('cls')
    print(comandos[f'{chave_final}'])

except KeyError:
    os.system('cls')
    print("O comando não existe")

