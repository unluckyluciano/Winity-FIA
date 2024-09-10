import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

#Carichiamo il dataset delle valutazioni e dei film
valutazioni = pd.read_csv('rating.csv')
valutazioni_porzione = valutazioni.sample(frac=0.001, random_state=42)  #riduzione della dimensione del dataset
film = pd.read_csv('movie.csv')

#Dividiamo il dataset di valutazioni in set di allenamento (80%) e set di test (20%)
dati_allenamento, dati_test = train_test_split(valutazioni_porzione, test_size=0.2, random_state=42)

#Creiamo la matrice utente-film usando solo il set di allenamento
matrice_utente_film = dati_allenamento.pivot_table(index='userId', columns='movieId', values='rating')

#Sostituiamo i valori mancanti con 0
matrice_utente_film.fillna(0, inplace=True)