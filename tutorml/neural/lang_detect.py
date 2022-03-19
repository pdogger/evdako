import numpy as np
import pandas as pd
import pickle
from keras.models import load_model

def predict_input(corpus):
    languages = {'eng': 'английский', 'fra': 'французский', 'deu': 'немецкий',
                 'ita': 'итальянский', 'rus': 'русский'}
    encoder = pickle.load(open("tutorml/neural/lang_detect_model/encoder.pkl", "rb"))
    vectorizer = pickle.load(open("tutorml/neural/lang_detect_model/vectorizer.pkl", "rb"))
    X = vectorizer.fit_transform(pd.Series(corpus))

    test_feat = pd.DataFrame(data=X.toarray(),columns=vectorizer.get_feature_names())

    model = load_model("tutorml/neural/lang_detect_model")
    result = model.predict(test_feat)
    label = np.argmax(result, axis=1)
    prob = format(np.amax(result, axis=1)[0] * 100, '.2f')
    lang = languages[encoder.inverse_transform(label)[0]]

    return lang, prob
