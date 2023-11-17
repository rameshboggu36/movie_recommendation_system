
# Movie Recommendation System

Implemented a content-based recommendation machine learning model focussed on recommending similar movies for the given movie.

You can checkout the app here:

[movie_recommendation_system_by_ramesh](https://movierecommendationsystem-ramesh.streamlit.app/)

#### Steps involved:
    1. Understanding the Data
    2. Exploratory Data Analysis
    3. Data Pre-Processing
    4. Vectorization
    5. Model Builiding

## Understanding the Data

Made use of two datasets _movies_, and its _credits_ of almost 5000 movies from kaggle.

You can find the datasets from below links:
1. [_credits_dataset_](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
2. [_movies_dataset_](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

movies dataset has columns like:

['budget', 'genres', 'homepage', __'id'__, 'keywords', 'original_language','original_title', 'overview', 'popularity', 'production_companies','production_countries', 'release_date', 'revenue', 'runtime','spoken_languages', 'status', 'tagline', __'title'__, 'vote_average',
'vote_count']

credits dataset has the following columns:

[__'movie_id'__, __'title'__, 'cast', 'crew']

Here both the datasets were combined on two rows: title and movie_id from __credits__, title and id from __movies__ dataset.

The combined dataset will be having almost 23 columns. We will not consider few columns which are not important for our analysis in the project.
Then for the combined dataset checked for any null values or duplicate values.After data pre-processing, we will end up with 4800 movies for the model.

## Exploratory Data Analysis (EDA)

EDA is one of the main part of the model implementation to know what the data can reveal beyond the model formation.

With the columns of the combined dataframe we can execute some analysis.

   Summary of EDA:

    Most Popular Movie: Minions with  875.58  popularity

    Highest Grossing Film: Avatar with almost  2.5Billion  dollars profit.

    Biggest Box Office Flop: The Lone Ranger with almost  165.71  dollars loss.

    Movies with Profit: Almost  54 % of total movies i.e.,  2585  have made the profits at box office.

    Average Vote Count: Most of the movies ( 32 %) got votes between ( 100−500 ).

    Average Rating: Most of the movies ( 3287 ) got on an average of rating between ( 5−7 ).

    Top Genre: Darama is the top genre with almost  2296  movies.

    Actor with most movies: Robert De Niro acted most movies as lead with almost  46  movies.
## Data Pre-Processing

After EDA, We process the data inorder to train the  model. 

We converted the given columns of cast, crew, keywords and overview by extracting related information.

Then created a new column, tags by adding all the columns.
## Model building

Then used countvectorizer to convert all the movie datapoints into vectors, i.e., text to vectors.

Using Cosinesimilarity on the vectors, we find the cosine distance of all points w.r.t each point.
We ended up having a multi dimentional array of size 4800 * 4800.

Then will take bottom 5 for each movie as there are more similar to the movie.
## Deployment

As the similarity file is very large, which has the distance of each movie with all the movies.

We don't need the distance of movie with all the movies, we just need the distance of movie with nearest 5 movies. 

So we just take those 5 movies and make a dictionary with movie titles as keys and the nearest 5 movies as their values.

We then use this dictionary to recommend the movies. 

Succesfully deployed the movie recommendation machine learning model on Streamlit.