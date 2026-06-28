import os

sensor_1 = {'SENSOR': 'Térmico', 'Temperatura': 45, 'Alerta': "Aquecimento"}
sensor_2 = {'SENSOR': 'Bateria', 'Nível': 15, 'Voltagem': 11.2, 'Erro': None}
sensor_3 = {'SENSOR': 'Giroscópio', 'eixo_x': 10, "Alerta": "Aquecimento"}

sensores = []
relatorio = {}

sensores.append(sensor_1)
sensores.append(sensor_2)
sensores.append(sensor_3)

os.system('cls')

for sensor in sensores:
    print('--------------')
    for chave, valor in sensor.items():
        if (valor is None) or (valor == ""):     
            continue
        
        elif relatorio.get(chave) == str(valor) :
            continue
            
        else:
            print(f"{chave} = {valor}")
            relatorio[f'{chave}'] = valor


    # Não usei o set por que achei que do jeito que eu fiz talvez fosse mais prático,
    # mas posso estar errado, então me explique se valeu a pena o que eu fiz e por que.

print('--------------')
print()

# -------------------------------------------------------



