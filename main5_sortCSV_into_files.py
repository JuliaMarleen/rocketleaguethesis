import csv

token = "5rJrtU5yJZEyshaPvpeJ5TuxlmgrnIFZqOg3tiQ8"
replay_id = "93441ec7-8c9b-45f3-b1a7-da6b3d3ee1ad"
replay_id2 = "35a53d71-d7f0-494b-b88a-9285b79a1f90"
replay_id3 = "105a245c-bc72-4a9c-9c4e-4d845af694af"
replay_id4 = "d1fe5bbc-e5e1-48e2-8279-a23cec9655ac"
replay_id_pro = "15f12bd9-f4a6-4cea-a2dc-610cd9dd976b"
filter = "?season=f4&min-rank=champion-1&max-rank=grand-champion-2&playlist=ranked-standard&count=2"


column_names_rank = ["game_id", "player_tag", "movement_avg_speed", "movement_total_distance", "movement_time_supersonic_speed",
    "movement_time_boost_speed", "movement_time_slow_speed", "movement_time_ground", "movement_time_low_air",
    "movement_time_high_air", "movement_time_powerslide", "movement_count_powerslide", "movement_avg_powerslide_duration",
    "movement_avg_speed_percentage", "movement_percent_slow_speed", "movement_percent_boost_speed",
    "movement_percent_supersonic_speed", "movement_percent_ground", "movement_percent_low_air", "movement_percent_high_air",
    "positioning_avg_distance_to_ball", "positioning_avg_distance_to_ball_possession", "positioning_avg_distance_to_ball_no_possession",
    "positioning_avg_distance_to_mates", "positioning_time_defensive_third", "positioning_time_neutral_third",
    "positioning_time_offensive_third", "positioning_time_defensive_half", "positioning_time_offensive_half",
    "positioning_time_behind_ball", "positioning_time_infront_ball", "positioning_time_most_back", "positioning_time_most_forward",
    "positioning_time_closest_to_ball", "positioning_time_farthest_from_ball", "positioning_percent_defensive_third", 
    "positioning_percent_offensive_third", "positioning_percent_neutral_third", "positioning_percent_defensive_half", 
    "positioning_percent_offensive_half", "positioning_percent_behind_ball", "positioning_percent_infront_ball", 
    "positioning_percent_most_back", "positioning_percent_most_forward", "positioning_percent_closest_to_ball", 
    "positioning_percent_farthest_from_ball", "pro", "winner"] ## infront -> end result

column_names_pro = ["game_id", "player_tag", "movement_avg_speed", "movement_total_distance", "movement_time_supersonic_speed",
    "movement_time_boost_speed", "movement_time_slow_speed", "movement_time_ground", "movement_time_low_air",
    "movement_time_high_air", "movement_time_powerslide", "movement_count_powerslide", "movement_avg_powerslide_duration",
    "movement_avg_speed_percentage", "movement_percent_slow_speed", "movement_percent_boost_speed",
    "movement_percent_supersonic_speed", "movement_percent_ground", "movement_percent_low_air", "movement_percent_high_air",
    "positioning_avg_distance_to_ball", "positioning_avg_distance_to_ball_possession", "positioning_avg_distance_to_ball_no_possession",
    "positioning_avg_distance_to_mates", "positioning_time_defensive_third", "positioning_time_neutral_third",
    "positioning_time_offensive_third", "positioning_time_defensive_half", "positioning_time_offensive_half",
    "positioning_time_behind_ball", "positioning_time_in_front_ball", "positioning_time_most_back", "positioning_time_most_forward",
    "positioning_time_closest_to_ball", "positioning_time_farthest_from_ball", "positioning_percent_defensive_third", 
    "positioning_percent_offensive_third", "positioning_percent_neutral_third", "positioning_percent_defensive_half", 
    "positioning_percent_offensive_half", "positioning_percent_behind_ball", "positioning_percent_in_front_ball", 
    "positioning_percent_most_back", "positioning_percent_most_forward", "positioning_percent_closest_to_ball", 
    "positioning_percent_farthest_from_ball", "pro", "winner"] ## in_front -> will change to infront

## need this?? ->> "game_id", "color", "team_id", "player_id", 
## what I don't have? ['game_id', 'color', 'team_id', 'player_id', 'positioning_time_in_front_ball', 'positioning_percent_in_front_ball']
## -> 'positioning_time_infront_ball', 'positioning_percent_infront_ball' -> without _ in "infront" does have
###### -> need to change this in csv of pro file
## what's not always there  "positioning_goals_against_while_last_defender" -> is also goals -> shouldn't use


def getCSV(CSV_file):
    team_list = []
    player_list = []
    good_players = 0 # just checking
    good_teams = 0 # just checking
    skipped_players = 0 # just checking
    skipped_teams = 0 # just checking
    skipped_teams_not_3 = 0 # just checking
    team_mates_one = 0 # just checking
    team_mates_two = 0 # just checking
    team_mates_three = 0 # just checking
    players_above_100 = 0 # just checking
    game_too_short = 0 # just checking
    played_too_short = 0 # just checking

    with open(CSV_file, newline='') as csvfile:
        playerreader = csv.reader(csvfile, delimiter=',')

        column_names_pro_all = []
        team_dict = {}
        usable_team_data = True

        current_game_id_team = "" # This one is relevant 
        current_color_team = "" # This one is relevant 
        players_in_team = 0 # This one is relevant 
        weird_numbers = 0 # just checking
        temp_player_list = [] # This one is relevant 

        for index_player, row in enumerate(playerreader):
            usable_player_data = True
            player_dict = {}
            current_game_id_player = ""
            current_color_player = ""
            game_duration = 0
            if index_player == 0: # row 0 is column names
                for item in row:
                    column_names_pro_all.append(item)
            else:
                for index_item, item in enumerate(row):
                    if column_names_pro_all[index_item] == 'game_id':
                        current_game_id_player = item
                        player_dict['game_id'] = item
                    elif column_names_pro_all[index_item] == 'color':
                        current_color_player = item
                    elif column_names_pro_all[index_item] ==  "_duration":
                        game_duration = float(item)
                        print(item)
                        if float(item) < 300:
                            print("too short")
                            usable_player_data = False
                            usable_team_data = False
                            game_too_short += 1
                    elif column_names_pro_all[index_item] == "players_end_time":
                        print(item, game_duration)
                        if float(item) < game_duration:
                            print(item, game_duration)
                            usable_player_data = False
                            usable_team_data = False
                            played_too_short += 1
                    
                    # if 'percentage'

                    elif column_names_pro_all[index_item] in column_names_pro or column_names_pro_all[index_item] in column_names_rank:
                        if item == "":
                            usable_player_data = False
                            usable_team_data = False
                        elif column_names_pro_all[index_item] ==  "player_tag":
                            player_dict['player_tag'] = item
                        elif column_names_pro_all[index_item] == 'winner':
                            if 'pro' not in column_names_pro_all:
                                player_dict['pro'] = True
                            player_dict[column_names_pro_all[index_item]] = item
                            if (players_in_team % 3) == 0:
                                if 'pro' not in column_names_pro_all:
                                    team_dict['pro'] = True
                                team_dict[column_names_pro_all[index_item]] = item
                        elif column_names_pro_all[index_item] == 'pro':
                            player_dict[column_names_pro_all[index_item]] = item
                            team_dict[f"{column_names_pro_all[index_item]}_{players_in_team % 3}"] = item
                        elif column_names_pro_all[index_item] ==  "positioning_time_in_front_ball":
                            player_dict["positioning_time_infront_ball"] = round(float(item), 2)
                            team_dict[f"positioning_time_infront_ball_{players_in_team % 3}"] = round(float(item), 2)
                        elif column_names_pro_all[index_item] ==  "positioning_percent_in_front_ball":
                            player_dict["positioning_percent_infront_ball"] = round(float(item), 2)
                            team_dict[f"positioning_percent_infront_ball_{players_in_team % 3}"] = round(float(item), 2)
                        else:
                            if "percent" in column_names_pro_all[index_item]:
                                if float(item) > 100:
                                    usable_player_data = False
                                    usable_team_data = False
                                    players_above_100 +=1
                                    print(item)
                            player_dict[column_names_pro_all[index_item]] = round(float(item), 2)
                            team_dict[f"{column_names_pro_all[index_item]}_{players_in_team % 3}"] = round(float(item), 2)
                
                if current_game_id_team == current_game_id_player and current_color_team == current_color_player:
                    players_in_team += 1 # this one is relevant and counts players per team
                else:
                    # When the team (color) or game (game_id) switches, check if 3 players
                    if players_in_team != 3: # when not 3 in one team (more or less than 3)
                        print("skipped to next team, but not 3 in a team -> so not in team file")
                        print(players_in_team)
                        # print(row[0])
                        skipped_teams_not_3 += 1 # just checking
                        # list_temp = player_list[-players_in_team:] # just checking
                        del player_list[-players_in_team:] # 

                        # for player_temp in list_temp:
                        #     print(player_temp["player_tag"]) # just checking

                    if players_in_team > 3: # when more than 3 in one team
                        # print("DELETE", team_list[-1])
                        del team_list[-1],

                        print("4 of meeeeer:", players_in_team)
                        weird_numbers += 1 #just checking 

                    players_in_team = 1 # reset
                    current_game_id_team = current_game_id_player # update game id
                    current_color_team = current_color_player # updat color
                    team_dict = {} # empty team_dict, because we don't want it

                if usable_player_data == True: # player data is good
                # if usable_player_data == True: # player data is good
                    temp_player_list.append(dict(player_dict))
                    good_players += 1 # just checking
                else: # player data is bad
                    skipped_players += 1 # just checking
                
                if players_in_team == 3: # 3 players in one team
                    team_mates_three += 1 #just tests
                    if usable_team_data == True: # team data is good
                        team_list.append(dict(team_dict)) 
                        good_teams += 1 #just tests
                        for player_item in temp_player_list:
                            player_list.append(player_item)
                    else: # team data is bad
                        skipped_teams += 1 # just checking
                    team_dict = {} # reset variable
                    temp_player_list = [] # reset variable
                    usable_team_data = True # reset variable

                ####################################
                elif players_in_team == 2: #just tests
                    team_mates_two += 1 # just checking
                elif players_in_team == 1: # just checking
                    team_mates_one += 1 # just checking

            # if index_player == 100: # Stop after 6 lines/players -> not neccesary if I use whole file -> just for testing
            #     break
    
    print("good players", good_players)
    print("good Teams", good_teams)
    print("skipped players, bc unusable data: ", skipped_players)
    print("skipped teams, bc unusable data:", skipped_teams)
    print("skipped teams, bc not 3:", skipped_teams_not_3)
    print("teammates, 1:", team_mates_one)
    print("teammates, 2:", team_mates_two)
    print("teammates, 3:", team_mates_three)
    print("Total", team_mates_one + team_mates_two + team_mates_three)
    print("weird_numbers", weird_numbers)
    print("above 100", players_above_100)
    print("Game too short", game_too_short)
    print("Played too short", played_too_short)

    # print(column_names_pro_all)
    return team_list, player_list



if __name__ == "__main__":
    dictPro = getCSV('archive/games_by_players.csv') # uses CSV
    dictAPI = getCSV('games_by_players_API_ranked3.csv') # uses CSV -> with 2 is grand-champion-1

    ######### games_by_player ranked & pro
    with open('games_by_players_all.csv', 'w', newline='') as csvfile:
        fieldnames = column_names_rank
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for player in dictAPI[1]:
            writer.writerow(player)
        for player in dictPro[1]:
            writer.writerow(player)
    
    ######### games_by_team ranked & pro
    with open('games_by_team_all.csv', 'w', newline='') as csvfile:
        all_keys = []
        for d in dictAPI[0]: # get keys that I used/made from API data for team: 3 players + winner + pro
            for key in d.keys():
                if key not in all_keys:
                    all_keys.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)

        writer.writeheader()
        for team in dictAPI[0]:
            writer.writerow(team)
        for team in dictPro[0]:
            writer.writerow(team)
    
    ######### make games_by_player_ranked
    with open('games_by_players_ranked.csv', 'w', newline='') as csvfile:
        fieldnames = column_names_rank
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for player in dictAPI[1]:
            writer.writerow(player)
    
    ######### make games_by_player_pro
    with open('games_by_players_pro.csv', 'w', newline='') as csvfile:
        fieldnames = column_names_rank
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for player in dictPro[1]:
            writer.writerow(player)
    
    ######## make games_by_team_ranked
    with open('games_by_team_ranked.csv', 'w', newline='') as csvfile:
        all_keys = []
        for d in dictAPI[0]: # get keys that I used/made from API data for team: 3 players + winner + pro
            for key in d.keys():
                if key not in all_keys:
                    all_keys.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)

        writer.writeheader()
        for team in dictAPI[0]:
            writer.writerow(team)
    
    ######## make games_by_team_pro
    with open('games_by_team_pro.csv', 'w', newline='') as csvfile:
        all_keys = []
        for d in dictAPI[0]: # get keys that I used/made from API data for team: 3 players + winner + pro
            for key in d.keys():
                if key not in all_keys:
                    all_keys.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)

        writer.writeheader()
        for team in dictPro[0]:
            writer.writerow(team)

    # ## to all put seperately in the model -> why? what can I learn?
