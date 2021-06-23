#!/usr/bin/env python3

moves = [lambda p: (p[0] + 1, p[1]),
         lambda p: (p[0], p[1] + 1),
         lambda p: (2 * p[0], p[1]),
         lambda p: (p[0], 2 * p[1])]


def win(state):
    return state[0] + state[1] >= 93


def print_game(state, n, max_depth, file):
    if n >= max_depth:
        return
    file.write(f'{"  " * n} {n}, {state} {"-- win" if win(state) else ""}\n')
    if win(state):
        return
    print_game((state[0] + 1, state[1]), n + 1, max_depth, file)
    print_game((state[0], state[1] + 1), n + 1, max_depth, file)
    print_game((2 * state[0], state[1]), n + 1, max_depth, file)
    print_game((state[0], 2 * state[1]), n + 1, max_depth, file)


with open('log', 'w') as file:
    for S in range(1, 80 + 1):
        state = (12, S)
        file.write('--------------------\n')
        print_game(state, 0, 3, file) # вместо max_depth можно подставить нужную глубину
