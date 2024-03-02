from models import RandomForestClassifier
from utils import find_reviews, save_csv
movie_imdb_url = input("please enter IMDB URL of the movie: ").strip()
model=RandomForestClassifier()
reviews=find_reviews(movie_imdb_url)
sentiments = []
for review in reviews:
    sentiment = model.predict(review)
    sentiments.append(sentiment)
save_csv(reviews, sentiments)