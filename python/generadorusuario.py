import random, string, json
import pandas as dp
import queue
import threading

colita=queue.Queue()

def generar(nombrelibro,numero_codigos):
    i=0
    data = [ {
        "registerCode": "ARCAL72Z1Y220121",
        "used":False
    } ]
    codigo=[('Codigos')]

    df=dp.DataFrame(codigo,columns=['codigo'])
    i=0
    while i!=numero_codigos:
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        x = "ARCM"+x
        data.append({
        "registerCode":x,
        "used":False
    })
        df.loc[i+1]=[x]
        i=i+1

    nombrejson =nombrelibro+".json"
    nombrexls = nombrelibro + ".xlsx"
    with open(nombrejson, 'w') as file:
        json.dump(data, file, indent=4)
    df.to_excel(nombrexls, index=False)
    print("exito con "+nombrelibro)

print("hola")

colita.put(generar("Alumnosmarcelo",4999))
