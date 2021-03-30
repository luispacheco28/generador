import random, string, json
import pandas as dp

i=0
data = [ {
    "book":"cabezal",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c64",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3matematica.json', 'w') as file:
    json.dump(data, file, indent=4)

df.to_excel("maestras3matematica.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c65",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3personal.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras3personal.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c66",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3tecnicas.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras3tecnicas.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c67",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4ct.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4ct.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c68",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4comu.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4comu.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c69",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4ingles.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4ingles.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c6a",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4personal.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4personal.xlsx", index=False)
print("éxito")




i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c6b",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4tecnicas.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4tecnicas.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c6c",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4grafias.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4grafias.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c6d",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras4matematica.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras4matematica.xlsx", index=False)
print("éxito")




i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c6e",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5ct.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5ct.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c6f",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5comu.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5comu.xlsx", index=False)
print("éxito")


i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c70",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5matematica.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5matematica.xlsx", index=False)
print("éxito")




i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c71",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5materec.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5materec.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c72",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5ingles.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5ingles.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c73",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5personal.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5personal.xlsx", index=False)
print("éxito")




i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c74",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5tecnicas.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5tecnicas.xlsx", index=False)
print("éxito")



i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c75",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras5grafias.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras5grafias.xlsx", index=False)




i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c76",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras2edutemp.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras2edutemp.xlsx", index=False)





i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c77",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras2materec.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras2materec.xlsx", index=False)





i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c78",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras2tecnicas.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras2tecnicas.xlsx", index=False)





i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c79",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3ct.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras3ct.xlsx", index=False)





i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c7a",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3comu.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras3comu.xlsx", index=False)





i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c7b",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3grafias.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras3grafias.xlsx", index=False)





i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c7c",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('maestras3materec.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("maestras3materec.xlsx", index=False)


i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c7d",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas3ct.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas3ct.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c7e",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas3comu.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas3comu.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c7f",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas3mate.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas3mate.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c80",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas3personal.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas3personal.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c81",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas3psico.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas3psico.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "601f762675fd6a1ac5870c82"+x
    data.append({
    "book":"601f762675fd6a1ac5870c82",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas3reli.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas3reli.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c83",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas4ct.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas4ct.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c84",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas4comu.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas4comu.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c85",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas4mate.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas4mate.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c86",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas4personal.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas4personal.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c87",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas5reli.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas5reli.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c88",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas4psico.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas4psico.xlsx", index=False)








i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c8a",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas5ct.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas5ct.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c8b",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas5comu.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas5comu.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c8c",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas5mate.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas5mate.xlsx", index=False)






i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c8d",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas5personal.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas5personal.xlsx", index=False)


i=0
data = [ {
    "book":"ra",
    "code":"ARCAAPTUC8I210121"
} ]
codigo=[('Codigos')]

df=dp.DataFrame(codigo,columns=['codigo'])
i=0
while i!=19999:
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    x = "ARCR"+x
    data.append({
    "book":"601f762675fd6a1ac5870c8e",
    "code":x
})
    df.loc[i+1]=[x]
    i=i+1


with open('manitas5psico.json', 'w') as file:
    json.dump(data, file, indent=4)
df.to_excel("manitas5psico.xlsx", index=False)


