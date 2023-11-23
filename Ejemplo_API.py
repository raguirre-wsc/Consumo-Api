import requests
import json
import pprint
import pandas
import xlsxwriter
import chardet

#CREAMOS DICCIONARIO QUE ALMACENARA LOS DATOS
poke_dict= {'name':[],
            'hp': [],
            'attack': [],
            'defense': [],
            'special-attack': [],
            'special-defense': [],
            'speed': []
    }

#HACEMOS LAS CONSULTAS A LA API
for k in range(1,20,3):
    #ENDPOINT API
    url= f"https://pokeapi.co/api/v2/pokemon/{k}/"

    #REQUEST - JSON
    request=requests.get(url).json()

    #ASIGNAMOS LOS DATOS A NUESTRO DICCIONARIO
    name= poke_dict["name"].append(request["name"])
    hp= poke_dict["hp"].append(request["stats"][0]["base_stat"])
    attack= poke_dict["attack"].append(request["stats"][1]["base_stat"])
    defense= poke_dict["defense"].append(request["stats"][2]["base_stat"])
    special_attack= poke_dict["special-attack"].append(request["stats"][3]["base_stat"])
    special_defense= poke_dict["special-defense"].append(request["stats"][4]["base_stat"])
    speed= poke_dict["speed"].append(request["stats"][5]["base_stat"])

#CREAMOS DATAFRAME
df=pandas.DataFrame.from_dict(poke_dict)

#IMPRIMIMOS EN UN EXCEL
writer = pandas.ExcelWriter(r'C:\Users\rodriaguirre\Desktop\Ej API Pokemon\PokeDB.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='PokeDB', index=False)
writer.save()








