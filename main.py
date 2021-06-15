import random
TILES = {}
players = {
    "player1": 1,
    "player2": 1,
}
order = -1  # for printing board in zigzag
player_position = 1
for i in range(1, 101):
    TILES[i] = -1   # initializing board tiles with -1


TILES[98] = 5   # snake
TILES[89] = 55  # snake
TILES[41] = 9   # snake
TILES[78] = 53  # snake
TILES[2] = 45   # ladder
TILES[25] = 62   # ladder
TILES[35] = 70   # ladder
TILES[9] = 20   # ladder


def printing_tiles(v1, v2, mode):
    """
    this will print board on console
    """
    if mode == 1:
        j = v1
        while j > v2:
            print(TILES[j], end=" ")
            j -= 1
    else:
        k = v1+1
        while k <= v2:
            print(TILES[k], end=" ")
            k += 1


L2R_turns = 100
while L2R_turns > 0:
    R2L_turns = (L2R_turns - 10)
    order *= -1
    if order == -1:
        R2L_turns, L2R_turns = L2R_turns, R2L_turns
    printing_tiles(L2R_turns, R2L_turns, order)
    print("\n")
    if order == -1:
        R2L_turns = L2R_turns
    else:
        L2R_turns = R2L_turns


def play(player):
    global players
    dice = random.randint(1, 6)
    print(f"dice : {dice}")
    temp_pos = players[player]+dice
    if temp_pos > 100:
        return temp_pos-dice
    elif TILES[temp_pos] > 0:
        return TILES[temp_pos]
    else:
        return temp_pos


game_on = True
p = 1
while game_on:
    if p == 1:
        pla = "player1"
    else:
        pla = "player2"
    print(f'Current positions - Player 1 : {players["player1"]} | Player 2 : {players["player2"]}')
    u = input(f"Press D to roll dice for {pla}: ")
    if u == "d":
        new_pos = play(pla)
        players[pla] = new_pos
        if new_pos == 100:
            print(f"{pla} wins")
            game_on = False
    else:
        print("Game ended!")
        game_on = False
    p *= -1
