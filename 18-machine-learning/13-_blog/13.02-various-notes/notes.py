#!/usr/bin/env python3
# https://python3.info/machine-learning/_blog/various-notes.html


# %% Notes
# %%



# %% Program
# %%



# %% Wprowadzenie do Machine Learning
# %%



# %% Biblioteki numeryczne
# %%



# %% Tensorflow
# %%



# %% Program 2
# %%



# %% Cele zajęć
# %%



# %% Dzień 1
# %%



# %% Dzień 2
# %%



# %% Notatki
# %%



# %% Data Science
# - Scientific Computing (stara nazwa Data Science)
# - analiza danych
# - łączenie danych z różnych źródeł
# %%



# %% Trzy dziedziny Data Science
# - Data Science (wymaga trochę programowania, ale mniej niż Engineering)
# - Data Engineering (przerzucanie danych z lewa na prawo - więcej programowania)
# - Statystyk (budowanie rozbudowanych modelów danych)
# %%



# %% Jupyter
# - średnik usuwa wyświetlanie linii
# - zamykanie kerneli
# - instalowanie pluginów - spellchecker
# - list.pop? - znak zapytania wyświetla help do obiektu
# - %%timeit
# - % - globalne
# - %% - dla komorki
# - ! uruchamianie terminala pod spodem (interoperacyjne z pythonem)
# %%



# %% Machine Learning
# %%



# %% Klastry
# %%



# %% Sieci Neuronowe
# %%



# %% Regresja liniowa
# - Odczytywanie wartości z wykresu dla linii wykreślonej na podstawie danych.
# - Minimalna funkcja, która daje nam poprawną predykcję.
# - Mało podatna na overfitting
# - Podatna na underfitting
# - Dobra wartość dobroci w stosunku do trudności.
# - Bardzo często wykorzystywana.
# - Szczególnie często wykorzystywane w systemach RTB (Realtime Bidding) czyli system aukcji dla reklam na stronach, który musi wyrobić się w 100-200ms (trzeba uwzględnić narzut sieciowy). Dla takich przypadków stosuje się regresję liniową albo logistyczną, bo decyzja musi być podjęta bardzo szybko (wykorzystanie sieci neuronowych byłoby zbyt czasochłonne).
# %%



# %% Modele Chernove
# - Czy klient przedłuży umowę mając jakieś dane (analityk Ci mówi, bo dzwonił do 1000 osób i wie, że najczęściej zmieniają umowę gdy...):
# %%



# %% Regularyzacja
# - Regularyzacja - minimalizując funkcję kosztu, minimalizujesz wagi
# - Lasso L1 - sprowadza wartości nieistotne do zera (sprawdzić czy to nie definicja Ridge)
# - Ridge (dodaje regularyzację L2 wag) - sprowadza wartości nieistotne blisko do zera (sprawdzić czy to nie definicja Lasso)
# %%



# %% SVM
# - Kiedyś bardziej rozpowszechnione obecnie trochę mniej
# - Krenel Tricks (trik jądrowy)
# - Jeżeli dane nie są liniowo separowalne (tzn można przeprowadzić linię, która rozdzieli zbiór na dwie części)
# - Mapuje coś na jakąś funkcję np. koła i tak rozdziela punkty sprowadzając odległości od okręgu na płaszczyznę liniową (odległość punktu od okręgu)
# - Funkcji się raczej nie pisze, używamy już istniejące.
# - Stara się znaleźć taką linię, która nie tylko najlepiej aproksymuje punkty, ale także stara się by punkty graniczne były równoodległe od linii.
# - Funkcja Sinus jest przedziałami liniowa. Model wielomianowy jest lepiej dopasowany.
# - Lepiej jest zastosować OLS i dopasować sinusoidę (np. do sygnałów z szumem warto dopasować sinusoidę)
# - Zwykle jednak nie znamy jaka to funkcja i trzeba szukać.
# - Modele wielomianowe są dużo bardziej złożone obliczeniowo.
# - SVM jest przydatny kiedy mamy ładne nieliniowe granice.
# %%



# %% Classification
# %%



# %% Łańcuchy Markova
# - konwersja z reklam
# - totalnie nie interesuje Cię co nie konwertuje
# - patrzysz na to na czym ludzie odpadają (np. układ strony, pozycja itp)
# %%



# %% Regresja logistyczna
# - 1 / exp(...)
# - klasyfikuje na dwie części
# - Jeżeli mamy problem wieloklasowy, to możemy zastosować model (OVR) 1 vs. rest
# - Mamy klasa numer jeden (pierwszy zbiór) i reszta
# - A reszta znów jest podzielona na jeden i reszta
# %%



# %% Recall
# - Liczymy to ilościowo, tzn. czy zgadł czy nie
# - Precision - ile zgadł poprawnie z wszystkich
# - Recall - ile false positive wystąpiło
# - F1 - średnia precyzji i recall
# - F1 = 2 * (precision * recall) / (precision + recall)
# %%



# %% Ensemble
# - Ensemble to jest połączenie wielu modeli.
# - Najczęściej się to stosuje w połączeniu Modeli drzewiastych.
# %%



# %% K-Nearest Neighbors
# - To bardziej algorytm niż model. Programiści go lubią bo jest mniej matematyki.
# - Jest bardzo prosty.
# - Uczy się danych na pamięć.
# - Jest parametr, weights='uniform' (niezależnie od tego jak są daleko)
# - Ale możemy też ważyć ilu jest bliskich sąsiadów a ilu dalekich (weights='distance').
# - Można także użyć [callable] tj. przekazać funkcję, która liczy wagi
# %%



# %% Drzewa decyzyjne
# - Najczęściej w postaci drzewa binarnego - z dwoma opcjami:
# %%



# %% CART - Classification and Regression Trees
# %%



# %% Kalibracja parametrów modeli
# %%



# %% Ocena jakości modelu
# %%



# %% Dane tekstowe
# - Jak reprezentować tekst, aby można było coś na jego temat powiedzieć?
# - Dane tekstowe zazwyczaj przychodzą w formie dokumentów
# - Najczęściej klasyfikujemy dokumenty i przypisujemy im klasy (spam - nie spam, pozytywny tekst - negatywny)
# %%



# %% Term Frequency–Inverse Document Frequency (TF-IDF)
# %%



# %% Transformatory i pipeline
# - Transformer - jak transformujemy dane
# - Pipeline - łączy transformatory
# - Estimator - model
# %%



# %% Klasyfikacja danych tekstowych
# - SMS Spam Collection (https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip)
# - Dane są jako TSV (Tab Separated Values)
# %%



# %% Naive Bayes
# - Naive dlatego, że uznaje wszystkie cechy za liniowo niezależne
# - dla dokumentów tekstowych jest to bardzo poprawne
# - prawdopodobieństwo jest nie tylko zależne od tego ile razy wystąpiło, ale również z naszą wiedzą ekspercką
# %%



# %% Modelowanie tematów
# - uczenie bez nadzoru
# - gensim i model LDA (Latent Dirichlet Allocation)
# - pakiet nie usuwa stopwords
# %%



# %% Metody bez nadzoru
# - Klastrowanie - Minus: musimy powiedzieć ile chcemy mieć klastrów
# - Algorytm K-Means bardzo często wykorzystywany (liczą gdzie jest środek geometryczny punktów, a później klasyfikuje
# - Batch k-means - nie bierze wszystkich danych na raz, tylko dane po kawałku
# - K-Means można użyć do danych dużych (batch) oraz dla danych strumieniowych (przychodzących)
# - K-Means z pamięcią i z zapominaniem
# - W k-means nie przywiązywać się do nazwy klastrów (mogą być przydzielane losowo) ale zawsze ilość klastrów będzie się zgadzała
# - MiniBatchKMeans()
# - K-Means nie bardzo sobie radzi z tym jak klastry są podzielone
# - Jeżeli odległość między dwoma centroidami jest niewielka to opisują ten sam klaster
# - K-Means jest prosty obliczeniowo
# %%



# %% PCA
# - Analiza wektorów własnych macierzy kowariancji, które rozpinają system bazowy
# - gdy mamy dużo zmiennych które są skorelowane (np. Naive Bayes nie lubi tego)
# - często stosuje się do rysowania wielowymiarowych danych
# - Word to weg generuje 100-300 stopni swobody i można zastosować PCA aby sprowadzić do 2 lub 3 wymiarów
# - PCA jest transformatorem a nie modelem
# %%



# %% Sieci neuronowe
# - Detekcja sentymentów na podstawie wyrazu twarzy która patrzy na reklamę
# - SKLearn nie jest narzędziem deeplearningowym, ale ma w sobie zaimplementowane sieci neuronowe
# - Sieci neuronowe są dość trudne w porównaniu z innymi rodzajami
# - Przy analizie obrazu na wejściu są piksele w skali szarości.
# - matshow (część plt.subplot pokazuje macierz jako obrazek
# - Sieć neuronowa uczy się backpropagation w każdym przejściu sieci
# - Większość sieci bazuje na obrazkach 300x300 px
# - Preprocessing:
# %%



