capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
aumento_capacidade = int(capacidade_atual * (aumento_percentual/100))
nova_capacidade = capacidade_atual + aumento_capacidade

# TODO: Imprima a nova capacidade
print(nova_capacidade)
#codigo aprovado