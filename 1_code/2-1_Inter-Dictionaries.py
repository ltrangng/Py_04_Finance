# DICTIONARIES

# Dictionaries are one of the most used data structures in Python
# Review the list data structure
my_list = ["a", "b", "c", "d"]
print(my_list)
# Looking up items in the list by index
my_list[0]
# Or determine the index by using its value
my_list.index("c")
# Dictionaries store and look up items using keys
dict = {"key-1": "value-1",
        "key-2": "value-2",
        "key-3": "value-3"}
print(dict) # each item has an unique key

# Create dictionaries
my_dict = {} # create an empty dictionary
# Or using the dict() function
my_dict = dict()
print(my_dict)
# Create a dictionary with initial values by expressing they keys and values
ticker_symbols = {"AAPL": "Apple", 
                  "F": "Ford",
                  "LUV": "Southwest"}
print(ticker_symbols)

# Adding to dictionaries
ticker_symbols["XON"] = "Exxon"
print(ticker_symbols)
# Use the same syntax to update the existing key
ticker_symbols["XON"] = "Exxon OLD" # ticker changed after Exxon Oil merged to Mobile

# Accessing values
ticker_symbols["F"]
# Accessing a key that's not in the dictionary throws an error
ticker_symbols["XOM"]
# To avoid this, make sure that the key is mapped in the dictionary
company = ticker_symbols.get("XOM") # if the key is missing, None is returned
print(company)
# Supply a second argument in the .get() method which will returns instead of "None"
company = ticker_symbols.get("XOM", "MISSING")
print(company)

# Deleting from dictionaries
del(ticker_symbols["XON"])
print(ticker_symbols)

# CUSIP is a nine-digit alphanumeric number used to identify most securities owned by American and Canadian companies. 
# Create a dictionary to look up the CUSIP number 
cusip_lookup = {} 
cusip_lookup["38259P706"] = "GOOG"
cusip_lookup["037833100"] = "AAPL"
print(cusip_lookup)
# Lookup the company by the CUSIP number
cusip_lookup["38259P706"] 

# Analyzing the change in stock prices over time is a common task in the world of finance. 
from datetime import datetime 
from datetime import timedelta
# Alphabet Inc. was formed in 2015 as part of a corporate restructuring of Google
alphabet_hist = {datetime(2019, 7, 30, 0, 0): 1228, 
                 datetime(2019, 7, 31, 0, 0): 1218.2, 
                 datetime(2019, 8, 1, 0, 0): 1211.78, 
                 datetime(2019, 8, 2, 0, 0): 1196.32}
print(alphabet_hist)
# Store stock data using the dates as keys and the prices as values in a dictionary
closing_price_date = datetime(2019, 8, 2, 0, 0)
# Closing price for the day before
day_before_closing_price_date = closing_price_date - timedelta(days = 1)
# Access the closing price for the day before in a way that is safe
print(alphabet_hist.get(day_before_closing_price_date))
# Get day eight weeks in future
future_closing_price_date = closing_price_date + timedelta(weeks = 8)
# Supply the default value 'Missing' to use if a key is missing 
print(alphabet_hist.get(future_closing_price_date, "Missing"))
# After deciding that the data might be incorrect, delete the entry
del(alphabet_hist[closing_price_date])
print(alphabet_hist)