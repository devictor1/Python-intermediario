setNumero = set((156,82,96,546,42,69))
setNovo = {8}
setNovo.update(setNumero)
setNumero.add(2)
setNumero.remove(156)
for i in setNumero:
    print(i)
print(32 in setNumero)
print(82 in setNumero)
print(setNovo)