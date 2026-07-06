import os

setores = {
    'api': 20000,
    'hardware': 10000,
    'infra': 30000,
    'gestão': 16000,
    'marketing': 12600,
    'consultoria': 5000,
}

prioridade_1 = ['api', 'hardware']
prioridade_2 = ['infra', 'gestão']
prioridade_3 = ['marketing', 'consultoria']

ordem_prioridades = [prioridade_3, prioridade_2]

def transferir_verba(setor_requerente, valor_requerido):
    for lista in ordem_prioridades:
        for setor in lista:
            if (setor != setor_requerente) and (setores[setor] >= valor_requerido):
                setores[setor] -= valor_requerido
                setores[setor_requerente] += valor_requerido

                return(
                    f"Transação realizada com sucesso!\n"
                    f"O setor '{setor_requerente}' recebeu {valor_requerido}, totalizando em cofre {setores[setor_requerente]}.\n"
                    f"O setor doador, '{setor}', agora tem em cofre {setores[setor]}."
                )
            
    return "Oops!! Não temos temos fundos necessário no confre para esse transição."
        
setor_requerente = 'api'
valor_requerido = 1600
os.system('cls')

transacao = transferir_verba(setor_requerente, valor_requerido)
print(transacao)