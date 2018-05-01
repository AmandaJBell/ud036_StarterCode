import fresh_tomatoes
import media

# Create instances of the Movie class, which represent specific movies.
mean_girls = media.Movie("Mean Girls",
                         ("After spending her childhood in Africa, Cady has no"
                          "idea how wild things can be at an American highs "
                          "school."),
                         "https://bit.ly/2wcd1A7",
                         "https://www.youtube.com/watch?v=KAOmTMCtGkI")

roman_holiday = media.Movie("Roman_Holiday",
                            ("Overwhelmed by her suffocating schedule, touring"
                             " European princess Ann (Audrey Hepburn) takes"
                             " off for a night while in Rome."),
                            "https://bit.ly/2FvXb2w",
                            "https://www.youtube.com/watch?v=9GzCG6lpFUw")
bring_it_on_3 = media.Movie("Bring it On 3",
                            ("When her father gets laid off, Britney Allen"
                             " has to drop out and transfer to her ritzy high"
                             " school's underfunded crosstown rival."),
                            "https://bit.ly/2HNGRw9",
                            "https://www.youtube.com/watch?v=go3ELJdpkx4")
oceans_8 = media.Movie("Ocean's 8",
                       ("Criminal mastermind Debbie Ocean and seven other"
                        " female thieves try to pull off the heist of the"
                        " century at New York's annual Met Gala."),
                       "https://bit.ly/2HEeXGx",
                       "https://www.youtube.com/watch?v=MFWF9dU5Zc0")
crazy_rich_asians = media.Movie("Crazy Rich Asians",
                                ("Rachel Chu is surprised to learn that her"
                                 "  boyfriend's family is extremely wealthy,"
                                 " after accompying him to a wedding in"
                                 " Singapore."),
                                "https://bit.ly/2jk1EfX",
                                "https://www.youtube.com/watch?v=WDhwEqxKCss")
step_up = media.Movie("Step Up",
                      ("A gifted ballet student convinces a troubled boy to"
                       " help her with her dance routines and the sparks fly"),
                      "https://bit.ly/29mODQg",
                      "https://www.youtube.com/watch?v=ZgnmCqA25-o")

movies = [roman_holiday, bring_it_on_3, mean_girls, oceans_8, step_up,
          crazy_rich_asians]

# Render and open the movie website in the browser.
fresh_tomatoes.open_movies_page(movies)
