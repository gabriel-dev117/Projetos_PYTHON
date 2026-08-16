import os

itens = [
    'word', 'excel', 'powerpoint',
    'calculadora', 'discord', 'vscode',
    'linha', 'arquivo', 'programa'
]

acoes = {
    'abrir': 'abrir',
    'ligar': 'abrir',
    'iniciar': 'abrir',
    'começar': 'abrir',
    'fechar': 'fechar',
    'finalizar': 'fechar',
    'desligar': 'fechar',
    'parar': 'fechar',
    'repetir': 'colar',
    'colar': 'colar',
    'apagar': 'deletar',
    'deletar': 'deletar',
    'excluir': 'deletar'
}

comandos = {
    'abrirword': '"abrindo o Word..."',
    'abrirexcel': '"abrindo o Excel..."',
    'abrirpowerpoint': '"abrindo o PowerPoint..."',
    'abrircalculadora': '"abrir Calculadora..."',
    'fecharword': '"fechando o Word..."',
    'fecharexcel': '"fechando o Excel..."',
    'fecharpowerpoint': '"fechando o PowerPoint..."',
    'fecharcalculadora': '"fechando a Calculadora..."',
}

os.system('cls')
ordem = input("Diga qual comando quer realizar:  (Ex.: ligar o Spotfy)\n").lower().split()

key_1 = ''
key_2 = ''

try:
    for palavra, chave in zip(ordem, acoes):
        if palavra in acoes:
            key_1 = acoes[palavra]

        if palavra not in acoes:
            raise KeyError(f'"Pedimos desculpas, mas a ação "{palavra}" ainda não está presente nas funções do sistema..."')

    for palavra, chave in zip(ordem, itens):
        if palavra in itens:
            key_2 = palavra

        if palavra not in itens:
            raise NameError(f'"Pedimos desculpas, mas o executável "{palavra}" ainda não está disponível nas funções do sistema..."')

    requisicao = key_1 + key_2
    print(comandos[requisicao])


except KeyError as KE:
    print(KE)

except NameError as NE:
    print(NE)
