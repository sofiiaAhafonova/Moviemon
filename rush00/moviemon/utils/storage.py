import pickle

class Storage:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        """
        Loads the game data passed as parameters into the class instance.
        Returns the current instance.
        """
        pass

    def dump(self):
        """
        Returns the game data.
        """
        pass

    def get_random_movie(self):
        """
        Returns a Moviemon randomly among Moviemonsnot captured.
        """
        pass
    
    def load_default_settings(self):
        """
        Load the game data in the class instance sincethe settings. 
        Query and store the details of all Moviemons on IMDB. 
        Return the current instance.
        """
        pass
    
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
    
