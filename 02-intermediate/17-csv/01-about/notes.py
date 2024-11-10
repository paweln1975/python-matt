#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/csv/about.html

#%% CSV About
# CSV - Comma/Character Separated Values
# No CSV formal standard, just a practice
# Flat file (2D) without relations
# Relations has to be flatten (serialization, additional columns, etc...)
# Typically first line (header) represents column names
# Rarely first line can also have a structure (nrows, ncols)
# Internationalization: encoding
# Localization: decimal separator, thousands separator, date format
# Parameters: delimiter, quotechar, quoting, lineterminator, dialect



#%% Header



#%% Delimiter
# csv module expects delimeter to be 1-character in length



#%% Quotechar
# " - quote char (best)
# ' - apostrophe



#%% Quoting
# csv.QUOTE_ALL (safest)
# csv.QUOTE_MINIMAL
# csv.QUOTE_NONE
# csv.QUOTE_NONNUMERIC



#%% Lineterminator
# \r\n - New line on Windows
# \n - New line on *nix
# *nix operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)



#%% Decimal Separator
# 1.0 - Decimal point
# 1,0 - Decimal comma
# 0٫‎1 - Arabic decimal separator (Left to right)
# More information: [#WikipediaDecimalSeparator]_



#%% Thousands Separator
# 1000000 - None
# 1'000'000 - Apostrophe
# 1 000 000 - Space, the internationally recommended thousands separator
# 1.000.000 - Period, used in many non-English speaking countries
# 1,000,000 - Comma, used in most English-speaking countries



#%% Date and Time



#%% Encoding
# utf-8 - international standard (should be always used!)
# iso-8859-1 - ISO standard for Western Europe and USA
# iso-8859-2 - ISO standard for Central Europe (including Poland)
# cp1250 or windows-1250 - Central European encoding on Windows
# cp1251 or windows-1251 - Eastern European encoding on Windows
# cp1252 or windows-1252 - Western European encoding on Windows
# ASCII - ASCII characters only



#%% Dialects



#%% Good Practices