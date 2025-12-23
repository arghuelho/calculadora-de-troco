conjunto_notas = (10000, 5000, 2000, 1000, 500, 200)
conjunto_moedas = (100, 50, 25, 10, 5)


compra = 1
pagamento = 2 


def contas(contexto):

    #inputs e correções.

    if contexto == compra:
        texto_input = "Digite o valor da compra: "
    elif contexto == pagamento:
        texto_input = "Digite o valor da pagamento: "
    else:
        raise ValueError("contexto inválido.")

    valor = input(texto_input)
    valor = valor.replace(",", ".")
    partes = valor.split(".")

    if len(partes) > 2:
        raise ValueError("Formatação inválida.")
    if not partes[0].isdigit():
        raise ValueError("Formatação inválida.")
    if len(partes) == 2 and not partes[1].isdigit():
        raise ValueError("Formatação inválida.")

    #conversoes + calculo

    reais = int(partes[0]) * 100

    centavos = 0

    if len(partes) == 2:
        decimal = partes[1].ljust(2, "0")
        centavos= int(decimal)
    else:
        centavos = 0


    return reais + centavos
    

def troco(valor_compra, valor_pagamento):
 
    if valor_pagamento >= valor_compra:
        troco = valor_pagamento - valor_compra
    else: 
        raise ValueError("Pagamento MENOR que a compra")


    return troco


def main():
    valor_compra = contas(compra)
    valor_pagamento = contas(pagamento)
    troco_em_centavos = troco(valor_compra,valor_pagamento)

    reais = troco_em_centavos // 100
    centavos = troco_em_centavos % 100

    print(f"Troco: R${reais},{centavos:02d}")

    resultado = {}

    for nota in conjunto_notas:
        quantidade = troco_em_centavos // nota

        if quantidade > 0:
            resultado[nota] = quantidade
            troco_em_centavos = troco_em_centavos % nota

    for moeda in conjunto_moedas:
        quantidade = troco_em_centavos // moeda

        if quantidade > 0:
            resultado[moeda] = quantidade
            troco_em_centavos = troco_em_centavos % moeda

    for valor, quantidade in resultado.items():
        if valor > 100:
            text = (f"{quantidade} nota(s) de R${valor/100:g},00 ")
            print(text)
        elif valor == 100 and quantidade == 1:
            text = (f"{quantidade} moeda de R${valor/100:g},00")
            print(text)
        else:
            text = (f"{quantidade} moeda(s) de R${valor/100:.2f}")
            print(text)

main()
