def count_games(file_name): # (1) Count games
    game_counter = 0
    with open(file_name, "r") as file:
        for line in file.readlines():
            if len(line.replace("\n", "")) > 0:
                game_counter += 1
    return game_counter


def decide(file_name, year): 
    print("AAAAA")
    return "Not implemented yet :) "


def get_latest(file_name):
    return "Not implemented yet :) "


def count_by_genre(file_name, genre):
    return "Not implemented yet :) "


def get_line_number_by_title(file_name, title):
    return "Not implemented yet :) "


def sort_abc(file_name):
    return "Not implemented yet :) "


def get_genres(file_name):
    return "Not implemented yet :) "



def when_was_top_sold_fps(file_name):
    return "Not implemented yet :) "
