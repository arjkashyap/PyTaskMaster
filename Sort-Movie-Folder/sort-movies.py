import os
import requests
from bs4 import BeautifulSoup as bs


MOVIES_DIR = "E:\Movies"
MOVIES_LIST = os.listdir(MOVIES_DIR)     # list of movies names in movie_dir folder


def clean_prefix():
    """
    cleans out the prefix if the movie folder is already sorted
    """
    for movie in MOVIES_LIST:
        requires_rename = False
        old_name = os.path.join(MOVIES_DIR, movie)
        name_split = movie.split("-")
        n = len(name_split)
        i = 0
        while i < n and len(name_split[i]) == 3 and name_split[i].isnumeric():
            requires_rename = True
            i += 1
        print("new namesplit")
        if requires_rename:
            new_name = os.path.join(MOVIES_DIR, "".join(name_split[i:n]))
            os.rename(old_name, new_name)
                

def arrange_movies(movies_ratings):
    """
    :param movies_ratings: an ordered dict of ratings -> movie_name
    :return: nothing
    """
    prefix = 0              # '001_movie_name'
    for rating in movies_ratings:
        print(f"Movie: {movies_ratings[rating]} rating: {rating}")
        movie_name_old = movies_ratings[rating]
        movie_path_old = os.path.join(MOVIES_DIR, movie_name_old)
        movie_name_new = f"{prefix:03d}-{movie_name_old}"
        movie_path_new = os.path.join(MOVIES_DIR, movie_name_new)
        os.rename(movie_path_old, movie_path_new)
        prefix += 1

    print(f"{prefix} movies sorted")


def hash_movies(movies_list):
    """
    :param movies_list:
    :return: a dict of rating -> movie
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

    return dict(sorted(movie_ratings.items(), reverse=True))


def main():
    clean_prefix()
    print("Sorting Movies")
    ratings = hash_movies(MOVIES_LIST)
    arrange_movies(ratings)
    print("Done")


if __name__ == '__main__':
    main()


