import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

data = pd.read_csv('data-film-fix.csv',encoding='utf-8')

def clean(text):
  # Menjadikan Setiap Kalimat Menjadi Huruf Kecil / Lower Text
  a = text.lower()

  # Menghapus Tanda Baca, Angka dan Kata Yang Tidak di Perlukan
  b = re.sub('[^A-Za-z]+', ' ', a)

  # Melakukan Tokenisasi
  b = word_tokenize(b)

  # Menghapus stop words
  english_stopwords = stopwords.words('english')

  tokens_wo_stopwords = []
  for word in b:
    if word not in english_stopwords:
      tokens_wo_stopwords.append(word)  

  # Proses Stemming
  ps = PorterStemmer()

  tokens_wo_stemming = []
  for word in tokens_wo_stopwords:
      tokens_wo_stemming.append(ps.stem(word))

  return " ".join(tokens_wo_stemming)

data['Clean Review'] = data['Description'].apply(clean)

data.to_csv('data-film-fix-preprocesing1.csv',index=False)