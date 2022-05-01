import crawl_movie_data
from RawMovieReview import RawMovieReview
from MovieReivew import MovieReivew

# run main
print("main")

# make movie review parser
rawMovieReview = RawMovieReview("samples.csv")

# make movie review filtered parser
movieReview = MovieReivew(10, "samples.csv")


