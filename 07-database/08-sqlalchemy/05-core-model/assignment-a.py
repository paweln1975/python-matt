"""
* Assignment: Model Data Iris
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Model data in `DATA`
        a. What is the name of the model?
        b. What are the names of the fields?
        c. What are the types of fields?
    2. Non-functional requirements:
        a. Use SQLAlchemy ORM to create models
        b. Do not convert data, just model it
        c. You can use any module from the standard library
        d. You can use SQLAlchemy and Alembic
        e. Do not install or use additional packages

Polish:
    1. Zamodeluj dane w `DATA`
        a. Jak nazywa się model?
        b. Jak nazywają się pola?
        c. Jakie typy mają pola?
    2. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Nie konwertuj danych, tylko je zamodeluj
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów

"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

