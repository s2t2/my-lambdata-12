

# my_lambdata/my_frames.py

import pandas

# State abbreviation -> Full Name and visa versa.
# FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

df2 = pandas.DataFrame({"state": ["AZ", "DC", "CO", "MI", "WI"]})
print(df2.head())
