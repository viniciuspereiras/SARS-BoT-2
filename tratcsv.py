import pandas as pd
import json
## script que trata o csv recebido e joga em um json
def tratar_csv():
    data = pd.read_csv("tabela.csv", sep=",")
    print(data.head(2))
    with open('file.json', 'wb') as f:
        data_towrite = data.to_json(orient='records', lines=True)
        f.write(data_towrite.encode('utf-8'))
        # check
    data = pd.read_json("file.json", lines=True)
    print(data.head(2))

# tratar_csv() ## no repo o json foi gerado, mas tera de ter uma func para relizar novos tratamentos


json_handler = open('file.json')
dados = json_handler.readlines()

uf = input("UF:")
## recebe o valor dos estados
if uf == "sp":
    uf_num=0
elif uf == "mg":
    uf_num=1
elif uf == "rs":
    uf_num=2
elif uf == "pr":
    uf_num=3
elif uf == "ba":
    uf_num=4
elif uf == "sc":
    uf_num=5
elif uf == "rj":
    uf_num=6
elif uf == "ce":
    uf_num=7
elif uf == "go":
    uf_num=8
elif uf == "pa":
    uf_num=9
elif uf == "es":
    uf_num=10
elif uf == "pe":
    uf_num=11
elif uf == "df":
    uf_num=12
elif uf == "am":
    uf_num=13
elif uf == "mt":
    uf_num=14
elif uf == "pb":
    uf_num=15
elif uf == "ma":
    uf_num=16
elif uf == "ms":
    uf_num=17
elif uf == "pi":
    uf_num=18
elif uf == "rn":
    uf_num=19
elif uf == "ro":
    uf_num=20
elif uf == "se":
    uf_num=21
elif uf == "al":
    uf_num=22
elif uf == "to":
    uf_num=23
elif uf == "ap":
    uf_num=24
elif uf == "rr":
    uf_num=25
elif uf == "ac":
    uf_num=26

## Pesquisa no json
query="Total de doses aplicadas"

dados_json = json.loads(dados[int(uf_num)])
response = int(dados_json[query]) 
print(f"Resposta: {response}")
## mostra a resposta


