import requests
import time
import csv

token = "5rJrtU5yJZEyshaPvpeJ5TuxlmgrnIFZqOg3tiQ8"
token2 = "YoufJJJKGDJc4chY6mK2Qfuk94NE06kyaNR0WiWM"
replay_id = "93441ec7-8c9b-45f3-b1a7-da6b3d3ee1ad"
replay_id2 = "35a53d71-d7f0-494b-b88a-9285b79a1f90"
replay_id3 = "105a245c-bc72-4a9c-9c4e-4d845af694af"
replay_id4 = "d1fe5bbc-e5e1-48e2-8279-a23cec9655ac"
replay_id_pro = "15f12bd9-f4a6-4cea-a2dc-610cd9dd976b"
filter = "?season=f4&min-rank=champion-1&max-rank=grand-champion-2&playlist=ranked-standard&count=200" # max 200

filter1 = "?season=f4&min-rank=champion-1&max-rank=champion-1&playlist=ranked-standard&count=1" # max 200
filter2 = "?season=f4&min-rank=champion-2&max-rank=champion-2&playlist=ranked-standard&count=1" # max 200
filter3 = "?season=f4&min-rank=champion-3&max-rank=champion-3&playlist=ranked-standard&count=1" # max 200
filter4 = "?season=f4&min-rank=grand-champion-1&max-rank=grand-champion-1&playlist=ranked-standard&count=1" # max 200
filter5 = "?season=f4&min-rank=grand-champion-2&max-rank=grand-champion-2&playlist=ranked-standard&count=1" # max 200
# filter6 = "?season=f4&min-rank=grand-champion-3&max-rank=grand-champion-3&playlist=ranked-standard&count=1" # max 200
## Doesn't this get the whole replay? -> that I shouldn't get the ID's and then retrieve per item, but I might be able to retrieve per 200


team_data_list = [
    '_id', '_created', '_rocket_league_id', '_playlist_id', '_duration', '_overtime', '_season', '_season_type', 
    '_date', 'min_rank_id', 'min_rank_name', 'max_rank_id', 'max_rank_name'
]

column_names_rank = [
    'game_id', '_created', '_rocket_league_id', '_playlist_id', '_duration', '_overtime', '_season', 
    '_season_type', '_date', 'min_rank_id', 'min_rank_name', 'max_rank_id', 'max_rank_name', 'color',
    'players_end_time', "player_tag", "movement_avg_speed", "movement_total_distance", "movement_time_supersonic_speed",
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

column_names_pro = ["movement_avg_speed", "movement_total_distance", "movement_time_supersonic_speed",
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

def get_data(endpoint_url, token): # get data with url from ballchasing.com
    for round in range(1, 4000):
        try:
            r = requests.get(endpoint_url, headers={'Authorization': token})
            r.raise_for_status()
            return r.json() 
        except requests.exceptions.RequestException as e:
            time.sleep(0.6)
            print("toofast")
            if round % 5 == 0:
                print("sleep")
                time.sleep(1)
            raise

def get_replay(replay_id, token):
    # time.sleep(0.0625)
    get_url = f"https://ballchasing.com/api/replays/{replay_id}" # replay id or filter for game_id's
    return get_data(get_url, token)


def getGameId(filter, token, rounds=0, id_list = []): # just game_id's for getting complete games
    if rounds == 105: # 90 * 200 is enough # update is was not enough 105 * 200 should be
        return id_list
    
    data = get_replay(filter, token)
    matches = data["list"]
    for i, item in enumerate(matches):
        # print("game_id",i)
        if "season" in filter:
            id_list.append({"game_id": item["id"]})
        else:
            id_list.append(item)

    next = data["next"].split('/replays')[1]
    return getGameId(next, token, rounds + 1, id_list)
            

def getData(data, cat = "", indent = 0): # recursive to get all the data in a list with a key + item
    index = 1
    list_returned = []
    for key, item in data.items():
        if isinstance(item, str) or isinstance(item, int) or isinstance(item, float):
            list_returned.append({cat + "_" + key: item}) #### append to list
        elif isinstance(item, list):
            list_returned.append({"list": key})
            for i in item:
                list_return = getData(i, key, indent+1)
                if list_return is None:
                    print("None to see here")
                else:
                    for list_item in list_return:
                        list_returned.append(list_item) #### append to list
        elif isinstance(item, dict):
            dict_return = getData(item, key, indent+1)
            list_returned.append({"dict": key})

            if dict_return is None:
                print("None to see here")
            else: 
                for dict_item in dict_return:
                    list_returned.append(dict_item) #### append to list
        else:
            print("----------------------------------------------")
            print(key, item, type(item))
            print("----------------------------------------------")
        
        if index == len(data.items()):
            return list_returned
        index += 1


def sortData(data): # sort data in the right format for the CSV
    complete_match_data = data
    nine_data_chuncks = [[],[],[],[],[],[],[],[],[]]
    index_chunk = 0
    score = [] # all the scores to extract which team is the winner
    first_team_win = True
    players_dict = [{},{},{},{},{},{}]

    for item in complete_match_data:
        # save scores of players and teams
        if 'core_goals' in item:
            score.append(item)

        if 'players_start_time' in item:
            index_chunk += 1
        elif item == {'dict': 'ball'}:
            index_chunk += 1

        if list(item.keys())[0] in column_names_rank:
            if list(item.keys())[0] == 'min_rank_id' or list(item.keys())[0] == 'max_rank_id':
                if item == 'grand-champion':
                    nine_data_chuncks[index_chunk].append({'min_rank_id': 'grand-champion-1'})
                elif item == 'grand-champion':
                    nine_data_chuncks[index_chunk].append({'max_rank_id': 'grand-champion-1'})
                else:
                    nine_data_chuncks[index_chunk].append(item)
            else:
                nine_data_chuncks[index_chunk].append(item)
        elif list(item.keys())[0] == '_id':
            # print(list(item.keys())[0], item["_id"])
            nine_data_chuncks[index_chunk].append({'game_id': item["_id"]})
        elif list(item.keys())[0] == "players_name":
            nine_data_chuncks[index_chunk].append({'player_tag': item["players_name"]})
        # elif list(item.keys())[0] == "players_end_time":
        #     nine_data_chuncks[index_chunk].append({'players_end_time': item["players_end_time"]})

    if len(nine_data_chuncks) != 9:
        return []

    # decide if first or second team won the game, by team scores and not player scores -> don't need the "two_teams"
    if len(score) != 8:
        return []

    if score[3]['core_goals'] < score[7]['core_goals']:
        first_team_win = False

    # split team vs player info
    game_info = nine_data_chuncks[0] # save upload and team data into team_info
    del nine_data_chuncks[8], nine_data_chuncks[4], nine_data_chuncks[0] # delete upload and team data from "nine_data_chuncks"

    # add who won and who lost and add that to players
    for i, player in enumerate(nine_data_chuncks):
        if i < 3:
            for game_info_item in game_info:
                key = next(iter(game_info_item)) # first key from the dictionary
                players_dict[i][f"{key}"] = game_info_item[key]
            players_dict[i]['color'] = "blue"
            for item in player:
                if 'player_tag' in item:
                    key = next(iter(item)) # first key from the dictionary
                    players_dict[i]["player_tag"] = item[key]
                else:
                    key = next(iter(item)) # first key from the dictionary
                    players_dict[i][f"{key}"] = round(float(item[key]), 2)
            players_dict[i]['pro'] = False # these are all not pro games -> should put this in teams and pro games too
            players_dict[i]['winner'] = first_team_win
        else: 
            for game_info_item in game_info:
                key = next(iter(game_info_item)) # first key from the dictionary
                players_dict[i][f"{key}"] = game_info_item[key]
            players_dict[i]['color'] = "orange"
            for item in player:
                if 'player_tag' in item:
                    key = next(iter(item)) # first key from the dictionary
                    players_dict[i]["player_tag"] = item[key]
                else:
                    key = next(iter(item)) # first key from the dictionary
                    players_dict[i][f"{key}"] = round(float(item[key]), 2)
            players_dict[i]['pro'] = False # these are all not pro games
            players_dict[i]['winner'] = not first_team_win

    for index_player, player in enumerate(players_dict):
        if list(player.keys()) == column_names_rank:
            # print("Great!")
            pass
        else:
            print("not good", players_dict[index_player])
            del players_dict[index_player]

    return players_dict


if __name__ == "__main__":
    id_codes = getGameId(filter, token) # find 200 * 90 game id's

    # id_codes_pro = getProReplayID()
    # dict1 = get_replay(replay_id3, token) # uses api
    # sortedDict = sortData(getData(dict1)) # uses data from api but from dict1 
    # print(sortData(getData(replay)))

    ##########################################
    
    game_ids = []

    with open('game_id_API_ranked.csv', newline='') as csvfile:
        game_reader = csv.reader(csvfile, delimiter=',')

        for index_id_row, id_row in enumerate(game_reader):
            if index_id_row == 0: # row 0 is column names
                for header in id_row:
                    print(header)
            else:
                game_ids.append(id_row[0])
                # print(id_row[0])
                # print("added game id", index_id_row)

    print(len(game_ids))
    # print(id_codes)

    with open('game_id_API_ranked.csv', 'a', newline='') as csvfile: # w for (over)write, a for append/add new to already existing data
        writer = csv.DictWriter(csvfile, fieldnames=["game_id"])
        # writer.writeheader()

        for code in id_codes:
            if code["game_id"] in game_ids:
                # print("id already in database", i)
                # print(code)
                pass
            else:
                writer.writerow(code)

#################################################################################################

    id_list = []

    with open('game_id_API_ranked.csv', newline='') as csvfile:
        game_id_reader = csv.reader(csvfile, delimiter=',')

        for index_id_row, id_row in enumerate(game_id_reader):
            if index_id_row == 0: # row 0 is column names
                for header in id_row:
                    print(header)
            else:
                for i, id_item in enumerate(id_row):
                    print("ronde:",index_id_row,"nr:", i)
                    id_list.append(id_item)

    game_ids = []

    with open('games_by_players_API_ranked3.csv', newline='') as csvfile:
        game_reader = csv.reader(csvfile, delimiter=',')

        for i, row in enumerate(game_reader):
            if index_id_row == 0: # row 0 is column names
                for header in id_row:
                    print(header)
            else:
                game_ids.append(row[0])
                print("added game id", i)

    with open('games_by_players_API_ranked3.csv', 'a', newline='') as csvfile: # w for (over)write, a for append/add new to already existing data
        fieldnames = column_names_rank
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
     #   writer.writeheader() # only first time?

        used_code = 0

        for i, code in enumerate(id_list):
            if code in game_ids:
                print("id already in database", i)
                print(code)
                pass
            else:
                used_code += 1
                print("used code try to CSV:", used_code)
                print(code)
                replay = get_replay(code, token)
                sortedDict = sortData(getData(replay))
                for player in sortedDict:
                    print("added player:", player["player_tag"])
                    writer.writerow(player) # 'game_id':%20'22b72e75-2490-4393-9196-6571d0e4a246'%7D -> 'just wants the ID' -> id_list

#####################################################################################################################

    all_data_new_rank = []

    with open('games_by_players_API_ranked3.csv', newline='') as csvfile: ## just for grand-champion -> grand-champion-1
        game_reader = csv.reader(csvfile, delimiter=',')

        for i, row in enumerate(game_reader):
            # 9 10 11 12
            if row[9] == 'grand-champion':
                print("changed row 9")
                row[9] = 'grand-champion-1'
            if row[11] == 'grand-champion':
                print("changed row 11")
                row[11] = 'grand-champion-1'
            complete_row = {}
            for index, item in enumerate(row):
                complete_row[column_names_rank[index]] = item
            all_data_new_rank.append(complete_row)
            print("added game to list", i)

    with open('games_by_players_API_ranked2.csv', 'w', newline='') as csvfile: ## just for grand-champion -> grand-champion-1
        fieldnames = column_names_rank
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader() # only first time?

        for i, row in enumerate(all_data_new_rank):
            writer.writerow(row)
            print("added game to CSV", i)