import sys, time
import HandleAPI as h_api
import HandleFiles as h_file


def print_leagues():
    """
    Prints the Soccer leagues to choose from.
    """
    leagues = h_api.get_leagues()
    print("")
    for l in leagues:
        print(" - " + l)
    print(" ")


def run_ui():
    print("Welcome to my WP4. Here you can see data visualizations of different soccer teams.")
    print("Fetching leagues...")
    # league_tups = print_leagues()[0]
    # printable_leagues = print_leagues()[1]

    # print(printable_leagues)
    print_leagues()

    league_input = input("What Socccer League do you want to analyze.\n" +
                         "Select a name from the menu above." +
                         "'Q' to exit:\n")

    while league_input != "Q":
        print(league_input)
        if league_input == "Premiership":
            league_id = 501
        elif league_input == "Superliga":
            league_id = 271
        else:
            print("incorrect league")
        print(h_api.get_standings(league_id))
        
        
        # Teams are found from league input
        # print(len(league_tups))
        # print(f"You have chosen {league_tups[int(league_input) - 1][1]}. Showing stats now.")
        # some functionality that I haven't implemented yet
        #print(h_api.get_data("teams").data)


        # TODO implement showing stats here

        # load data visualization

        # save data visulization
        # file_name = input("Enter a filename: ")
        # h_file.create_path(file_name)
        # store the loaded data visualziation






        league_input = input("What Socccer League do you want to analyze.\n" +
                         "Select a number from the dropdown Menu." +
                         "'Q' to exit:\n")


