import pdb

game_dictionary = {'home': {'team_name': 'Brooklyn Nets', 'colors': ['Black', 'White'],
           'players':
           {'Alan Anderson': {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1},
           'Reggie Evans': {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7},
           'Brook Lopez': {'number': 11, 'shoe': 17, 'points': 17, 'rebounds':  19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15},
           'Mason Plumlee': {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5},
           'Jason Terry': {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1}}},
'away': {'team_name': 'Charlotte Hornets', 'colors': ['Turquoise', 'Purple'], 'players':
            {'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2},
            'Bismak Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10},
            'DeSagna Diop': {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5},
            'Ben Gordon': {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0},
            'Brendan Haywood': {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists':12, 'steals':22, 'blocks': 5, 'slam_dunks': 12}}}}

def Hello():
    print("Hello")
    return "Good Morning"

def game_dict():
    return game_dictionary

def num_points_scored(name):
    player = player_stats(name)
    return player['points']


def shoe_size(name):
    return player_stats(name)['shoe']
#    player = player_stats(name)
#    return player['shoe']

def team_colors(team):
   for team_stat in game_dict().values():
       if team_stat['team_name'] == team:
           return team_stat['colors']


def team_names():
    teams= []
    for team_stat in game_dict().values():
        teams.append(team_stat['team_name'])
    return teams


def player_numbers(team):
#iterate through team and send player into player_stat function to get numbers
    team_num = []
#    for location, team_stat in game_dict().items():
    for team_stat in game_dict().values():
        if team_stat['team_name'] == team:
            for person in team_stat['players']:
                team_num.append(player_stats(person)['number'])
    return team_num
# if value in stats.values()

def player_stats(player):
#    all_players = {k:v for (k,v) in game_dict().items()}
    all_players = {}
#    for location, team_stat in game_dict().items():
    for team_stat in game_dict().values():
       all_players.update(team_stat['players'])
#       pdb.set_trace()
    return all_players[player]

def big_shoe_rebound():
#find player with biggest shoe size using player stats
    really_big_shoe = max(all_players_in_game(), key = lambda shoe: shoe_size(shoe))
    # everyone = all_players_in_game()
    # biggest = 0
    # player = None
    # for person in everyone:
    #     if shoe_size(person) >= biggest:
    #         biggest = shoe_size(person)
    #         player = person
            # print (player)
            # print(biggest)
    big_man = {really_big_shoe: player_stats(really_big_shoe)['rebounds']}
    return big_man
#    big_man = {person: biggest}
#    print (big_man)
#        if person['shoe']

def all_players_in_game():
    all_players = {}
    for team_stat in game_dict().values():
         all_players.update(team_stat['players'])
    #       pdb.set_trace()
    return all_players

def most_points_scored():
#    everyone = all_players_in_game()
#    top_score = 0
#    player = None
    top_scorer = max(all_players_in_game(), key = lambda sc: num_points_scored(sc))
    # for person in everyone:
    #     if num_points_scored(person) >= top_score:
    #         top_score = num_points_scored(person)
    #         player = person
    # top_scorer = {player: top_score}
    return top_scorer


def player_with_longest_name():
#    everyone = all_players_in_game().keys()
    longest_name = 0
    long_name_player= None
    for player in all_players_in_game().keys():
    #    pdb.set_trace()
         if len(player) > longest_name:
             longest_name = len(player)
             long_name_player = player
    return long_name_player

def winning_team():
    home_score =0
    away_score = 0
    for player in all_players_in_game():
        if player in game_dict()['home']['players']:
#            print("home " + player)
            home_score += num_points_scored(player)
#            print (home_score)
        else:
#            print("away " + player)
            away_score += num_points_scored(player)
#            print (away_score)
    if home_score > away_score:
        return "Winner is: " + team_names()[0]
    if home_score < away_score:
        return "Winner is: " + team_names()[1]
    else:
        return "It's a Tie!?"

def long_name_steals_a_ton():
    long_name = player_with_longest_name()
    for player in all_players_in_game():
        if player_stats(long_name)['steals'] <= player_stats(player)['steals']:
            return False
        else:
            return True

    # for team in teams:
    #     score.append(sum(player_stats(team['player'])))
    # return score



#hello = Hello()
#print(team_colors('Brooklyn Nets'))
#print(team_names())
#print(player_stats('Jason Terry'))
#print(shoe_size('Ben Gordon'))
#print(num_points_scored('Reggie Evans'))
#print(player_numbers('Charlotte Hornets'))
#print(big_shoe_rebound())
#print(most_points_scored())
print(winning_team())
#print(all_players_in_game().keys())
#print(player_with_longest_name())
print(long_name_steals_a_ton())
