import random, string, json
import pandas as dp
import queue
import threading

colita=queue.Queue()

def generar(codigolibro,nombrelibro,numero_codigos):
    i=0
    data = [ {
        "book":"ra",
        "code":"ARCAAPTUC8I210121"
    } ]
    codigo=[('Codigos')]

    df=dp.DataFrame(codigo,columns=['codigo'])
    i=0
    while i!=numero_codigos:
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        x = "ARCR"+x
        data.append({
        "book":codigolibro,
        "code":x
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

colita.put(generar("6060dc7aaac831ddfc81a30c","1Material Lúdico",999))
colita.put(generar("6060dc7aaac831ddfc81a301","2Educación Temprana",999))
colita.put(generar("6060dc7aaac831ddfc81a317","3Taller Expresión Artística",999))
colita.put(generar("6060dc7aaac831ddfc81a300","4Matemática Avanzada",999))
colita.put(generar("6060dc7aaac831ddfc81a302","5Ciencia y Tecnología",999))
colita.put(generar("6060dc7aaac831ddfc81a303","6Comunicación",999))
colita.put(generar("6060dc7aaac831ddfc81a304","7Taller Grafo Motrocidad",999))
colita.put(generar("6060dc7aaac831ddfc81a305","8Matemática",999))
colita.put(generar("6060dc7aaac831ddfc81a306","9Material Lúdico",999))
colita.put(generar("6060dc7aaac831ddfc81a307","10Persona Social y Religión",999))
colita.put(generar("6060dc7aaac831ddfc81a308","11Taller Grafo Motrocidad",999))
colita.put(generar("6060dc7aaac831ddfc81a309","12Taller Expresion Plástica",999))
colita.put(generar("6060dc7aaac831ddfc81a319","13Taller Grafo Motrocidad",999))
colita.put(generar("6060dc7aaac831ddfc81a31a","14Taller Expresion Plástica",999))
colita.put(generar("6060dc7aaac831ddfc81a30d","15Comunicación Avanzada",999))
colita.put(generar("6060dc7aaac831ddfc81a30e","16Matemática Avanzada",999))
colita.put(generar("6060dc7aaac831ddfc81a30f","17Ciencia y Tecnología",999))
colita.put(generar("6060dc7aaac831ddfc81a311","18Matemática",999))
colita.put(generar("6060dc7aaac831ddfc81a312","19Comunicación",999))
colita.put(generar("6060dc7aaac831ddfc81a313","20Material Lúdico",999))
colita.put(generar("6060dc7aaac831ddfc81a314","21Persona Social y Religión",999))
colita.put(generar("6060dc7aaac831ddfc81a31e","22Matemática Avanzada",999))
colita.put(generar("6060dc7aaac831ddfc81a31f","23Comunicación Avanzada",999))
colita.put(generar("6060dc7aaac831ddfc81a320","24Comunicación",999))
colita.put(generar("6060dc7aaac831ddfc81a321","25Matemática",999))
colita.put(generar("6060dc7aaac831ddfc81a322","26Material Lúdico",999))
colita.put(generar("6060dc7aaac831ddfc81a323","27Ciencia y Tecnología",999))
colita.put(generar("6060dc7aaac831ddfc81a324","28Persona Social y Religión",999))
colita.put(generar("6060dc7aaac831ddfc81a325","29Taller Expresion Plástica",999))
colita.put(generar("6060dc7aaac831ddfc81a326","30Taller Grafo Motrocidad",999))
colita.put(generar("6060dc7aaac831ddfc81a318","31Habilidades del Pensamiento 1",999))
colita.put(generar("6060dc7aaac831ddfc81a31b","32Habilidades del Pensamiento 2",999))
colita.put(generar("6060dc7aaac831ddfc81a31c","33Habilidades del Pensamiento 3",999))



