def maximizar_troca_de_figurinhas(self, figurinhas_da_maria, figurinhas_do_joao):
    joao = 0
    maria = 0

    if figurinhas_da_maria != figurinhas_da_joao:
        joao = joao +1
        return joao
    else: figurinhas_da_joao != figurinhas_da_maria
    maria = maria +1
    return maria

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
