import csv
import numpy as np
import statistics

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


def getCSV(CSV_file):
    team_list = []

    with open(CSV_file, newline='') as csvfile:
        teamreader = csv.reader(csvfile, delimiter=',')

        column_names_pro_all = []
        team_dict = {}

        for index_team, row in enumerate(teamreader):
            if index_team == 0: # row 0 is column names
                for item in row:
                    column_names_pro_all.append(item)
            else: # all other rows that are teams
                speed = [] # want to know, min, max, variance, should be 3 all

                positioning_percent_behind_ball = [] # want to know, min, max, variance (offensive half)
                positioning_percent_infront_ball = [] # want to know, min, max, variance (defensive half)
                positioning_time_behind_ball = [] # want to know, min, max, variance (offensive half)
                positioning_time_front_of_ball = [] # want to know, min, max, variance

                positioning_percent_closest_to_ball = [] # want to know, min, max, variance
                positioning_percent_farthest_from_ball = [] # want to know, min, max, variance
                positioning_avg_distance_to_ball_possession = []
                positioning_avg_distance_to_ball_no_possession = []
                positioning_avg_distance_to_ball = []
                positioning_avg_distance_to_mates = []

                positioning_percent_most_forward = [] # want to know, min, max, variance
                positioning_percent_most_back = [] # want to know, min, max, variance
                positioning_time_most_forward = [] # want to know, min, max, variance
                positioning_time_most_back = [] # want to know, min, max, variance

                movement_percent_high_air = [] # want to know, min, max, variance
                movement_percent_supersonic_speed = []

                temp_pro_win = []

                for index_item, item in enumerate(row):
                    if 'pro' in column_names_pro_all[index_item] or 'winner' in column_names_pro_all[index_item]:
                        # print(item)
                        temp_pro_win.append(item)
                    else:
                        team_dict[column_names_pro_all[index_item]] = item


                    if  "movement_avg_speed" in column_names_pro_all[index_item] and "percentage" not in column_names_pro_all[index_item]:
                        speed.append(float(item))
                        # print(item)

                    elif "positioning_percent_behind_ball" in column_names_pro_all[index_item]:
                        positioning_percent_behind_ball.append(float(item))
                    elif "positioning_percent_infront_ball" in column_names_pro_all[index_item]:
                        positioning_percent_infront_ball.append(float(item))
                    elif "positioning_time_behind_ball" in column_names_pro_all[index_item]:
                        positioning_time_behind_ball.append(float(item))
                    elif "positioning_time_infront_ball" in column_names_pro_all[index_item]:
                        positioning_time_front_of_ball.append(float(item))

                    elif "positioning_percent_closest_to_ball" in column_names_pro_all[index_item]:
                        positioning_percent_closest_to_ball.append(float(item))
                    elif "positioning_percent_farthest_from_ball" in column_names_pro_all[index_item]:
                        positioning_percent_farthest_from_ball.append(float(item))
                    elif "positioning_avg_distance_to_ball_possession" in column_names_pro_all[index_item]:
                        positioning_avg_distance_to_ball_possession.append(float(item))
                    elif "positioning_avg_distance_to_ball_no_possession" in column_names_pro_all[index_item]:
                        positioning_avg_distance_to_ball_no_possession.append(float(item))
                    elif "positioning_avg_distance_to_ball" in column_names_pro_all[index_item]:
                        positioning_avg_distance_to_ball.append(float(item))
                    elif "positioning_avg_distance_to_mates" in column_names_pro_all[index_item]:
                        positioning_avg_distance_to_mates.append(float(item))

                    elif "positioning_percent_most_forward" in column_names_pro_all[index_item]:
                        positioning_percent_most_forward.append(float(item))
                    elif "positioning_percent_most_back" in column_names_pro_all[index_item]:
                        positioning_percent_most_back.append(float(item))
                    elif "positioning_time_most_forward" in column_names_pro_all[index_item]:
                        positioning_time_most_forward.append(float(item))
                    elif "positioning_time_most_back" in column_names_pro_all[index_item]:
                        positioning_time_most_back.append(float(item))

                    elif "movement_percent_high_air" in column_names_pro_all[index_item]:
                        movement_percent_high_air.append(float(item))
                    elif "movement_percent_supersonic_speed" in column_names_pro_all[index_item]:
                        movement_percent_supersonic_speed.append(float(item))


                # print(speed)

                variables = {'speed': speed, 'positioning_percent_behind_ball': positioning_percent_behind_ball,
                    'positioning_percent_infront_ball': positioning_percent_infront_ball, 'positioning_time_behind_ball': positioning_time_behind_ball,
                    'positioning_time_front_of_ball': positioning_time_front_of_ball, 'positioning_percent_closest_to_ball': positioning_percent_closest_to_ball,
                    'positioning_percent_farthest_from_ball': positioning_percent_farthest_from_ball, 'positioning_avg_distance_to_ball_possession': positioning_avg_distance_to_ball_possession,
                    'positioning_avg_distance_to_ball_no_possession': positioning_avg_distance_to_ball_no_possession, 'positioning_avg_distance_to_ball': positioning_avg_distance_to_ball,
                    'positioning_avg_distance_to_mates': positioning_avg_distance_to_mates, 'positioning_percent_most_forward': positioning_percent_most_forward,
                    'positioning_percent_most_back': positioning_percent_most_back, 'positioning_time_most_forward': positioning_time_most_forward,
                    'positioning_time_most_back': positioning_time_most_back, 'movement_percent_high_air': movement_percent_high_air,
                    'movement_percent_supersonic_speed': movement_percent_supersonic_speed}

                for key in variables:
                    item = variables[key]
                    # print(item)
                    team_dict[f"{'max_' + key}"], team_dict[f"{'min_' + key}"], team_dict[f"{'var_' + key}"], team_dict[f"{'avg_' + key}"]  = round(max(item), 2), round(min(item), 2), round(float(np.var(item)), 2), round(statistics.mean(item), 2)
                    # team_dict['max_' + key], team_dict['min_' + key], team_dict['var_' + key], team_dict['avg_' + key]  = max(item), min(item), np.var(item), statistics.mean(item)


                team_dict['pro'] = temp_pro_win[0]
                team_dict['winner'] = temp_pro_win[1]
                # print(team_dict)
            
                team_list.append(dict(team_dict))
                # print(team_list)

            # if index_team == 2: # Stop after 6 lines/players -> not neccesary if I use whole file -> just for testing
            #     break
    
    return team_list



if __name__ == "__main__":
    dictPro = getCSV('games_by_team_pro.csv')
    dictRanked = getCSV('games_by_team_ranked.csv')
    dictAll = getCSV('games_by_team_all.csv')

    ######### games_by_team_all_added_features ranked & pro
    with open('games_by_team_all_added_features.csv', 'w', newline='') as csvfile:
        all_keys = []
        for d in dictAll: # 3 players + new features + winner + pro
            for key in d.keys():
                print("key in csv ophalen")
                if key not in all_keys:
                    all_keys.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)

        writer.writeheader()
        for team in dictAll:
            print("dict all")
            writer.writerow(team)


    ######## make games_by_team_ranked_added_features
    with open('games_by_team_ranked_added_features.csv', 'w', newline='') as csvfile:
        all_keys = []
        for d in dictRanked: # 3 players + new features + winner + pro
            for key in d.keys():
                print("key dict ranked")
                if key not in all_keys:
                    all_keys.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)

        writer.writeheader()
        for team in dictRanked:
            print("dict ranked")
            writer.writerow(team)
    
    ######## make games_by_team_pro_added_features
    with open('games_by_team_pro_added_features.csv', 'w', newline='') as csvfile:
        all_keys = []
        for d in dictPro: # 3 players + new features + winner + pro
            for key in d.keys():
                print("key dict pro")
                if key not in all_keys:
                    all_keys.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)

        writer.writeheader()
        for team in dictPro:
            print("dict pro")
            writer.writerow(team)

