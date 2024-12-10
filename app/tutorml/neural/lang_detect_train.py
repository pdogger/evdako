import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential, load_model
from keras.layers import Dense


def predict_input(corpus):
    X = vectorizer.fit_transform(pd.Series(corpus))

    test_feat = pd.DataFrame(data=X.toarray(),columns=feature_names)
    # test_feat = (test_feat - train_min)/(train_max-train_min)

    result = model.predict(test_feat)
    label=np.argmax(result,axis=1)
    return encoder.inverse_transform(label)[0]


def encode(y):
    """
    Returns a list of one hot encodings
    """
    y_encoded = encoder.transform(y)
    y_dummy = np_utils.to_categorical(y_encoded)

    return y_dummy


def get_trigrams(corpus):
    #fit the n-gram model
    vectorizer = CountVectorizer(analyzer='char')

    X = vectorizer.fit_transform(corpus)

    #Get model feature names
    feature_names = vectorizer.get_feature_names()

    return feature_names


#Read in full dataset
data = pd.read_csv('tutorml/neural/sentences.csv',
                            sep='\t',
                            encoding='utf8',
                            index_col=0,
                            names=['lang','text'])

#Filter by text length
# len_cond = [True if 10<=len(s)<=200 else False for s in data['text']]
# data = data[len_cond]

#Filter by text language
lang = ['eng', 'fra', 'deu', 'ita', 'rus']
data = data[data['lang'].isin(lang)]

#Select 50000 rows for each language
data_trim = pd.DataFrame(columns=['lang','text'])

for l in lang:
    lang_trim = data[data['lang'] == l].sample(50000,random_state = 100)
    data_trim = data_trim.append(lang_trim)

#Create a random train, valid, test split
data_shuffle = data_trim.sample(frac=1)

train = data_shuffle[0:120000]
valid = data_shuffle[120000:180000]
test = data_shuffle[180000:250000]

#obtain trigrams from each language
features = {}
features_set = set()

for l in lang:
    #get corpus filtered by language
    corpus = train[train.lang==l]['text']
    #get 200 most frequent trigrams
    trigrams = get_trigrams(corpus)
    #add to dict and set
    features[l] = trigrams
    features_set.update(trigrams)


#create vocabulary list using feature set
vocab = dict()
for i,f in enumerate(features_set):
    vocab[f]=i

vectorizer = CountVectorizer(analyzer='char',
                            #  ngram_range=(2, 2),
                            vocabulary=vocab)

#create feature matrix for training set
corpus = train['text']
X = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names()

train_feat = pd.DataFrame(data=X.toarray(),columns=feature_names)

# #Scale feature matrix
# train_min = train_feat.min()
# train_max = train_feat.max()
# train_feat = (train_feat - train_min)/(train_max-train_min)

#Add target variable
train_feat['lang'] = list(train['lang'])

#create feature matrix for validation set
corpus = valid['text']
X = vectorizer.fit_transform(corpus)

valid_feat = pd.DataFrame(data=X.toarray(),columns=feature_names)
# valid_feat = (valid_feat - train_min)/(train_max-train_min)
valid_feat['lang'] = list(valid['lang'])

#create feature matrix for test set
corpus = test['text']
X = vectorizer.fit_transform(corpus)

test_feat = pd.DataFrame(data=X.toarray(),columns=feature_names)
# test_feat = (test_feat - train_min)/(train_max-train_min)
test_feat['lang'] = list(test['lang'])

#Fit encoder
encoder = LabelEncoder()
encoder.fit(lang)

#Get training data
x = train_feat.drop('lang',axis=1)
y = encode(train_feat['lang'])

#Define model
model = Sequential()
model.add(Dense(250, input_dim=len(vocab), activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(len(lang), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#Train model
model.fit(x, y, epochs=100, batch_size=512)
model.save("tutorml/neural/lang_detect_model")

pickle.dump(vectorizer, open("tutorml/neural/lang_detect_model/vectorizer.pkl", "wb"))
pickle.dump(encoder, open("tutorml/neural/lang_detect_model/encoder.pkl", "wb"))

x_test = test_feat.drop('lang',axis=1)
y_test = test_feat['lang']


#Get predictions on test set
predict_x=model.predict(x_test)
labels=np.argmax(predict_x,axis=1)
predictions = encoder.inverse_transform(labels)

#Accuracy on test set
accuracy = accuracy_score(y_test,predictions)
print("Точность модели на тестовых данных:", accuracy)

print("Распознанный язык:", predict_input(input("Введите фразу: ")))