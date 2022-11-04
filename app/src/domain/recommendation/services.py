from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from pythainlp.corpus import thai_stopwords
import pandas as pd

from ..places.information.model import PlaceInformation
from ..places.place.services import get_place_with_fee

STOP_WORDS = list(thai_stopwords())


def find_cosine_similarity(bag_of_words):
    tf = TfidfVectorizer()
    tfidf_matrix = tf.fit_transform(bag_of_words)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    return cosine_similarities


def recommendations(id, df, top_n=10):
    indices = pd.Series(df.index)
    bag_of_words = df["bag_of_words"].astype(str)
    cosine_similarities = find_cosine_similarity(bag_of_words)

    recommended_places = []
    idx = indices[indices == id].index[0]
    score_series = pd.Series(
        cosine_similarities[idx]).sort_values(ascending=False)
    top_indexes = list(score_series.iloc[1:top_n+1].index)

    for i in top_indexes:
        recommended_places.append(list(df.index)[i])

    return recommended_places


def get_content_based_data(db: Session):
    result = db.query(
        PlaceInformation.place_id,
        PlaceInformation.bag_of_words
    ).all()

    df = pd.DataFrame.from_records(
        result,
        columns=['id', 'bag_of_words']
    )

    df.set_index('id', inplace=True)
    recommendation_id_list = recommendations('P03006845', df)

    recommendation_list = [get_place_with_fee(db, place_id, 'th')
                           for place_id in recommendation_id_list]

    return recommendation_list
