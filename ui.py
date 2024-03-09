import HandleAPI as hapi
import HandleFiles as hfile
import VisualizeData as plot


def run_ui():
    """
    Function runs and handles much of the User interface for this program.
    """
    print("Welcome to my WP4. Powered by LastFM")

    user_in = input("Enter the name of an artist ('Q' to exit): ")
    while user_in != "Q":
        print(f"Cool, you selected: {user_in}")
        fm_obj = hapi.LastFM(user_in)
        fm_obj.set_apikey("0356663ee33a0a5d27428b1f63011652")
        fm_obj.load_data()
        VizualizeData = plot.VisualizeData()
        VizualizeData.set_data(fm_obj.play_list)
        VizualizeData.set_labels(fm_obj.names_list)
        VizualizeData.create_pie()
        hfile.create_png_folder()
        hfile.sort_file(VizualizeData.file_name)
        user_in = input("Enter the name of an artist ('Q' to exit): ")

