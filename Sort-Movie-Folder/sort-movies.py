import os
import requests
from bs4 import BeautifulSoup as bs
import collections


MOVIES_DIR = "E:\Movies"
MOVIES_LIST = os.listdir(MOVIES_DIR)     # list of movies names in movie_dir folder

def arrange_movies(movies_ratings):
    """
    :param movies_ratings: an ordered dict of ratings -> movie_name
    :return:
    """
    for i in range(len(movies_ratings)):
        print(f"Movie: {movies_ratings[i][1]}, rating: {movies_ratings[i][0]}")
    pass


def hash_movies(movies_list):
    """
    :param movies_list:
    :return: an ordered dict of rating -> movie
    """

    movie_ratings = {}  # dict: rating -> movie name

    for movie in movies_list:
        search = "+".join(movie.split(" ")) + "+imdb"
        results = 1  # number of search results required
        page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
        soup = bs(page.content, "html5lib")
        imdb_url = ""    # imdb link of the movie
        links = soup.findAll("a")
        for link in links:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                link = link.get('href').split("?q=")[1].split("&sa=U")[0]

                # check if the link contains imdb
                if "imdb" in link:
                    print(f"{movie} Link: " + link)
                    imdb_url = link
                    break
        # find rating
        try:
            movie_page = requests.get(imdb_url)
            movie_soup = bs(movie_page.content, "html5lib")
            rating = float(movie_soup.find_all(attrs={'itemprop': 'ratingValue' })[0].text.strip())
            movie_ratings[rating] = movie
            print(rating)
        except Exception as e:
            print("Error in finding movie rating: ", movie)
            print(e)
    return collections.OrderedDict(sorted(movie_ratings.items(), reverse=True))


def main():
    print("Sorting Movies")
    ratings = hash_movies(MOVIES_LIST)
    print("I came from main")
    print(ratings)
    arrange_movies()
    print(ratings)


if __name__ == '__main__':
    main()


