import sys, time
import HandleAPI as h_api


def print_leagues():
    """
    Prints the Soccer leagues to choose from.
    """
    output = ""
    leagues = h_api.get_leagues()
    leagues_enum = list(enumerate(leagues, start=1))
    for league_tup in leagues_enum:
        pos = league_tup[0]
        name = league_tup[1]
        output += f"{name} - ({pos})\n"
    output = output[:-1]
    return leagues_enum, output


def run_ui():
    print("Welcome to my WP4. Here you can see data visualizations of different soccer teams.")
    print("Fetching leagues...")
    league_tups = print_leagues()[0]
    printable_leagues = print_leagues()[1]
    print(printable_leagues)
    league_input = input("What Socccer League do you want to analyze.\n" +
                         "Select a number from the menu above." +
                         "'Q' to exit:\n")

    while league_input != "Q":
        # Teams are found from league input
        print(len(league_tups))
        print(f"You have chosen {league_tups[int(league_input) - 1][1]}. Showing stats now.")
        # some functionality that I haven't implemented yet
        league_input = input("What Socccer League do you want to analyze.\n" +
                         "Select a number from the dropdown Menu." +
                         "'Q' to exit:\n")


