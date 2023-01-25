import pandas as pd
import re

data = pd.read_csv('film/data-film.csv',encoding='utf-8')

data['Rating'] = data['Rating'].apply(lambda x: ' '.join(re.findall(r"\w+",str(x))))
data['Genre'] = data['Genre'].apply(lambda x: " ".join(re.findall(r"\w+",str(x))))
data['Original Lenguage'] = data['Original Lenguage'].apply(lambda x: " ".join(re.findall(r"\w+",str(x))))
data['Producer'] = data['Producer'].apply(lambda x: " ".join(re.findall(r"\w+",str(x))))
data['Release Date(Stremming)'] = data['Release Date(Stremming)'].apply(lambda x: " ".join(re.findall(r"\w+",str(x))))
data['Box Office(Gros USA)'] = data['Box Office(Gros USA)'].apply(lambda x: " ".join(re.findall(r"\w+",str(x))))
data['Runtime'] = data['Runtime'].apply(lambda x: " ".join(re.findall(r"\w+",str(x))))

data.to_csv('data-film-fix.csv',index=False)