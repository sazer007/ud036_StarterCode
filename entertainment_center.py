"""This module is used to create movie objects. Each movie takes a title, plot, poster, and YouTube trailer."""
import fresh_tomatoes
import media


#We are creating an instance of the class movie for Shaun of the Dead.
#It contains all of the infor we are storing for it (title, rating, plot, etc.).
shaun_of_the_dead = media.Movie("Shaun of the Dead",
                                "A British romantic comedy. With zombies.",
                                "http://www.gstatic.com/tv/thumb/movieposters/34914/p34914_p_v8_ae.jpg",
                                "https://www.youtube.com/watch?v=z-lmF5DAssU")

#Creating an instance of the movie Hot Fuzz
hot_fuzz = media.Movie("Hot Fuzz",
                       "A police officer moves from the big city to rural England.",
                       "http://www.gstatic.com/tv/thumb/movieposters/163411/p163411_p_v8_ad.jpg",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4")

#Creating an instance of the movie Guardians of the Galaxy
guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "A band of space misfits join together to save the galaxy.",
                                      "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                                      "https://www.youtube.com/watch?v=d96cjJhvlMA")

#Creating an instance of the movie Kingsman: The Secret Service
kingsman = media.Movie("Kingsmen: The Secret Service",
                       "A teen is recruited for an organization that fights international threats.",
                       "http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-N4gVBmixzAXvGfZ",
                       "https://www.youtube.com/watch?v=m4NCribDx4U")

#Creating an instance of the movie Goodfellas
goodfellas = media.Movie("Goodfellas",
                         "A story about the rise and fall of gangster Henry Hill.",
                         "https://ae01.alicdn.com/kf/HTB1rE0TSXXXXXbYXVXXq6xXFXXXZ/DIY-frame-font-b-GOODFELLAS-b-font-CLASSIC-font-b-MOVIE-b-font-font-b-POSTER.jpg",
                         "https://www.youtube.com/watch?v=2ilzidi_J8Q")

#Creating an instance of the movie Deadpool
deadpool = media.Movie("Deadpool",
                       "A merc with a mouth has his cancer cured... for a price.",
                       "http://www.impawards.com/2016/posters/deadpool_ver4.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

#The movie objects are put into a list
movies = [shaun_of_the_dead,
          hot_fuzz,
          guardians_of_the_galaxy,
          kingsman,
          goodfellas,
          deadpool]

#This function uses the movies list to populate the web page
fresh_tomatoes.open_movies_page(movies)
