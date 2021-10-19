pessoas = []
media = cont = 0
while True:
    pessoas.append({"nome":input("Nome: ").title().strip()})
    pessoas[cont]["sexo"] = input("Sexo [F/M]: ").upper().strip()
    while pessoas[cont]["sexo"] not in "FM":
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoas[cont]["sexo"] = input("Sexo [F/M]: ").upper().strip()
    pessoas[cont]["idade"] = int(input("Idade: "))
    media += pessoas[cont]["idade"]
    cont += 1
    es = input("Quer continuar?[S/N]: ").strip()
    while es not in "snSN":
        print("ERRO! Responda apenas S ou N.")
        es = input("Quer continuar?[S/N]: ").strip()
    if es == "n":
        break
media /= len(pessoas)
print("=-" * 35)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
print(f"B) A média de idade é de {media} anos..")
print("C) As mulheres cadstrads foram:", end=" ")
for c in pessoas:
    if c["sexo"] == "F":
        print(c["nome"], end=" ")
print()
print("D) Lista de pessoas com a idade acima da média:")
for c in pessoas:
    if c["idade"] > media:
        for k, v in c.items():
            print(f"{k:>8} = {v:<14}",end="")
        print()
print("<< ENCERRADO >>")
