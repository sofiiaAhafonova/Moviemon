import pickle
import requests
import os

class Storage:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self, file_name=None):
        """
        Loads the game data passed as parameters into the class instance.
        Returns the current instance.
        """
        data = {}
        self.file_name = file_name if file_name is not None else self.file_name
        try:
            with open(self.file_name, 'rb') as file:
                pickle.dump(data, file)
        except Exception as e:
            print(e)
        return data

    def dump(self, game_data):
        """
        Returns the game data.
        """
        pass

    def get_random_movie(self):
        """
        Returns a Moviemon randomly among Moviemons not captured.
        """
        pass
    
    def load_default_settings(self):
        """
        Load the game data in the class instance since the settings. 
        Query and store the details of all Moviemons on IMDB. 
        Return the current instance.
        """
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        game_data = {
            'length': 10,
            'height': 10,
            'x': 0,
            'y': 0,
            'movieball': 10,
            'moviemon_db': load_moviemons(),
            'captured_moviemons': [],
            'captured_moviemons_nb': 0,
        }
        self.dump(game_data)


    
    def get_strength(self):
        """
        Returns the player's strength.
        """
        pass

    def get_movie(self, moviemon_name):
        """
        Returns a Python dictionary containing all the details
        since the name of the Moviemon passed in parameter and necessary to the Detail page.
        """
        pass
    

def load_moviemons():
    movie_ids = ['tt0110912', 'tt0068646', 'tt0137523', 'tt1213644', 'tt0811138', 'tt0432291', 'tt6892400', 'tt0432291', 'tt0482571', 'tt8772262', 'tt1386697', 'tt2294629', 'tt7343762']
    moviemons = []
    for movie_id in movie_ids:
        url = f'http://www.omdbapi.com/?i={movie_id}&apikey=fa513f2c'
        try:
            moviemon = requests.get(url).json()
            moviemons.append(moviemon)
        except Exception as e:
            print(e)
    return moviemons

if __name__ == "__main__":
    moviemons = load_moviemons()
    for each in moviemons:
        print(each['Title'])
