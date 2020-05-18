from sklearn.neighbors import KNeighborsClassifier
from grading_algo.data_prep import get_features
import pandas as pd

'upload processed dataset and split into labels and features - may have to edit file path for your location of essay_train'
t_data = pd.read_csv("C:/Users/jswon/PycharmProjects/autograder/grading_algo/essay_train.csv")
t_features = t_data[['sent_count', 'word_count', 'avg_sent_length']]
t_labels = t_data.loc[:, 'grade']

'fit model with data'
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(t_features, t_labels)

'grade inputted essay according to fitted model = grade ranges from letter grades A-D (no pluses or minuses)'


def grade_essay(essay):
    (n_s, n_w, a_s) = get_features(essay)

    grade = knn_model.predict([[n_s, n_w, a_s]])

    if grade[0] == 0:
        l_grade = 'D'
    elif grade[0] == 1:
        l_grade = 'C'
    elif grade[0] == 2:
        l_grade = 'B'
    elif grade[0] == 3:
        l_grade = 'A'

    return l_grade

