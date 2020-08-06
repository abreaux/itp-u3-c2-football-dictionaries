def players_by_position(squads_list):
    r_dict = {}
    for player in squads_list:
        r_dict[player[1]]= []
    for player in squads_list:
        r_dict[player[1]].append(player[2])
    return r_dict
