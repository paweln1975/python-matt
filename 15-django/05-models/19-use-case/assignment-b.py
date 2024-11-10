
"""
* Assignment: Django Model Company
* Complexity: medium
* Lines of code: 50 lines
* Time: 34 min

English:
    1. Use `myproject` project
    2. Create app `company`
    3. Create model `Department` with fields:
        a. name
        b. employees list (m2m relation to Employee)
    4. Create model `Employee` with fields:
        a. first name
        b. last name
        c. salary USD
        d. is active (yes, no, unknown)
    5. Generate an admin panel:
        a. Add search by last name
        b. Add filter by status
        c. Add filter by salary (low, medium, high)
     6. Salary:
        a. low - up to 5_000
        b. medium - from 5_000 to 10_000
        c. high - above 10_000

Polish:
    1. Użyj projekt `myproject`
    2. Stwórz apkę `company`
    3. Stwórz model `Department` z polami:
        a. nazwa
        b. lista pracowników (relacja m2m do Employee)
    4. Stwórz model `Employee` z polami:
        a. imię
        b. nazwisko
        c. pensja USD
        d. jest aktywny (tak, nie, nieznany)
    5. Wygeneruj panel administracyjny:
        a. dodaj wyszukiwarkę po nazwisku
        b. dodaj filtr po statusie
        c. dodaj filtr po pensji (low, medium, high)
    6. Pensja:
        a. low - do 5_000
        b. medium - od 5_000 do 10_000
        c. high - powyżej 10_000

Hints:
    * models.CharField
    * models.DecimalField
    * models.ManyToManyField
    * models.BooleanField
    * admin.SimpleListFilter
    * search_fields
    * list_display
    * display_filter
"""


