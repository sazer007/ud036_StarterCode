class Movie():
    """Creates a instance of a move for the Fresh Tomatoes website.

    Args:
        movie_title: The name of the movie.
        movie_plot: A description of the movie.
        movie_poster: URL of the movie's poster/box art.
        movie_trailer. URL of the movie's trailer on YouTube.
    """
    def __init__(self, movie_title, movie_plot, movie_poster, movie_trailer):
        self.movie_title = movie_title
        self.movie_plot = movie_plot
        self.movie_poster = movie_poster
        self.movie_trailer = movie_trailer
