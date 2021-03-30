import random, string, json
import pandas as dp

codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
data2 = [ {"codigo": "abc"

} ]
while i!=20:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x

    data2.append({"codigo":x})
    df.loc[i+1]=[x]
    i=i+1



with open('acod_obras3.json', 'w') as file:
    json.dump(data2, file, indent=4)
df.to_excel("aprueba.xlsx", index=False)