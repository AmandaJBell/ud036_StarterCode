import webbrowser


class Movie():
    """This class provides a way to store movie related information

    Attributes:
        title (str): The title of the movie
        storyline (str): A brief description of the movie plot
        poster_image_url (str): The url of the poster image
        trailer_youtube_url (str): The url of the movie trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the link to the movie trailer in the webbrowser."""

        webbrowser.open(self.trailer_youtube_url)
