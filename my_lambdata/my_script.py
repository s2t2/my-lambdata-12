
# my_lambdata/my_script.py

import pandas

from my_lambdata.my_mod import enlarge


print("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

df2 = pandas.DataFrame({"state": ["AZ", "DC", "MI", "WI"]})
print(df2.head())

print("-----------------")


x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!
