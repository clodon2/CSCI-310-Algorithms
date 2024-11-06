"""
Corey Verkouteren
10/28/2024 - 11/6/2024
CSCI 310
Baseball Player Signer

Actual maximum vorp and position player table creation and best team finding
"""
def make_2d_array(rows:int, columns:int):
    """
    make a 2d array with given rows and columns
    :param rows: lists in main array list
    :param columns: amount of 0s in each row list
    :return:
    """
    blank_array = []
    for r in range(rows):
        # add new row
        blank_array.append([])
        for c in range(columns):
            # add new column item to row
            blank_array[r].append(0)

    return blank_array


def position_comparison(positions:int, options:list, budget:int):
    """
    given player and budget info, return 2 arrays that reflect best vorp possible and best players possible
    :param positions: number of positions we're looking at
    :param options: 2d array with player options, row = position column = player
    :param budget: amount we can spend on players
    :return: best vorp for budget array (2d), and best player for position w/ given budget array (2d)
    """
    # stores maximum vorp value possible for current position # with certain budget
    position_cost_array = make_2d_array(positions + 1, budget + 1)
    # stores best player to pick for each position given a certain budget
    player_position_array = make_2d_array(positions + 1, budget + 1)

    for position in range(positions + 1):
        for cost in range(budget + 1):
            # make first row and column 0 to avoid list boundary errors
            if position == 0 or budget == 0:
                position_cost_array[position][cost] = 0

            else:
                # default to best value being the one above (with those player vorps)
                position_cost_array[position][cost] = position_cost_array[position - 1][cost]

                # check if adding a player from this position will make it larger
                for p in range(len(options[position - 1])):
                    # player object, p is index
                    player = options[position - 1][p]
                    # if player is less than available budget, consider adding
                    if player.get_cost() <= cost:
                        # value if we were to add the player to position_cost array
                        plus_player = position_cost_array[position - 1][cost - player.get_cost()] + player.get_vorp()
                        # if adding the player gives more vorp, add them to our tables
                        if position_cost_array[position][cost] < plus_player:
                            position_cost_array[position][cost] = plus_player

                            player_position_array[position][cost] = p

    return position_cost_array, player_position_array


def get_best_team(pc_array:list, pp_array:list, options:list, positions:int, budget:int):
    """
    work through both tables/arrays to find the best team
    :param pc_array: player_cost array/table, the one with max vorp for budget w/ each position
    :param pp_array: player_position array/table, the one with the best player for a given budget in each position
    :param options: original 2d array of player options
    :param positions: number of positions we're looking at
    :param budget: amount we can spend on players
    :return: dictionary with "VORP Total":int, "Cost Total":int, and "Players":list reflecting best team
    """
    current_budget = budget
    # bottom right value considers best vorp for all positions combined (with max budget)
    best_vorp = pc_array[positions][budget]

    best_team = {"VORP Total": best_vorp,
                 "Cost Total": 0,
                 "Players": []}

    for position in range(positions, 0, -1):
        # if current best vorp is diff from above, player there must have been added
        if best_vorp != pc_array[position - 1][current_budget]:
            # add player to list of best choices
            pos_player = options[position - 1][pp_array[position][current_budget]]
            best_team["Players"].append(pp_array[position][current_budget])

            # best vorp is now without the player from that position
            best_vorp -= pos_player.get_vorp()
            # used budget to get that player for their cost
            current_budget -= pos_player.get_cost()
            best_team["Cost Total"] += pos_player.get_cost()

    return best_team
