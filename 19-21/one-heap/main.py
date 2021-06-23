#!/usr/bin/env python3

moves = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 5]


def win(state):
    return state >= 68


def print_game(state, n, max_depth, file):
    if n >= max_depth:
        return
    file.write(f'{"  " * n} {state} {"-- win" if win(state) else ""}\n')
    if win(state):
        return
    for m in moves:
        print_game(m(state), n + 1, max_depth, file)


for max_depth in range(3, 5 + 1):
    with open('log' + str(max_depth), 'w') as file:
        for S in range(1, 67):
            state = S
            file.write('--------------------\n')
            print_game(S, 0, max_depth, file)
