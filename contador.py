import time


def contagem(segundos):
    """
    Esta função recebe um parâmetro inteiro.
    :param segundos: recebe um valor inteiro
    :return: retorna um segundo, até finalizar os segundos informados no parâmetro.
    """
    while segundos:
        m, s = divmod(segundos, 60)
        min_sec = '{:02d}:{:02d}'.format(m, s)
        print(min_sec, end='\n')
        time.sleep(1)
        segundos -= 1