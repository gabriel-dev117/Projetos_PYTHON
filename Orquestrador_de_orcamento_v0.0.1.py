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

setor = 'hardware'            #input("Qual setor está fazendo a requisição? ")
valor =  1500            #int(input("Qual valor está sendo requisitado? "))
os.system('cls')

#-------------------------------------| EMP_P1 |-----------------------------------------
def emp_p1(setor, valor):
    for setor_2 in prioridade_2:
        if (setor_2 != setor) and (setores[setor_2] >= valor):
            setores[setor_2] -= valor
            setores[setor] += valor

            return (
                "A Requisição foi feita pelo setor 1 e está sendo doada pelo setor 2:\n"
                f"{setor}: {setores[setor] - valor} -> {setores[setor]}\n"
                f"{setor_2}: {setores[setor_2] + valor} -> {setores[setor_2]}\n"
                f"Valor Requisitado -> {valor}"
                )

        elif (setor_2 == setor) or (setores[setor_2] < valor):
            continue

        else:    
            return emp_p2(setor, valor)
        
#----------------------------------------------------------------------------------------


#-------------------------------------| EMP_P2 |-----------------------------------------
def emp_p2(setor, valor):
    for setor_3 in prioridade_3:
        if (setor_3 != setor) and (setores[setor_3] >= valor):
            setores[setor_3] -= valor
            setores[setor] += valor
            
            return (
                "A Requisição foi feita pelo setor 2 e está sendo doada pelo setor 3:\n"
                f"{setor}: {setores[setor] - valor} -> {setores[setor]} \n"
                f"{setor_3}: {setores[setor_3] + valor} -> {setores[setor_3]}\n"
                f"Valor Requisitado -> {valor}"
                )
        
        elif (setor_3 == setor) or (setores[setor_3] < valor):
            continue

        else:           
            return emp_p3(setor, valor)
        
#----------------------------------------------------------------------------------------


#-------------------------------------| EMP_P3 |-----------------------------------------
def emp_p3(setor, valor):
    for setor_4 in prioridade_3:
        if (setor_4 != setor) and (setores[setor_4] >= valor):
            setores[setor_4] -= valor
            setores[setor] += valor
            
            return (
                "A doação está sendo pedida ao setor 3:\n"
                f"{setor}: {setores[setor] - valor} -> {setores[setor]}\n"
                f"{setor_4}: {setores[setor_4]+ valor} -> {setores[setor_4]}\n"
                f"Valor Requisitado -> {valor}"
                )

        elif (setor_4 == setor) or (setores[setor_4] < valor):
            continue
 
        else:
            return "Ih rapaz, acabou o money, vai ter que contratar dev júnior\n"
#----------------------------------------------------------------------------------------





#-------------------------------------| PRIORIDADES |-----------------------------------------

def prioridades(setor, valor):
    if setor in prioridade_1:
        print()
        print("O setor que precisa do dinheiro é do setor 1, e o setor solicitado será do setor 2...\n")
        input("Pressione ENTER para continuar...")
        os.system('cls')
      
        return emp_p1(setor, valor)


    elif setor in prioridade_2:
        print()
        print("O setor que precisa do dinheiro é do setor 2, e o setor solicitado será do setor 3...\n")
        input("Pressione ENTER para continuar...")
        os.system('cls')
        
        return emp_p2(setor, valor)

    elif setor in prioridade_3:
        print()
        print("O setor que precisa do dinheiro é do setor 3, e o setor solicitado será também do setor 3...\n")
        input("Pressione ENTER para continuar...")
        os.system('cls')

        return emp_p3(setor, valor)

    else:
        return "Deu algum probleminha aqui ó...\n"


#---------------------------------------------------------------------------------------------

p = prioridades(setor, valor)

print(p)
