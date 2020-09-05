# Printing functions
# from reports import *
import reports
import os

COUNT_GAMES_NUMER = 1
DECIDE_NUMBER = 2
GET_LATEST_NUMBER = 3
COUNT_BY_GENRE_NUMBER = 4


AVAILABE_FUNCTIONS_NUMBERS = [COUNT_GAMES_NUMER, DECIDE_NUMBER, GET_LATEST_NUMBER, COUNT_BY_GENRE_NUMBER]

def main():
    file_with_data = "game_stat.txt"
    print("Interactive printing module:")
    function_number = get_function_to_start()
    funtion_result = execute_function(function_number, file_with_data)
    print(f"Function result: {funtion_result}")


# This function decides which function to start
# 1 - count_games
# 2 - decide ...
def get_function_to_start():
    print_availble_functions()
    user_choice = int(input("Which function you want to execute? : "))

    if user_choice in AVAILABE_FUNCTIONS_NUMBERS:
        return user_choice

def execute_function(number, datafile):
    if number == COUNT_GAMES_NUMER:
        return reports.count_games(datafile)

    if number == DECIDE_NUMBER:
        return reports.decide(datafile, ask_for_a_year()) 

    if number == GET_LATEST_NUMBER:
        return reports.get_latest(datafile) 
    
    if number == COUNT_BY_GENRE_NUMBER:
        return reports.count_by_genre(datafile, ask_for_genre()) 

def ask_for_a_year():
    string_year = ask_for_argument("Give a year :")
    return int(string_year)

def ask_for_genre():
    genre = ask_for_argument("Give a genre :")
    return genre

def ask_for_argument(labal):
    #os.clear("cls || clear")
    return input(labal)


def print_availble_functions():
    print(f"({COUNT_GAMES_NUMER}) - Count games")
    print(f"({DECIDE_NUMBER}) - Decide")
    print(f"({GET_LATEST_NUMBER}) - Get latest")
    print(f"({COUNT_BY_GENRE_NUMBER}) - Count by genre")



if __name__ == "__main__":
    main()
