import os

""""
O que o sistema precisa fazer: Armazenar as chaves e os dados
sem repetir informação e sem contabilizar valores insignificantes
"""

sensor_1 = {'SENSOR': 'Térmico', 'Temperatura': 45, 'Alerta': "Aquecimento"}
sensor_2 = {'SENSOR': 'Bateria', 'Nível': 15, 'Voltagem': 11.2, 'Erro': None}
sensor_3 = {'SENSOR': 'Giroscópio', 'eixo_x': 10, "Alerta": "Aquecimento"}

sensores = [sensor_1, sensor_2, sensor_3]
registros = []

os.system('cls')
for sensor in sensores:
    sen = {}
    for chave, valor in sensor.items():
        if (sensor[chave] == None) or (sensor[chave] == ""):
            continue

        if sensor[chave] in (sens.get(chave) for sens in registros):
            continue

        else:
            sen[chave]= valor

    registros.append(sen)


for sensor in registros:
    print("--------------------")
    for chave, valor in sensor.items():
        print(f"{chave} = {valor}")
print("--------------------")
