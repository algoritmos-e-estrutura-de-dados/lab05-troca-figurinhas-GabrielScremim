def maximizar_troca_de_figurinhas(self, figurinhas_da_maria, figurinhas_do_joao):

    if figurinhas_da_maria != figurinhas_da_joao:
        return figurinhas_da_joao
    else: figurinhas_da_joao != figurinhas_da_maria
    return figurinhas_da_maria

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
