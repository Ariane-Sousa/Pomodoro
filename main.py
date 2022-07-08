import os
from contador import contagem


def pomodoro():
    """
    Função sem parâmetro.
    :return: retorna ciclos de pomodoros. Um ciclo possui um contador de 25 minutos, após um de 5 minutos. Após 4 ciclos,
    inicia-se um contador de 20 minutos.
    """
    pomodoros = 0
    definicao = input('Olá, você já conhece o método pomodoro? (S/N): ')
    if definicao == 'N'.lower():
        print('O método Pomodoro propõe estudos divididos em blocos de 25 minutos e pausa de 5 minutos..\nAo final de 4 blocos, realiza-se uma pausa de 20. ')
    iniciar = input('\nDeseja iniciar o Pomodoro? (S/N): ')
    while iniciar == 'S'.lower():
        n = int(input('Quantos blocos pomodoros irá realizar: '))
        duration = 1
        freq = 440
        for x in range(n):
            print(f'\nEstudo de 25 minutos!')
            (contagem(1500))
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
            print(f'\nIntervalo de 5 minutos! ')
            (contagem(300))
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
            pomodoros += 1
        if n == 4:
            print(f'\nIntervalo de 20 minutos! ')
            (contagem(1200))
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        iniciar = input('Começara um novo ciclo? S/N')
    print(f'\nTotal de blocos pomodoros realizados: {pomodoros}')
    print('Até mais. Espero que o método Pomodoro tenha sido eficaz. :)')


pomodoro()
