def turno(t):
    """funcao que alterna entre turnos dos jogadores"""
    if t%2 != 0:
        return 1
    else:
        return 2
