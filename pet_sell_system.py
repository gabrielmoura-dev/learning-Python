'''
criar um sistema para determinar se o funcionario pode vender um pet para um cliente
'''
has_license = True
has_space = True
has_experience = False
# O cliente pode comprar um pet regular se tiver OU uma licença OU experiência, E deve ter espaço
can_sell_regular_pet = (has_license or has_experience) and has_space
# O cliente pode comprar um pet exótico se tiver UMA licença E experiência, E deve ter espaço
can_sell_exotic_pet = has_license and has_experience and has_space
# A loja NÃO PODE vender nenhum pet se o cliente não tiver licença E não tiver experiência, OU não tiver espaço
cannot_sell_any_pet = (not has_license and not has_experience) or not has_space
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)