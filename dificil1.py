te = float(input("total de eleitores"))
print(te)
b = float(input("informe o total de votos brancos"))
print(b)
n = float(input("informe o total de votos nulos"))
print(n)

vi = (float(te) - float(n))
pv = (float(vi) * float(te))/100

print("o percentual de votos validos e",(pv),"%")