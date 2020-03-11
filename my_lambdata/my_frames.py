

# my_lambdata/my_frames.py

import pandas

def add_state_names(my_df):
    """
    Add a column of state names to a dataframe that already has the abbrevs
    Param my_df pandas.DataFrame should have a column of "abbrev"
    Return a copy of the DataFrame with a new column called "name"
    """
    names_map = {"CT": "Conn", "CO": "Colorado", "CA": "Cali"}
    #breakpoint() # python 3.7 or later, otherwise use pdb module
    new_df = my_df.copy()
    new_df["name"] = my_df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    return new_df

df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
mutated_df = add_state_names(df) # desired invocation
print(mutated_df.head())

df2 = pandas.DataFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})
mutated_df2 = add_state_names(df2) # desired invocation
print(mutated_df2.head())
