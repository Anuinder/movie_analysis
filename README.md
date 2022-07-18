# movie_analysis

Analyzing the TMDb dataset for various primary and critical features.

#### Requirements
* Install the [Anaconda](https://www.anaconda.com/products/distribution) distribution of Python. It already has required packages, namely, NumPy, panadas, matplotlib included. 
* Data set: [Tmdb movie dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

#### Details
The dataset provides both basic information related to a movie and useful information like ratings, revenue, runtime, etc. 
* The columns ‘homepage’ and ‘tagline’ are dropped as they contain a significant amount of null values.
* Dropped the ‘overview’ and ‘movie_id’ columns as they are not required.
* Extract year as release_year from the release_date column.
* Extract earnings as profit_loss using revenue and budget column.

Some of the points analyzed are mentioned below
* Number of movies released year by year.
* Trends of parameters – runtime, profit, popularity, budget over the years.
* Most commonly used genre for movies over the years.
* Most common genre every decade over the given period of years
* Most filmed actors, production companies over the given period of time
* Countries which max releases over the given period of time
* Relationships between budget and popularity, revenue and popularity, profit and popularity, runtime and popularity, votes and popularity.
* Revenue trends for the movies based on the budget associated with them
* The 10 most popular movies over the given period of time

