# Leggi i nomi_saggio completi da file1.txt e tieni solo la parte finale
with open("pippo2.txt", "r", encoding="utf-8") as f1:
    saggi_completi = {line.strip().split(".")[-1].replace(" ", "_") for line in f1 if line.strip()}
    
# Leggi i nomi_saggio da file2.txt
with open("pippo.txt", "r", encoding="utf-8") as f2:
    saggi_da_verificare = {line.strip().removeprefix("flare.saggi.cluster.") for line in f2 if line.strip()}

index = 0

for saggio in saggi_completi:
    if saggio not in saggi_da_verificare:
        index = index + 1
        print(f"{index} {saggio}")

# Stampa i mancanti
# print("Saggi mancanti in pippo.txt:")
# for nome in sorted(mancanti):
#     print(nome)
