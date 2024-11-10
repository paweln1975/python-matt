#!/usr/bin/env python3

# Reference:
# https://python3.info/machine-learning/svm/support-vector-machines.html

#%% Support Vector Machines



#%% TL;DR
# Jeden z najbardziej popularnych algorytmów Machine Learning
# Dzieli :term:vector space za pomocą linii
# Wyszukuje linię taką linię, która ma największy margines pomiędzy wszystkimi punktami tzw. :term:best separating hyperplane
# Dla nieznanego punktu sprawdza po której stronie krzywej się znajduje i na podstawie tego określa przynależność
# Linia prosta jest najprostszym przypadkiem
# Może się okazać, że konieczne będzie przeprowadzenie bardzo skomplikowanej krzywej
# Jeżeli dane są zgrupowane w wielowymiarowej przestrzeni, trzeba będzie użyć zbioru



#%% Charakterystyka algorytmu



#%% Przeznaczenie



#%% Zalety algorytmu
# Guaranteed Optimality: Due to the nature of Convex Optimization, the solution is guaranteed to be the global minimum not a local minimum.



#%% Wady algorytmu
# In Natural Language Processing, structured representations of text yield better performances. Sadly, SVMs can not accommodate such structures(word embeddings) and are used through Bag-of-Words representation which loses sequentially information and leads to worse performance.



#%% Opis algorytmu



#%% Definicja intuicyjna



#%% Definicja formalna
# Tą metodą wykonuje się regresję i klasyfikację, konstruując nieliniowe granice decyzyjne.
# Istnieje kilka typów wektorów nośnych, z różnymi funkcjami bazowymi:



#%% Support Vector Machines (Kernels)
# :math:f(x) = B0 + sum(ai * (x,xi))



#%% Linear Kernel SVM
# :math:K(x, xi) = sum(x * xi)



#%% Polynomial Kernel SVM
# :math:K(x,xi) = 1 + sum(x * xi)^d



#%% Radial Kernel SVM
# :math:K(x,xi) = exp(-gamma * sum((x – xi^2))



#%% Przykłady praktyczne



#%% Przykład wykorzystania ``sklearn``



#%% Przygotowanie do przykładów



#%% Motivating Support Vector Machines



#%% Maximizing the Margin



#%% Fitting a Support Vector Machine



#%% Going further: Kernel Methods