"""
Corey Verkouteren
10/28/2024
CSCI 310
Baseball Player Signer

Gets the most VORP possible with a fixed budget given a set of baseball players
"""
def make_2d_array(rows, columns):
    blank_array = []
    for r in range(rows):
        blank_array.append([])
        for c in range(columns):
            blank_array[r].append(0)

    return blank_array


# 2 tables: 1 has the best vorp considering positions and budget
# 2nd is made with that one, reflecting what players are needed to make that vorp
def position_comparison(positions: int, position_players: int, options: list, budget: int):
    position_cost_array = make_2d_array(positions + 1, budget + 1)
    player_position_array = [0 for i in range(positions)]

    for position in range(positions + 1):
        for cost in range(budget + 1):
            # make first row and column 0 to avoid list boundary errors
            if position == 0 or budget == 0:
                position_cost_array[position][cost] = 0

            else:
                # default to best value being the one above (with those player values)
                position_cost_array[position][cost] = position_cost_array[position - 1][cost]

                # check if adding a player from this position will make it larger
                for player in options[position- 1]:
                    # if player is less than available budget, consider adding
                    if player.get_cost() <= cost:
                        # value if we were to add
                        plus_player = position_cost_array[position - 1][cost - player.get_cost()] + player.get_vorp()
                        # if adding the player gives more vorp, add them
                        if position_cost_array[position][cost] < plus_player:
                            position_cost_array[position][cost] = plus_player
                            print(position - 1, player.get_all(), cost)
                            player_position_array[position - 1] = player

                """
                # get the maximum vorp player for this cost in this position
                max_vorp_player = max([player for player in options[position - 1] if player.get_cost() <= cost],
                                      default=0)

                # if no player available for this cost, enter above value
                if max_vorp_player == 0:
                    position_cost_array[position][cost] = position_cost_array[position -1][cost]

                # if player available, add the maximum value between adding or not adding this player
                else:
                    above_value = position_cost_array[position - 1][cost]
                    add_mvp_value = (max_vorp_player.get_vorp() +
                                     position_cost_array[position - 1][cost - max_vorp_player.get_cost()])

                    if position == 3:
                        print(above_value, add_mvp_value, max_vorp_player.get_all(),position_cost_array[position - 1][cost - max_vorp_player.get_cost()], cost)

                    position_cost_array[position][cost] = max(above_value, add_mvp_value)
                

                player_position_array[position][cost] = max_vorp_player
                """

    return position_cost_array, player_position_array


def get_best_team(pc_array, pp_array, positions, budget):
    j = budget
    result = pc_array[positions][budget]

    best_team = {"VORP Total": result,
                 "Cost Total": 0,
                 "Players": []}

    for i in range(positions, 0, -1):
        print(i, j)
        if result <= 0:
            best_team["Cost Total"] = j
            return best_team
        if result != pc_array[i - 1][j]:
            pos_player = pp_array[i - 1]
            print(type(pos_player), i, j)

            best_team["Players"].append(pos_player)

            result -= pos_player.get_vorp()
            j -= pos_player.get_cost()

            best_team["Cost Total"] += pos_player.get_cost()

    return best_team
