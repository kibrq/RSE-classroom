#!/usr/bin/env python3

def win(state):
    return state >= 68


def print_game(state, n, max_depth, file):
    if n >= max_depth:
        return
    file.write(f'{"  " * n} {state} {"-- win" if win(state) else ""}\n')
    if win(state):
        return
    print_game(state + 1, n + 1, max_depth, file)
    print_game(state + 4, n + 1, max_depth, file)
    print_game(state * 5, n + 1, max_depth, file)


with open('log', 'w') as file:
     for S in range(1, 67):
         state = S
         file.write('--------------------\n')
         print_game(S, 0, 3, file) # вместо max_depth можно подставить нужную глубину
