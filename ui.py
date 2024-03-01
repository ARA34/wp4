import sys


def print_leagues():
    """
    Prints the Soccer leagues to choose from.
    """
    print("Liga MX - 1")
    print("Premier League - 2")
    print("La Liga - 3")
    print()


def run():
    print("Welcome to my WP4. Here you can see data visualizations of different soccer teams.")
    league_input = input("What Socccer League do you want to analyze.\n" +
                         "Select a number from the dropdown Menu." +
                         "'Q' to exit:\n")
    while league_input != "Q":
        # Teams are found from league input
        pass


