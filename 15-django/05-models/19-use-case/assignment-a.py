"""
* Assignment: Django Model AddressBook
* Complexity: medium
* Lines of code: 50 lines
* Time: 34 min

English:
    0. Install `Pillow` package:
       `python -m pip install --upgrade pillow`
    1. Use `myproject` project
    2. Create app `addressbook`
   
    3. Create model `Address` with fields:
        a. type (choice: home, work)
        b. street
        c. house number
        d. apartment number
        e. post-code
        f. city
        g. region
        h. country
    4. Create model `Person` with fields:
        a. first name
        b. last name
        c. date of birth
        d. photo
        e. phone (choice: home, work, mobile)
        f. email (choice: home, work)
    5. Person can have many addresses, phones and emails
    6. Generate an admin panel:
        a. You can list contacts
        b. On the main screen you can see the basic fields of the person
        c. You can search contacts by last name
        d. You can filter contacts by date of birth
    7. Run doctests - all must succeed

Polish:
    0. Zainstaluj pakiet `Pillow`:
       `python -m pip install --upgrade pillow`
    1. Użyj projekt `myproject`
    2. Stwórz apkę `addressbook`
    3. Stwórz model `Address` z polami:
        a. Typ (do wyboru typ: domowy, praca)
        b. Ulica
        c. Numer bloku
        d. Numer mieszkania
        e. Kod pocztowy
        f. Miasto
        g. Region
        h. Kraj
    4. Stwórz model `Person` z polami:
        a. Imię
        b. Nazwisko
        c. Data Urodzenia
        d. Zdjęcie
        e. Telefon (do wyboru typ: domowy, praca, komórka)
        f. Email (do wyboru typ: domowy, praca)
    5. Osoba może mieć wiele adresów, telefonów i e-maili
    6. Wygeneruj panel administracyjny:
        a. Można wylistować kontakty
        b. Na głównym ekranie widoczne są podstawowe pola osoby
        c. Można wyszukiwać kontakty po nazwisku
        d. Można filtrować kontakty po dacie urodzenia
    7. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * models.CharField
    * models.DateField
    * models.ImageField
    * models.EmailField
    * models.ForeignKey
    * search_fields
    * list_filter
    * list_display
    * admin.StackedInline
    * admin.TabularInline
"""


