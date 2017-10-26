from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import sys
import os

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print (" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

def train_topic_model():
    #dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))


    CORPUS_PATH = os.path.join('data', 'Model_Training')

    filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

    print(filenames)

    vectorizer = CountVectorizer(input='filename', stop_words='english', min_df=20)

    dtm = vectorizer.fit_transform(filenames).toarray()

    vocab = np.array(vectorizer.get_feature_names())

    print (dtm.shape)
    print (vocab.shape)
    sys.exit()

    documents = dataset.data

    no_features = 1000

    # NMF is able to use tf-idf
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(documents)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()

    # LDA can only use raw term counts for LDA because it is a probabilistic graphical model
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(documents)
    tf_feature_names = tf_vectorizer.get_feature_names()

    no_topics = 20

    # Run NMF
    nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

    # Run LDA
    lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

    no_top_words = 10
    display_topics(nmf, tfidf_feature_names, no_top_words)
    display_topics(lda, tf_feature_names, no_top_words)

train_topic_model()