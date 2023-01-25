import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv('film/data-film-fix-preprocesing.csv',encoding='utf-8')

cv = CountVectorizer()
word_count_vector = cv.fit_transform(data['Clean Review'])

tf = pd.DataFrame(word_count_vector.toarray(), columns = cv.get_feature_names_out())

tf.to_csv('data-film-fix-tf.csv',index=False)