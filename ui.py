import HandleAPI as hapi
import HandleFiles as hfile


def run_ui():
    print("Welcome to my WP4. Powered by LastFM")

    user_in = input("Enter the name of an artist ('Q' to exit): ")
    while user_in != "Q":
        print(f"Cool, you selected: {user_in}")
        fm_obj = hapi.LastFM(user_in)
        fm_obj.set_apikey("0356663ee33a0a5d27428b1f63011652")
        fm_obj.load_data()
        # print(fm_obj.data)
        print(fm_obj.names_list)
        print(fm_obj.play_list)

        user_in = input("Enter the name of an artist ('Q' to exit): ")

