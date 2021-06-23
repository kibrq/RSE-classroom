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
    for m in moves:
        print_game(m(state), n + 1, max_depth, file)


for max_depth in range(3, 5 + 1):
    with open('log' + str(max_depth), 'w') as file:
        for S in range(1, 80 + 1):
            state = (12, S)
            file.write('--------------------\n')
            print_game(state, 0, max_depth, file)
